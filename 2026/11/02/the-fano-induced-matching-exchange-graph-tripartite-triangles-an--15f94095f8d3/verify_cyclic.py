#!/usr/bin/env python3
"""Cyclic-design, compatible-pair, and automorphism verifier for Fano flag exchange."""
from itertools import combinations, permutations
from collections import Counter, deque

# Independent model: the seven translates of the (7,3,1) difference set.
D = (0, 1, 3)
lines = tuple(frozenset((i + d) % 7 for d in D) for i in range(7))
assert len(set(lines)) == 7
assert all(sum({p, q}.issubset(l) for l in lines) == 1 for p, q in combinations(range(7), 2))
flags = tuple((p, i) for i in range(7) for p in sorted(lines[i]))
assert len(flags) == 21

def compatible(x, y):
    return x[0] not in lines[y[1]] and y[0] not in lines[x[1]]

# Start from 84 compatible *pairs*, not triples or a vertex-exchange search.
pairs = tuple(p for p in combinations(flags, 2) if compatible(*p))
assert len(pairs) == 84
triangles = []
for p in pairs:
    completions = tuple(f for f in flags if compatible(f, p[0]) and compatible(f, p[1]))
    assert len(completions) == 3
    triangles.append(tuple(frozenset(p + (f,)) for f in completions))
matchings = tuple(sorted({m for ts in triangles for m in ts}, key=lambda x: sorted(x)))
assert len(matchings) == 84
index = {m: k for k, m in enumerate(matchings)}
adj = [set() for _ in matchings]
for tri in triangles:
    for a, b in combinations(tri, 2):
        ia, ib = index[a], index[b]
        adj[ia].add(ib)
        adj[ib].add(ia)
assert all(len(ns) == 6 for ns in adj)
assert sum(map(len, adj)) // 2 == 252

def classification(m):
    pts = {p for p, i in m}
    lis = {i for p, i in m}
    col = any(pts.issubset(line) for line in lines)
    con = any(all(x in lines[i] for i in lis) for x in range(7))
    if not col:
        assert con
        return 'A'
    return 'C' if con else 'B'

classes = tuple(classification(m) for m in matchings)
assert Counter(classes) == {'A': 28, 'B': 28, 'C': 28}
assert all({classification(m) for m in tr} == {'A', 'B', 'C'} for tr in triangles)

# Exhaustively construct all point/line collineations and one point-line duality.
line_index = {l: i for i, l in enumerate(lines)}
collineations = []
for perm in permutations(range(7)):
    mapped = tuple(frozenset(perm[p] for p in line) for line in lines)
    if all(line in line_index for line in mapped):
        collineations.append((perm, tuple(line_index[l] for l in mapped)))
assert len(collineations) == 168

def apply_col(m, auto):
    pmap, lmap = auto
    return frozenset((pmap[p], lmap[j]) for p, j in m)

def dual(m):
    # (p,j) -> (-j,-p); incidence is preserved since p-j in {0,1,3}.
    return frozenset(((-j) % 7, (-p) % 7) for p, j in m)

for m in matchings:
    assert dual(m) in index
    for a in collineations:
        assert apply_col(m, a) in index
orbits = []
remaining = set(matchings)
while remaining:
    m = next(iter(remaining))
    orbit = {apply_col(m, a) for a in collineations}
    orbits.append(orbit)
    remaining -= orbit
assert len(orbits) == 3 and sorted(map(len, orbits)) == [28] * 3
assert {frozenset(classes[index[m]] for m in orbit) for orbit in orbits} == {
    frozenset({'A'}), frozenset({'B'}), frozenset({'C'})}
assert all(classification(dual(m)) == {'A': 'B', 'B': 'A', 'C': 'C'}[classification(m)]
           for m in matchings)

# Three representative BFS's suffice by the actual 168 graph automorphisms.
reps = {t: classes.index(t) for t in 'ABC'}
profiles = {}
for t, root in reps.items():
    dist = {root: 0}
    todo = deque([root])
    while todo:
        v = todo.popleft()
        for w in adj[v]:
            if w not in dist:
                dist[w] = dist[v] + 1
                todo.append(w)
    assert len(dist) == 84
    profiles[t] = tuple(Counter(dist.values())[d] for d in range(6))
assert profiles == {'A': (1, 6, 21, 34, 18, 4),
                    'B': (1, 6, 21, 34, 18, 4),
                    'C': (1, 6, 18, 35, 24, 0)}
# Vertex-transitive within each 28-element collineation orbit.
counts = Counter()
for d in range(1, 6):
    counts[d] = sum(28 * profiles[t][d] for t in 'ABC') // 2
assert counts == {1: 252, 2: 840, 3: 1442, 4: 840, 5: 112}
print('CYCLIC_FLAG_PAIR_AND_AUTOMORPHISM_PASS')
print('GL3_order=168 duality=valid; 3 collineation orbits of size 28; exact BFS profiles=', profiles)
print('distance_pairs=', sorted(counts.items()))
