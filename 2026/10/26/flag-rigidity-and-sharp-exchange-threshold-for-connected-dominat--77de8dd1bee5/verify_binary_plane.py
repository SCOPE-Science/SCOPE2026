"""Standalone exhaustive checks in the order-two projective plane (stdlib only)."""
from collections import Counter, deque
from itertools import combinations

q = 2
points = tuple(range(1, 8))
lines = tuple(sorted({tuple(sorted((a, b, a ^ b)))
                      for a in points for b in points if a != b}))
assert len(lines) == 7
N = len(points)
neighbors = [set() for _ in range(2 * N)]
for j, line in enumerate(lines):
    for p in line:
        neighbors[p - 1].add(N + j)
        neighbors[N + j].add(p - 1)
assert all(len(s) == q + 1 for s in neighbors)


def connected(chosen):
    seen = {next(iter(chosen))}
    stack = list(seen)
    while stack:
        u = stack.pop()
        for v in neighbors[u] & chosen:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen == chosen


def dominating(chosen):
    return all(v in chosen or neighbors[v] & chosen for v in range(2 * N))

min_sets = []
counts = Counter()
for mask in range(1, 1 << (2 * N)):
    s = {v for v in range(2 * N) if (mask >> v) & 1}
    if dominating(s) and connected(s):
        counts[len(s)] += 1
        if len(s) == 2 * (q + 1):
            min_sets.append(frozenset(s))
assert min(counts) == 6

flags = []
for i, line in enumerate(lines):
    for p in line:
        S = {x - 1 for x in line} | {N + j for j, L in enumerate(lines) if p in L}
        flags.append(frozenset(S))
assert len(flags) == 21
assert set(flags) == set(min_sets)


def swap_distance(a, b):
    return len(a - b)

assert all(swap_distance(a, b) >= 2
           for a, b in combinations(flags, 2))

adj = [set() for _ in flags]
for i, a in enumerate(flags):
    for j, b in enumerate(flags):
        if i != j and swap_distance(a, b) <= q:
            adj[i].add(j)
assert all(len(a) == 2 * q for a in adj)
assert sum(map(len, adj)) // 2 == 42

def distances(i):
    D = {i: 0}
    queue = deque([i])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v not in D:
                D[v] = D[u] + 1
                queue.append(v)
    return D

assert all(len(distances(i)) == 21 and max(distances(i).values()) == 3
           for i in range(len(flags)))

# The unique maximum-leaf tree for each flag has the induced double star
# plus one edge from each outside vertex to its unique selected neighbor.
trees = set()
for S in flags:
    edges = {tuple(sorted((u, v))) for u in S for v in neighbors[u] & S if u < v}
    assert len(edges) == len(S) - 1
    for v in set(range(14)) - S:
        attaches = neighbors[v] & S
        assert len(attaches) == 1
        edges.add(tuple(sorted((v, next(iter(attaches))))))
    assert len(edges) == 13
    degree = Counter(z for e in edges for z in e)
    assert sum(degree[v] == 1 for v in range(14)) == 8
    trees.add(frozenset(edges))
assert len(trees) == 21
print('q=2, 14 graph vertices, 21 incident flags')
print('minimum connected domination = 6, count =', len(min_sets))
print('minimum-set ordinary single-vertex exchange edges = 0')
print('two-vertex exchange edges = 42, degree = 4, radius = diameter = 3')
print('maximum leaves = 8, maximum-leaf spanning trees =', len(trees))
print('all assertions passed')
