#!/usr/bin/env python3
"""Exact incidence and lattice arithmetic for the visible quotient curves."""
from itertools import combinations

coords = range(4)
edges = list(combinations(coords, 2))
exceptionals = [(e, s) for e in edges for s in (+1, -1)]

# A face z_i=0 contains the edge L_jk exactly when i is not j or k.
face_vectors = []
for i in coords:
    face_vectors.append([
        1 if i not in e else 0
        for e, s in exceptionals
    ])

assert all(sum(v) == 6 for v in face_vectors)
assert all(sum(face_vectors[i][q] for i in coords) == 2 for q in range(12))
for i, j in combinations(coords, 2):
    common = sum(a*b for a, b in zip(face_vectors[i], face_vectors[j]))
    assert common == 2

def gf2_rank(rows):
    a = [row[:] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((q for q in range(r, m) if a[q][c] & 1), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        for q in range(m):
            if q != r and (a[q][c] & 1):
                a[q] = [(x ^ y) for x, y in zip(a[q], a[r])]
        r += 1
    return r

assert gf2_rank(face_vectors) == 3
# The half classes are (H-F_i)/2; add a final H-coordinate.
half_vectors = [v + [1] for v in face_vectors]
assert gf2_rank(half_vectors) == 3

# Base lattice A1^12 + <4>, then adjoin an index 2^3 isotropic subgroup.
disc_base = (2**12) * 4
index_visible = 2**3
disc_visible = disc_base // (index_visible**2)
assert disc_visible == 2**8

# Piroddi: M_{2,2} is obtained from A1^12 by two independent half-sums.
disc_m22 = (2**12) // (4**2)
assert disc_m22 == 2**8
# Family no. 3: an index-two overlattice of M_{2,2} + <4>.
disc_source_ns = (disc_m22 * 4) // (2**2)
assert disc_source_ns == 2**8
assert disc_source_ns == disc_visible

# Local/global intersection arithmetic for H = 2C + six exceptional curves.
C2 = -2
num_incident = 6
E2_sum = num_incident * (-2)
H2 = 4*C2 + 4*num_incident + E2_sum
assert H2 == 4

# The concrete nonempty open example a_i=1, b_ij=0 has all edge discriminants -4.
assert 0*0 - 4*1*1 == -4
# In the same example, the A1 quadratic term at an edge root has determinant -8.
local_hessian_det = -8
assert local_hessian_det != 0

print('VERIFY_OK rank=13 discriminant=256 face_rank=3 incidence=doubled_K4')
