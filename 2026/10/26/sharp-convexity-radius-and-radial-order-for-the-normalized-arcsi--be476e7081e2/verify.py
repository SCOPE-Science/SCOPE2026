#!/usr/bin/env python3
"""Supplementary numerical and exact-rational checks for the sharp arcsine radius."""
import math
from fractions import Fraction
r = Fraction(11,20)
alo = r + r**3/6
upper_D = 1-Fraction(7,11)*alo
assert upper_D == Fraction(30353,48000)
assert Fraction(21,25)*upper_D**2 < Fraction(7,20)
def beta(x):
    D=1-2/math.pi*math.asin(x)
    return D - (2/math.pi)*x/(math.sqrt(1-x*x)*D)
assert beta(0.5)>0 and beta(0.55)<0
lo,hi=.5,.55
for _ in range(80):
    mid=(lo+hi)/2
    if beta(mid)>0: lo=mid
    else: hi=mid
R=(lo+hi)/2
assert abs(beta(R))<2e-14
assert 0.5385859965<R<0.5385859966
print('Verified rational endpoint comparison and root:',format(R,'.15f'))
