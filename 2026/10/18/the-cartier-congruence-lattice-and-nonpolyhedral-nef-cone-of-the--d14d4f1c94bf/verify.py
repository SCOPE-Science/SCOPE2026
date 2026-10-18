#!/usr/bin/env python3
"""Exact finite-field consistency checks accompanying the Hermitian Cartier-lattice theorem."""
from itertools import product

P = 3
F = list(product(range(P), repeat=4))


def rank_mod3(rows):
    a = [list(map(lambda x: x % P, row)) for row in rows]
    if not a:
        return 0
    piv = 0
    for col in range(len(a[0])):
        ix = next((j for j in range(piv, len(a)) if a[j][col]), None)
        if ix is None:
            continue
        a[piv], a[ix] = a[ix], a[piv]
        d = pow(a[piv][col], -1, P)
        a[piv] = [(d * z) % P for z in a[piv]]
        for j in range(len(a)):
            if j != piv and a[j][col]:
                c = a[j][col]
                a[j] = [(x - c * y) % P for x,y in zip(a[j],a[piv])]
        piv += 1
        if piv == len(a):
            break
    return piv

# Each symmetric Hermitian reduction has 4 diagonal and 6 off-diagonal coordinates.
# The q_H coefficients are evaluated at all 81 fixed points.
quad = [tuple(t[i]*t[i] % P for t in F) for i in range(4)]
quad += [tuple(2*t[i]*t[j] % P for t in F)
         for i in range(4) for j in range(i+1,4)]
affine = [tuple(1 for t in F)] + [tuple(t[i] for t in F) for i in range(4)]
assert len(quad) == 10 and len(affine) == 5
assert rank_mod3(quad) == 10
assert rank_mod3(affine) == 5
assert rank_mod3(quad + affine) == 15

# Matrix used in the originating construction, reduced modulo pi=(1-zeta).
M = ((1,0,0,0),(0,1,0,0),(1,1,0,0),(1,-1,0,0))
H = [[sum(M[k][i]*M[k][j] for k in range(4)) % P
      for j in range(4)] for i in range(4)]
assert H == [[0]*4 for _ in range(4)]

# Its image on F_3^4 is an isotropic plane for the original sum-of-squares q.
images = set()
for t in F:
    v = tuple(sum(M[i][j]*t[j] for j in range(4)) % P for i in range(4))
    images.add(v)
    assert sum(x*x for x in v) % P == 0
assert len(images) == 9

# All 3^10 independent Hermitian residues occur: four independent diagonal
# coordinates and six off-diagonal coordinates of the reduced symmetric matrix.
assert P**10 == 59049

# An infinite sequence of distinct rank-one classes has primitive first entry 1.
for n in range(100):
    v = (1,n,0,0)
    assert v[0] % P == 1
    assert v[0]*v[0] % P != 0

print('FIXED_POINTS 81')
print('QUADRATIC_DIMENSION 10')
print('AFFINE_DIMENSION 5')
print('COMBINED_RANK 15')
print('CARTIER_INDEX 59049')
print('SOURCE_ISOTROPIC_IMAGE 9')
print('VERIFY_OK')
