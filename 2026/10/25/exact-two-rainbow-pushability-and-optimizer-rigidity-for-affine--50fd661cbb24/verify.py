#!/usr/bin/env python3
"""Exact rational verification of the six-vertex facet kernel and extremizer.

No floating point arithmetic or external packages are used.
"""
from fractions import Fraction

x = (2, 1, -1, -2, -1, 1)
y = (0, 1, 1, 0, -1, -1)

# Pointwise identity on all 36 ordered vertex pairs:
# 6 * 1{same or adjacent} = 3 + x_j*x_k+3*y_j*y_k - (-1)^{j+k}.
for j in range(6):
    for k in range(6):
        A = int((j - k) % 6 in (0, 1, 5))
        assert 6 * A == 3 + x[j] * x[k] + 3*y[j]*y[k] - (-1)**(j+k)

p = tuple(Fraction(1, 3) if j % 2 == 0 else Fraction(0) for j in range(6))
q = tuple(Fraction(1, 3) if j % 2 == 1 else Fraction(0) for j in range(6))
assert sum(p) == sum(q) == 1
assert sum(p[j]*x[j]+q[j]*x[j] for j in range(6)) == 0
assert sum(p[j]*y[j]+q[j]*y[j] for j in range(6)) == 0
F = sum(p[j]*q[k] for j in range(6) for k in range(6)
        if (j-k)%6 in (0,1,5))
assert F == Fraction(2, 3)

# Each parity triple has unique centered probability weights: direct
# determinant of the normalization plus two moment equations.
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
          - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
          + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
for parity in (0, 1):
    js = [j for j in range(6) if j % 2 == parity]
    mat = [[1]*3, [x[j] for j in js], [y[j] for j in js]]
    assert abs(det3(mat)) == 6
    assert sum(x[j] for j in js) == 0
    assert sum(y[j] for j in js) == 0

print('PASS: 36 exact kernel identities, sharp 2/3 example, uniqueness determinants')
