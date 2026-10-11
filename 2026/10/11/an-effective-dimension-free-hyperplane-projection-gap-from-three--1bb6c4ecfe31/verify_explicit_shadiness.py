"""Exact checks for the rational inequalities in the analytic proof.

These finite calculations do not verify the cited 3D/4D/5D input theorems
or replace the proof for arbitrary norms and dimensions.
"""
from fractions import Fraction as Q
from math import ceil

D=Q(1,10**6)
assert (1+D)**4<Q(244,125)
assert 2*Q(201,10**6)<Q(1,2000)
assert (Q(2)+Q(1,2000))/40<Q(1,19)
assert 1-Q(3,19)-Q(1,2000)>0

b4=8*7**5
b5=8*8**5
# epsilon = 1/(10^6*b4^2940), a5 = 1/b5^1920
assert b5**1920 < 10**6*b4**2940
assert 100 < 10**6*b4**2940
assert b4**1470 < 10**6*b4**2940

for n in range(6,1000):
    assert any((n-3*a)>=0 and (n-3*a)%4==0 for a in range(n//3+1))
for numerator in (1,2,3,7,11,27,83):
    for denominator in (1,2,3,7,11,137,1000):
        r=Q(numerator,denominator)
        if not (0<r<=1):continue
        d=r*r/10**6
        m=ceil(200/r)
        assert m*d<=Q(201,10**6)*r
        assert Q(2,1)*m*d<r/Q(2000)
        assert (Q(2)+r/2000)*r/Q(40)<r/Q(19)
        assert (Q(1)+r/2000+r/19)/(1-r/19)<1+r
print('EXPLICIT_SHADINESS_RATIONAL_CHECK_OK')
