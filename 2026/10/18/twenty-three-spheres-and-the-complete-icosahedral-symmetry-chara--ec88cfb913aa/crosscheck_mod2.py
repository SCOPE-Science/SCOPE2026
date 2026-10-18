#!/usr/bin/env python3
"""Independent combinatorial model and mod-two boundary calculation."""
from collections import defaultdict

# Icosahedron as two pentagonal belts between a north and a south pole.
# Vertices 0/1 are poles, 2..6 upper pentagon, 7..11 lower pentagon.
N = 12
E = set()
def edge(a, b):
    E.add(tuple(sorted((a, b))))
for i in range(5):
    edge(0, 2 + i)
    edge(1, 7 + i)
    edge(2 + i, 2 + (i + 1) % 5)
    edge(7 + i, 7 + (i + 1) % 5)
    edge(2 + i, 7 + i)
    edge(2 + i, 7 + (i - 1) % 5)
assert len(E) == 30
ADJ = [0] * N
for a, b in E:
    ADJ[a] |= 1 << b
    ADJ[b] |= 1 << a
assert all(x.bit_count() == 5 for x in ADJ)

faces = defaultdict(list)
for s in range(1, 1 << N):
    valid = True
    for u in range(N):
        if s & (1 << u) and (s & ADJ[u]).bit_count() > 1:
            valid = False
            break
    if valid:
        faces[s.bit_count() - 1].append(s)
assert [len(faces[d]) for d in range(4)] == [12, 66, 140, 105]

rank = {}
for d in range(1, 4):
    index = {s: k for k, s in enumerate(faces[d - 1])}
    basis = {}
    for s in faces[d]:
        v = 0
        for u in range(N):
            if s & (1 << u):
                v ^= 1 << index[s ^ (1 << u)]
        while v:
            pivot = v.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = v
                break
            v ^= basis[pivot]
    rank[d] = len(basis)
betti = [len(faces[d]) - rank.get(d, 0) - rank.get(d + 1, 0) - (1 if d == 0 else 0)
         for d in range(4)]
assert rank == {1: 11, 2: 55, 3: 85}
assert betti == [0, 0, 0, 20]
print('canonical_double_pentagon_icosahedron', 'vertices', 12, 'edges', len(E))
print('f_vector', [len(faces[d]) for d in range(4)])
print('F2_boundary_ranks', [rank[d] for d in range(1, 4)])
print('reduced_F2_betti', betti)
print('CROSSCHECK_PASS')
