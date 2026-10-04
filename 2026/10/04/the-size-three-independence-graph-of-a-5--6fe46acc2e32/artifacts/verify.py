from itertools import permutations, combinations
from collections import deque, Counter


def parity(p):
    c = 0
    for i in range(5):
        for j in range(i + 1, 5):
            c += p[i] > p[j]
    return c & 1


def compose(p, q):
    return tuple(p[q[i]] for i in range(5))


def permutation_order(p):
    e = tuple(range(5))
    x = e
    for k in range(1, 61):
        x = compose(x, p)
        if x == e:
            return k
    raise AssertionError("order failure")


def fixed_points(p):
    return frozenset(i for i in range(5) if p[i] == i)


elems = [p for p in permutations(range(5)) if parity(p) == 0]
assert len(elems) == 60
index = {p: i for i, p in enumerate(elems)}
identity = index[tuple(range(5))]

mult = [[index[compose(a, b)] for b in elems] for a in elems]
inv = []
for i in range(60):
    found = None
    for j in range(60):
        if mult[i][j] == identity and mult[j][i] == identity:
            found = j
            break
    assert found is not None
    inv.append(found)


def generated(gens):
    steps = list(dict.fromkeys(list(gens) + [inv[g] for g in gens]))
    seen = {identity}
    q = deque([identity])
    while q:
        x = q.popleft()
        for g in steps:
            y = mult[x][g]
            if y not in seen:
                seen.add(y)
                q.append(y)
    return frozenset(seen)

orders = [permutation_order(p) for p in elems]
assert Counter(orders) == Counter({1: 1, 2: 15, 3: 20, 5: 24})
nonidentity = [i for i in range(60) if i != identity]

pair_full = set()
pair_size = {}
for a, b in combinations(nonidentity, 2):
    H = generated((a, b))
    pair_size[(a, b)] = len(H)
    if len(H) == 60:
        pair_full.add((a, b))
assert len(pair_full) == 1140

minimal_triples = []
for t in combinations(nonidentity, 3):
    if any(tuple(sorted(pair)) in pair_full for pair in combinations(t, 2)):
        continue
    if len(generated(t)) == 60:
        minimal_triples.append(t)
assert len(minimal_triples) == 1240

adj3 = {}
for t in minimal_triples:
    for x in t:
        adj3.setdefault(x, set())
    for a, b in combinations(t, 2):
        adj3[a].add(b)
        adj3[b].add(a)

assert len(adj3) == 35
assert Counter(orders[x] for x in adj3) == Counter({2: 15, 3: 20})
assert all(x not in adj3 for x in nonidentity if orders[x] == 5)

involutions = [x for x in adj3 if orders[x] == 2]
threecycles = [x for x in adj3 if orders[x] == 3]

# All involutions form a clique.
for a, b in combinations(involutions, 2):
    assert b in adj3[a]

# Three-cycle adjacency is exactly one common fixed point.
for a, b in combinations(threecycles, 2):
    want = len(fixed_points(elems[a]) & fixed_points(elems[b])) == 1
    assert (b in adj3[a]) == want

# Cross adjacency is exactly failure to generate A5.
for a in involutions:
    for b in threecycles:
        key = tuple(sorted((a, b)))
        want = pair_size[key] < 60
        assert (b in adj3[a]) == want

assert Counter(len(adj3[x]) for x in involutions) == Counter({26: 15})
assert Counter(len(adj3[x]) for x in threecycles) == Counter({21: 20})
assert sum(len(v) for v in adj3.values()) // 2 == 405

# Exact diameter and connectivity of Delta_3.
def diameter(adj):
    dmax = 0
    for s in adj:
        dist = {s: 0}
        q = deque([s])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1
                    q.append(y)
        assert len(dist) == len(adj)
        dmax = max(dmax, max(dist.values()))
    return dmax

assert diameter(adj3) == 2

# Ordinary generating graph Delta_2 is connected of diameter 2.
adj2 = {x: set() for x in nonidentity}
for a, b in pair_full:
    adj2[a].add(b)
    adj2[b].add(a)
assert all(adj2[x] for x in nonidentity)
assert diameter(adj2) == 2

print("VERIFY_OK")
print("generating_pairs=1140")
print("minimal_generating_triples=1240")
print("delta3_vertices=35")
print("delta3_edges=405")
print("delta3_degree_counts=26x15,21x20")
print("delta3_diameter=2")
