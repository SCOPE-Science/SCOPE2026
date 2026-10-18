#!/usr/bin/env python3
"""Independent all-subset and mod-2 boundary check for the Heawood complex.

The Fano-plane labels here are the seven distinct triples from Goldberg,
Rajendraprasad and Mathew, rather than the cyclic labels of verify_morse.py.
"""
from collections import Counter

blocks = [tuple(x-1 for x in b) for b in
          [(1,2,3), (1,4,5), (1,6,7), (2,4,6),
           (2,5,7), (3,4,7), (3,5,6)]]
nb = [set() for _ in range(14)]
for j, block in enumerate(blocks):
    for p in block:
        nb[p].add(7+j)
        nb[7+j].add(p)
assert all(len(a) == 3 for a in nb)

# A selected set S is a face precisely if V\S is a dominating set.
face_by_dim = [[] for _ in range(14)]
for s in range(1, 1 << 14):
    comp = set(range(14)) - {i for i in range(14) if s & (1 << i)}
    if all(v in comp or bool(nb[v].intersection(comp)) for v in range(14)):
        face_by_dim[s.bit_count()-1].append(s)
assert [len(xs) for xs in face_by_dim if xs] == [
    14, 91, 364, 987, 1862, 2394, 1962, 931, 224, 21]

# For each signed simplicial boundary, signs disappear modulo two.
# Reduce columns as integers with bit i denoting row i, so no reliance
# on numpy, sympy, an integer Smith routine, or any other package.
ranks = {}
for d in range(1, 10):
    row_number = {v: i for i, v in enumerate(face_by_dim[d-1])}
    pivots = {}
    for simplex in face_by_dim[d]:
        col = 0
        for v in range(14):
            if simplex & (1 << v):
                col ^= 1 << row_number[simplex ^ (1 << v)]
        while col:
            highest = col.bit_length() - 1
            if highest not in pivots:
                pivots[highest] = col
                break
            col ^= pivots[highest]
    ranks[d] = len(pivots)
reduced_betti = {}
for d, faces in enumerate(face_by_dim):
    if faces:
        reduced_betti[d] = len(faces) - ranks.get(d,0) - ranks.get(d+1,0)
reduced_betti[0] -= 1
assert reduced_betti == {0:0,1:0,2:0,3:0,4:0,5:0,6:1,7:0,8:0,9:0}
chi = sum((-1)**d * len(faces) for d, faces in enumerate(face_by_dim))
assert chi == 2
print('independent faces:', sum(map(len, face_by_dim)), 'Euler:', chi)
print('GF2_boundary_ranks:', [ranks[d] for d in range(1,10)])
print('reduced_GF2_Betti:', [reduced_betti[d] for d in range(10)])
print('PASS: separate Fano labels and complement-based enumeration reproduce S6 mod-two homology')
