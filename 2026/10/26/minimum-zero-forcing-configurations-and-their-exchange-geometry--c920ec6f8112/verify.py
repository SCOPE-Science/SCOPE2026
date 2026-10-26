"""Exhaustive certificate for minimum zero forcing in the line graph of KG(5,2).

Python 3.10+; standard library only. Running this file rebuilds the graph,
independently checks its forcing closures, and counts all optimal seeds,
S5-orbits, propagation rounds, and distances between optimal seeds.
"""
from collections import Counter, deque
from itertools import combinations, permutations
from math import comb

KVERT = tuple(combinations(range(5), 2))
PEDGES = tuple((i, j) for i, j in combinations(range(10), 2)
               if set(KVERT[i]).isdisjoint(KVERT[j]))
assert len(KVERT) == 10 and len(PEDGES) == 15

# The 15 edges of the Petersen graph are the 15 line-graph vertices.
NEIGH = tuple(frozenset(j for j, f in enumerate(PEDGES)
                        if i != j and not set(e).isdisjoint(f))
              for i, e in enumerate(PEDGES))
assert all(len(x) == 4 for x in NEIGH)
assert sum(map(len, NEIGH)) // 2 == 30
assert all((j in NEIGH[i]) == (i in NEIGH[j]) for i in range(15)
           for j in range(15))
B = tuple(sum(1 << j for j in s) for s in NEIGH)
ALL = (1 << 15) - 1


def bit_closure(initial):
    """Simultaneous rounds, using bit operations."""
    blue = initial
    sizes = [blue.bit_count()]
    while True:
        new = 0
        for i in range(15):
            if (blue >> i) & 1:
                whites = B[i] & ~blue
                if whites and (whites & (whites - 1)) == 0:
                    new |= whites
        if not (new & ~blue):
            break
        blue |= new
        sizes.append(blue.bit_count())
    return blue, tuple(sizes)


def set_closure(initial):
    """Independent literal-set implementation, no bitwise propagation."""
    blue = {i for i in range(15) if initial & (1 << i)}
    sizes = [len(blue)]
    while True:
        candidates = set()
        for u in sorted(blue):
            targets = NEIGH[u] - blue
            if len(targets) == 1:
                candidates.update(targets)
        if not candidates:
            break
        blue.update(candidates)
        sizes.append(len(blue))
    return frozenset(blue), tuple(sizes)


# Exhaustion over all initial states, not a random sample.
for x in range(1 << 15):
    end, st = bit_closure(x)
    end2, st2 = set_closure(x)
    assert end == sum(1 << v for v in end2)
    assert st == st2

# Every smaller size is tested; monotonicity also lets six-set
# non-forcing imply that no subset of size at most six is forcing.
for size in range(7):
    assert not any(bit_closure(sum(1 << j for j in subset))[0] == ALL
                   for subset in combinations(range(15), size))

OPT = tuple(sum(1 << j for j in subset)
            for subset in combinations(range(15), 7)
            if bit_closure(sum(1 << j for j in subset))[0] == ALL)
OPTSET = set(OPT)
assert len(OPT) == len(OPTSET) == 2280
PT = Counter(len(bit_closure(x)[1]) - 1 for x in OPT)
assert PT == {3: 120, 4: 1440, 5: 720}

# Each permutation of the five underlying symbols acts on Petersen
# vertices (two-subsets), then on Petersen edges (line-graph vertices).
KINDEX = {v: i for i, v in enumerate(KVERT)}
EINDEX = {e: i for i, e in enumerate(PEDGES)}
GROUP = []
for p in permutations(range(5)):
    vm = [KINDEX[tuple(sorted(p[t] for t in v))] for v in KVERT]
    em = tuple(EINDEX[tuple(sorted((vm[u], vm[v])))] for u, v in PEDGES)
    GROUP.append(em)
assert len(set(GROUP)) == 120


def action(m, perm):
    return sum(1 << perm[j] for j in range(15) if (m >> j) & 1)


pending = set(OPT)
ORBIT_REPS = []
while pending:
    rep = min(pending)
    orbit = {action(rep, g) for g in GROUP}
    assert orbit.issubset(OPTSET)
    pending.difference_update(orbit)
    ORBIT_REPS.append((rep, len(orbit), len(bit_closure(rep)[1]) - 1))
assert len(ORBIT_REPS) == 21
assert Counter(s for _, s, _ in ORBIT_REPS) == {60: 4, 120: 17}
assert sum(s for _, s, _ in ORBIT_REPS) == len(OPT)
assert [m for m, _, _ in ORBIT_REPS] == [
    239, 247, 253, 254, 439, 687, 695, 699, 701, 702, 762,
    979, 981, 4334, 4341, 4345, 4346, 4495, 4503, 4555, 4781]

# One-vertex replacement inside the optimal family.
INDEX = {m: i for i, m in enumerate(OPT)}
EDGES = [set() for m in OPT]
for i, m in enumerate(OPT):
    for u in range(15):
        if (m >> u) & 1:
            for v in range(15):
                if not ((m >> v) & 1):
                    t = m ^ (1 << u) ^ (1 << v)
                    if t in INDEX:
                        EDGES[i].add(INDEX[t])
assert all(i in EDGES[j] for j, a in enumerate(EDGES) for i in a)
assert sum(map(len, EDGES)) // 2 == 28650
# Independent unordered-pair cross-check of the one-replacement criterion.
assert sum(1 for i, a in enumerate(OPT) for b in OPT[i+1:]
           if (a ^ b).bit_count() == 2) == 28650
assert Counter(map(len, EDGES)) == {
    22: 180, 23: 480, 24: 240, 25: 240,
    26: 660, 27: 240, 28: 60, 29: 180}

HIST = Counter()
for start in range(len(OPT)):
    dist = [-1] * len(OPT)
    dist[start] = 0
    todo = deque([start])
    while todo:
        u = todo.popleft()
        for v in EDGES[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                todo.append(v)
    assert min(dist) == 0
    assert max(dist) <= 7  # every other optimum is reachable
    for d in dist[start+1:]:
        HIST[d] += 1
assert HIST == {1: 28650, 2: 234120, 3: 765570, 4: 1004640,
                5: 483480, 6: 78540, 7: 3060}
assert sum(HIST.values()) == comb(len(OPT), 2)

print('VERIFY_OK')
print('petersen_vertices=10 petersen_edges=15 line_graph_edges=30')
print('zero_forcing_number=7 minimum_sets=2280 orbit_sizes={60:4,120:17}')
print('propagation={3:120,4:1440,5:720}')
print('exchange_vertices=2280 exchange_edges=28650 diameter=7')
print('exchange_distances=', dict(sorted(HIST.items())))
print('orbit_reps=', ORBIT_REPS)
