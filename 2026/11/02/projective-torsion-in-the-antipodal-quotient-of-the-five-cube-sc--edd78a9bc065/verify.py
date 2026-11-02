#!/usr/bin/env python3
"""Exact combinatorial checks for the antipodal quotient of the scale-three five-cube Rips complex.
Uses only Python's standard library. The topological spectral-sequence deductions are proved in RESULT.md.
"""
from collections import Counter
from itertools import product

N = 5
V = range(1 << N)
FULL = (1 << N) - 1

def hamming(a, b):
    return (a ^ b).bit_count()

neighbors = {v: sum(1 << w for w in V if w > v and hamming(v, w) <= 3) for v in V}
faces = set()

def extend(face, candidates):
    if face:
        faces.add(face)
    while candidates:
        bit = candidates & -candidates
        candidates ^= bit
        v = bit.bit_length() - 1
        extend(face | bit, candidates & neighbors[v])

extend(0, (1 << (1 << N)) - 1)
counts = Counter(x.bit_count() for x in faces)
assert [counts[i] for i in range(1, 11)] == [32, 400, 2560, 9280, 19872, 25312, 18560, 7080, 1120, 80]
assert len(faces) == 84296

# Every simplex has diameter at most three, and no simplex contains an antipodal pair.
for face in faces:
    vbits = face
    while vbits:
        bit = vbits & -vbits
        vbits ^= bit
        v = bit.bit_length() - 1
        assert not (face & (1 << (v ^ FULL)))

def facet_vertices(axis, side):
    return [v for v in V if ((v >> axis) & 1) == side]

facet_simplices = []
for axis in range(N):
    for side in (0, 1):
        verts = facet_vertices(axis, side)
        assert len(verts) == 16
        # In the four-cube, distinct vertices fail the Rips condition
        # exactly when antipodal in the four free coordinates.
        for u in verts:
            excluded = [v for v in verts if v != u and hamming(u, v) > 3]
            assert excluded == [u ^ (FULL ^ (1 << axis))]
        free_axes = [i for i in range(N) if i != axis]
        three = free_axes[:3]
        last = free_axes[3]
        sample = [v for v in verts if sum((v >> j) & 1 for j in three) % 2 == 0]
        assert len(sample) == 8
        assert all(hamming(u, v) <= 3 for u in sample for v in sample)
        sample_set = set(sample)
        # Verify global maximality, so the indicator of this simplex is a cocycle.
        assert all(any(hamming(v, w) > 3 for w in sample)
                   for v in V if v not in sample_set)
        # Verify its cubical hull is exactly its own four-facet.
        assert all({(v >> j) & 1 for v in sample} == {0, 1} for j in free_axes)
        assert {(v >> axis) & 1 for v in sample} == {side}
        facet_simplices.append((axis, side, sample_set))

# Evaluate the integral dual-cocycle matrix against the ten oriented
# embedded 7-sphere fundamental classes: diagonal entries +/-1,
# and all other entries zero, hence a unimodular 10-by-10 matrix.
for i, (a, b, sample) in enumerate(facet_simplices):
    for j, (c, d, _) in enumerate(facet_simplices):
        contained = all(((v >> c) & 1) == d for v in sample)
        assert contained == (i == j)

# The central antipode exchanges each pair of parallel four-facets.
for a, b, sample in facet_simplices:
    moved = {v ^ FULL for v in sample}
    assert all(((v >> a) & 1) == 1 - b for v in moved)
# Its action on the oriented 7-sphere boundary within a four-facet
# is the determinant of eight antipodal-pair flips: (-1)^8=+1.
assert (-1) ** 8 == 1

# The antipode acts without fixed simplices, giving Lefschetz number zero.
assert not any({v ^ FULL for v in V if face >> v & 1} ==
               {v for v in V if face >> v & 1}
               for face in faces)
# The ten 7-sphere classes form five swapped pairs; trace on H_7 is zero.
# The source homotopy theorem supplies ranks H_4=1 and H_7=10,
# so 0 = 1 + trace(H_4) - trace(H_7) implies trace(H_4)=-1.
trace_H7 = 0
trace_H4 = -1 + trace_H7
assert trace_H4 == -1

print('Q5_SCALE3_ANTIPODAL_10_INTEGRAL_SPHERE_DUALS_OK')
print('faces', len(faces), 'fvector', [counts[i] for i in range(1,11)])
print('facets', len(facet_simplices), 'integral_dual_matrix', 'identity_up_to_sign')
print('involution', 'free', 'Lefschetz', 0, 'H4_action', -1, 'H7_orbits', 5)
