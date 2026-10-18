#!/usr/bin/env python3
"""Independent face enumerator via the forbidden connected triples.
Run: python3 dodecahedron_ind2_crosscheck.py
Only the Python standard library is required.
"""
from collections import Counter
from itertools import combinations
N = 20
SIZE = 1 << N
neighbors = [set() for _ in range(N)]
def edge(u, v):
    neighbors[u].add(v)
    neighbors[v].add(u)
for i in range(10):
    edge(i, (i + 1) % 10)
    edge(i, i + 10)
    edge(i + 10, 10 + ((i + 2) % 10))
assert all(len(s) == 3 for s in neighbors)
forbidden = set()
for c in range(N):
    for a, b in combinations(sorted(neighbors[c]), 2):
        forbidden.add((1 << a) | (1 << b) | (1 << c))
assert len(forbidden) == 60
by_vertex = [[] for _ in range(N)]
for t in forbidden:
    for v in range(N):
        if (t >> v) & 1:
            by_vertex[v].append(t)
face = bytearray(SIZE)
face[0] = 1
counts = Counter()
for mask in range(1, SIZE):
    b = mask & -mask
    v = b.bit_length() - 1
    if face[mask ^ b] and all((mask & t) != t for t in by_vertex[v]):
        face[mask] = 1
        counts[mask.bit_count() - 1] += 1
f = [counts[i] for i in range(12)]
assert f == [20, 190, 1080, 3985, 9772, 15870, 16640,
             10770, 4000, 750, 60, 5]
assert sum(f) == 63142
assert sum((-1)**i * a for i, a in enumerate(f)) == 2
facets = Counter()
for mask in range(1, SIZE):
    if not face[mask]:
        continue
    if not any(face[mask | (1 << v)] for v in range(N) if not (mask >> v) & 1):
        facets[mask.bit_count() - 1] += 1
assert dict(facets) == {7: 25, 8: 60, 9: 420, 11: 5}
print('forbidden_triples:', len(forbidden))
print('simplices:', sum(f), 'Euler_characteristic:', 2)
print('face_vector:', f)
print('facet_dimensions:', dict(sorted(facets.items())))
print('PASS: independent incidence-hypergraph face census')
