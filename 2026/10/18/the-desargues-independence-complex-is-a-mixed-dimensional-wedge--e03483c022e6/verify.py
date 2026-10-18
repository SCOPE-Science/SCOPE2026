#!/usr/bin/env python3
"""Exact, dependency-free verification of an independence-complex collapse.

The graph is the canonical bipartite double cover of the Petersen graph.
Vertices 0..9 and 10..19 are its two sheets.  All combinatorial
incidences and integral Morse coefficients are recomputed from scratch.
"""
from collections import Counter, deque
from functools import lru_cache

N = 20
petersen_edges = set()
for i in range(5):
    for a, b in ((i, (i + 1) % 5),
                 (i + 5, 5 + (i + 2) % 5),
                 (i, i + 5)):
        petersen_edges.add(tuple(sorted((a, b))))
assert len(petersen_edges) == 15
edges = set()
for a, b in petersen_edges:
    edges.add(tuple(sorted((a, b + 10))))
    edges.add(tuple(sorted((a + 10, b))))
assert len(edges) == 30

# A permutation displays the isomorphism to the generalized Petersen
# graph GP(10,3); it was found by a graph-isomorphism search and is now
# checked here only by the 30 undirected edge equalities.
to_gp = (10, 12, 14, 9, 5, 18, 7, 16, 3, 1,
         15, 17, 19, 4, 0, 13, 2, 11, 8, 6)
assert sorted(to_gp) == list(range(N))
gp_edges = set()
for i in range(10):
    for a, b in ((i, (i + 1) % 10), (i, 10 + i),
                 (10 + i, 10 + (i + 3) % 10)):
        gp_edges.add(tuple(sorted((a, b))))
assert {tuple(sorted((to_gp[a], to_gp[b]))) for a, b in edges} == gp_edges

neighbours = [0] * N
for a, b in edges:
    neighbours[a] |= 1 << b
    neighbours[b] |= 1 << a
assert all(n.bit_count() == 3 for n in neighbours)
faces = [0]
for v in range(N):
    bit = 1 << v
    faces += [s | bit for s in faces if not s & neighbours[v]]
face_set = set(faces)
assert len(face_set) == len(faces) == 6212
counts = Counter(s.bit_count() for s in faces)
assert tuple(counts.get(k, 0) for k in range(11)) == (
    1, 20, 160, 660, 1510, 1924, 1320, 480, 115, 20, 2)

def oriented_boundary(s):
    return [(s ^ (1 << v), (-1) ** i)
            for i, v in enumerate(v for v in range(N) if s >> v & 1)]

# Sequential element matchings: at each vertex match every currently
# available lower face with its one-vertex coface.
remaining = set(faces)
pairs = []
for v in range(N):
    bit = 1 << v
    for a in sorted(s for s in remaining if not s & bit):
        b = a | bit
        if b in remaining:
            remaining.remove(a)
            remaining.remove(b)
            pairs.append((a, b))
assert len(pairs) == 3103
assert len(remaining) == 6
crit4 = sorted(s for s in remaining if s.bit_count() == 5)
crit5 = sorted(s for s in remaining if s.bit_count() == 6)
assert crit4 == [0x7c00]
assert crit5 == sorted((0x71c00, 0xe2c00, 0x99c00, 0xccc00, 0x2ec00))
assert len(crit4) == 1 and len(crit5) == 5
assert set(remaining) == set(crit4 + crit5)
assert sum(bool(a == 0) for a, b in pairs) == 1
assert all(b.bit_count() == a.bit_count() + 1 and (a & b) == a for a, b in pairs)

# Exhaustive acyclicity test: orient every unmatched Hasse edge from
# coface to face; reverse every matched Hasse edge.
reverse = {(a, b) for a, b in pairs}
indegree = {s: 0 for s in faces}
successors = {s: [] for s in faces}
arcs = 0
for s in faces:
    for t, sign in oriented_boundary(s):
        if (t, s) in reverse:
            source, target = t, s
        else:
            source, target = s, t
        successors[source].append(target)
        indegree[target] += 1
        arcs += 1
queue = deque(s for s, d in indegree.items() if d == 0)
processed = 0
while queue:
    s = queue.popleft()
    processed += 1
    for t in successors[s]:
        indegree[t] -= 1
        if indegree[t] == 0:
            queue.append(t)
assert processed == len(faces), f'directed Hasse cycle: processed={processed}'

# Exact integral chain-cancellation recurrence: coefficient of the
# critical 4-simplex when a 4-face is reduced along paired 4/5 faces.
up = dict(pairs)
@lru_cache(None)
def coefficient(s):
    assert s.bit_count() == 5
    if s == crit4[0]:
        return 1
    upper = up.get(s)
    if upper is None or upper.bit_count() != 6:
        return 0
    bdry = dict(oriented_boundary(upper))
    pivot = bdry[s]
    assert abs(pivot) == 1
    return -sum(c * coefficient(t) for t, c in bdry.items() if t != s) // pivot
morse_boundary = [sum(c * coefficient(t) for t, c in oriented_boundary(s))
                  for s in crit5]
assert morse_boundary == [0] * 5

# Independent mod-two check on original (unmatched) simplicial chains.
# All boundary matrices include the augmentation C_0 -> C_{-1}.
by_size = {k: sorted(s for s in faces if s.bit_count() == k)
           for k in range(11)}
ranks = {}
for k in range(1, 11):
    index = {s: i for i, s in enumerate(by_size[k - 1])}
    pivots = {}
    for s in by_size[k]:
        column = 0
        for t, _ in oriented_boundary(s):
            column ^= 1 << index[t]
        while column:
            pivot = column.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = column
                break
            column ^= pivots[pivot]
    ranks[k] = len(pivots)
    assert ranks[k] <= min(len(by_size[k]), len(by_size[k - 1]))
betti = {k - 1: len(by_size[k]) - ranks.get(k, 0) - ranks.get(k + 1, 0)
         for k in range(1, 11)}
assert {k: n for k, n in betti.items() if n} == {4: 1, 5: 5}
assert ranks[1] == 1

print('VERIFY_OK vertices=20 edges=30 faces=6212'
      f' hasse_arcs={arcs} pairs=3103 critical_4=1 critical_5=5'
      f' integral_morse_boundary={morse_boundary}'
      f' F2_reduced_betti={{4:1,5:5}}')
