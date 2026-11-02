#!/usr/bin/env python3
"""Exact-rational supplement to the analytic reuse-count optimization proof.
No external dependencies; finite samples are not the proof of the infinite tail.
"""
from fractions import Fraction as Q
from math import sqrt, log, isclose

assert Q(41) > Q(32,5)**2
assert Q(17) < Q(207,50)**2
assert Q(67,10)**4 > Q(457,100)**5
assert Q(67,10)**2 > 32
u = Q(57,77)
bound = 2*(u + u**3/3)
assert bound == Q(799368,456533)
assert bound > Q(25,16)
# Since sqrt(41)>32/5, this checks the decisive H(5)>0 certificate.
assert Q(10,1)/Q(32,5) == Q(25,16)
def sigma(ell):
    if ell in (1,2):return sqrt(2)
    if ell == 3:return 2.0
    return ((2*ell-3)+sqrt((2*ell-3)**2-8))/2
values = [log(sigma(ell))/ell for ell in range(1,201)]
assert values.index(max(values)) == 4
assert all(values[j]>values[j+1] for j in range(4,len(values)-1))
for m in (1,2,3,5,10,50):
    assert max(range(1,201), key=lambda ell:log(sigma(ell))/(m*ell)) == 5
assert isclose(sigma(4),(5+sqrt(17))/2,rel_tol=0,abs_tol=1e-14)
assert isclose(sigma(5),(7+sqrt(41))/2,rel_tol=0,abs_tol=1e-14)
print('PASS: exact rational inequalities and supplementary finite numerical comparisons')
