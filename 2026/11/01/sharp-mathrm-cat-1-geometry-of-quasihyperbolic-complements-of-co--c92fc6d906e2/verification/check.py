"""Standalone finite checks of the smooth-convex-obstacle curvature identities.

Run: python3 verification/check.py
These tests do not certify global CAT comparison or uniqueness.
"""
from fractions import Fraction as F
from itertools import product

checks = 0
for t, k1, k2 in product([F(1,10),F(1,2),F(1),F(3),F(20),F(1000)],
                          [F(1,10),F(1),F(3),F(19)],
                          [F(1,20),F(2),F(8)]):
    a = t*k1/(1+t*k1)
    b = t*k2/(1+t*k2)
    # All three principal two-planes in a three-dimensional exterior.
    assert -1 < a-1 < 1
    assert -1 < b-1 < 1
    assert -1 < a+b-1 < 1
    checks += 3
    # Geodesic logarithmic-distance concavity tensor in orthonormal velocity basis.
    for v0, v1, v2 in [(3,4,0),(0,3,4),(12,5,0),(1,2,2)]:
        sq = F(v0*v0+v1*v1+v2*v2)
        numerator = -F(v1*v1,sq)/(1+t*k1)-F(v2*v2,sq)/(1+t*k2)
        from_hessian = (a*F(v1*v1,sq)+b*F(v2*v2,sq)) + F(v0*v0,sq)-1
        assert numerator == from_hessian and numerator <= 0
        checks += 1
# Sharpness: for unit ball, tangent curvature = (t-1)/(t+1) in dimension >=3.
for t in [F(1,1000),F(1),F(3),F(1000),F(10**10)]:
    K = 2*t/(1+t)-1
    assert K == (t-1)/(t+1) and K < 1
    checks += 1
assert (F(10**10)-1)/(F(10**10)+1) > F(999999,1000000)
checks += 1
print('PASS:', checks, 'exact-rational curvature and geodesic-Hessian assertions')
