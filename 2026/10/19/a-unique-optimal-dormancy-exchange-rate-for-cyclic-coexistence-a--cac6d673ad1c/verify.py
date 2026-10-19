#!/usr/bin/env python3
"""Exact bracket and independently reconstructed characteristic-rate checks.

This standalone program verifies finite certificates, not an infinite optimizer theorem.
"""
from fractions import Fraction as Q
import cmath
import math


def f(v):
    return 4*v*(1-v)**4+3*v-2


lo = Q(654193, 1000000)
hi = Q(654194, 1000000)
assert f(lo) < 0 < f(hi)   # exact integer-arithmetic sign checks
assert f(Q(1, 2)) == -Q(3, 8)
assert f(Q(2, 3)) == Q(8, 243)
# f' >= 267/125 by maximizing (1-v)^3(5v-1) on [1/5,1].
assert 3 - 4*Q(27, 125) == Q(267, 125)

left, right = float(lo), float(hi)
for _ in range(90):
    mid = (left+right)/2
    if f(mid) < 0:
        left = mid
    else:
        right = mid
v = (left+right)/2
d = 2*v*(1-v)**2
a = d - 1 + v*(1-v)/d
assert 0.602354 < a < 0.602356
assert 0.156459 < d < 0.156461
assert abs(d*d-v*(2-3*v)) < 2e-14
assert abs(d-(1-v)*(d*d+v*v)) < 2e-14

def slow(a):
    disc = a*(a+2)+2j*(1-a)
    return -(a+1-1j)/2 + cmath.sqrt(disc)/2

l = slow(a)
assert abs(l-(-d+1j*v)) < 1e-12
assert abs(l*l+(a+1-1j)*l-1j) < 1e-12
for aa in [0.05, 0.1, 0.2, 0.4, 0.6, 0.602, 0.7, 1, 2, 4, 10, 100]:
    lam = slow(aa)
    companion = -(aa+1)+1j-lam
    assert lam.real < 0
    assert companion.real < lam.real
    assert abs(lam*lam+(aa+1-1j)*lam-1j) < 1e-12
    if abs(aa-a)>1e-3:
        assert -lam.real < d
# Check the cubic cyclic Fourier spectrum: the nonzero eigenvalue of
# sqrt(3)/3 times the antisymmetric circulant is exactly +/-i.
import cmath
z = cmath.exp(2j*math.pi/3)
cyclic_eigen = (z.conjugate()-z)/math.sqrt(3)
assert abs(abs(cyclic_eigen)-1) < 1e-14
assert abs(cyclic_eigen.real) < 1e-14
print('PASS: exact isolating signs, polynomial identity, eigenvalues, off-optimum checks')
print('v_star=',format(v,'.14f'),'a_star=',format(a,'.14f'),'d_star=',format(d,'.14f'))
