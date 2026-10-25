#!/usr/bin/env python3
"""Exact standalone combinatorial certificate for the Coxeter graph Rips filtration.
Run: python3 check_coxeter.py. Python standard library only.
"""
from collections import Counter, deque
from itertools import combinations

ORDER = (15, 22, 3, 12, 13, 17, 9, 27, 25, 7, 5, 14, 11, 24,
         20, 18, 1, 26, 21, 2, 23, 6, 4, 8, 0, 19, 16, 10)
N = 28

def bits(m):
    while m:
        b = m & -m
        yield b.bit_length() - 1
        m ^= b

def mask(xs):
    return sum(1 << x for x in xs)

# Standard Fano-plane lines and nonline triples; Coxeter adjacency is disjointness.
lines = {frozenset((i % 7, (i + 1) % 7, (i + 3) % 7)) for i in range(7)}
triples = [frozenset(t) for t in combinations(range(7), 3) if frozenset(t) not in lines]
assert len(lines) == 7 and len(triples) == N
adj = [set() for _ in range(N)]
for i, j in combinations(range(N), 2):
    if triples[i].isdisjoint(triples[j]):
        adj[i].add(j)
        adj[j].add(i)
assert all(len(a) == 3 for a in adj)
assert sum(map(len, adj)) // 2 == 42

# BFS shortest path distances and distance-regular shell count.
dist = []
for root in range(N):
    dd = [-1] * N
    dd[root] = 0
    queue = deque([root])
    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if dd[w] == -1:
                dd[w] = dd[v] + 1
                queue.append(w)
    assert Counter(dd) == {0: 1, 1: 3, 2: 6, 3: 12, 4: 6}
    dist.append(dd)

def faces_at(r):
    close = [mask(j for j in range(N) if j != i and dist[i][j] <= r)
             for i in range(N)]
    faces = set()
    def visit(current, candidates):
        while candidates:
            b = candidates & -candidates
            v = b.bit_length() - 1
            candidates ^= b
            f = current | b
            faces.add(f)
            visit(f, candidates & close[v])
    visit(0, (1 << N) - 1)
    return faces

# Exact scale-two elementary collapses, fixing the scale-one graph.
k2 = faces_at(2)
assert Counter(f.bit_count() - 1 for f in k2) == {0: 28, 1: 126, 2: 112, 3: 28}
active = set(k2)
def elementary(lower, upper):
    assert lower in active and upper in active
    assert upper.bit_count() == lower.bit_count() + 1
    assert (lower & upper) == lower
    assert all((f == upper) for f in active if f != lower and (f & lower) == lower)
    active.remove(lower)
    active.remove(upper)

for v in range(N):
    nbrs = sorted(adj[v])
    elementary(mask(nbrs), mask(nbrs + [v]))
for v in range(N):
    for a, b in combinations(sorted(adj[v]), 2):
        elementary(mask((a, b)), mask((a, b, v)))
original_faces = {1 << i for i in range(N)} | \
                 {mask((i, j)) for i in range(N) for j in adj[i] if i < j}
assert active == original_faces
assert len(k2) - len(active) == 224
print('radius 2: 112 certified collapses onto original 28-vertex 42-edge graph')

# Exhaustive scale-three cliques and acyclic Forman matching.
k3 = faces_at(3)
fvector = Counter(f.bit_count() - 1 for f in k3)
assert fvector == {0: 28, 1: 294, 2: 1456, 3: 3514,
                   4: 3864, 5: 1596, 6: 144}
assert len(k3) == 10896
assert sorted(ORDER) == list(range(N))
used = set()
matching = set()
for vertex in ORDER:
    m = 1 << vertex
    # For a fixed vertex these potential pairs are disjoint, so iteration order
    # does not affect the result.
    for face in k3:
        upper = face | m
        if face & m or face in used or upper not in k3 or upper in used:
            continue
        used.add(face)
        used.add(upper)
        matching.add((face, upper))
critical = k3 - used
assert len(matching) == 5404 and len(critical) == 88
assert Counter(f.bit_count() - 1 for f in critical) == {0: 1, 4: 87}

# Directed Hasse graph: coface -> face for ordinary incidences;
# face -> coface for matched incidences. Kahn exhausts the entire graph iff
# the matching contains no nontrivial closed alternating gradient path.
faces = sorted(k3)
index = {f: i for i, f in enumerate(faces)}
arrow = [[] for _ in faces]
indegree = [0] * len(faces)
for upper in faces:
    for v in bits(upper):
        lower = upper ^ (1 << v)
        if not lower:
            continue
        if (lower, upper) in matching:
            source, target = index[lower], index[upper]
        else:
            source, target = index[upper], index[lower]
        arrow[source].append(target)
        indegree[target] += 1
queue = deque(i for i, degree in enumerate(indegree) if degree == 0)
visited = 0
while queue:
    source = queue.popleft()
    visited += 1
    for target in arrow[source]:
        indegree[target] -= 1
        if indegree[target] == 0:
            queue.append(target)
assert visited == len(faces), f'cyclic matching: visited={visited}'
print('radius 3: 10896 faces, 5404 disjoint matched pairs,')
print('          Hasse DAG verified, one critical vertex and 87 critical four-cells')
assert max(max(row) for row in dist) == 4  # Every vertex pair is a scale-four edge.
print('radius 4: full simplex; integral wedge and persistence classification PASS')
