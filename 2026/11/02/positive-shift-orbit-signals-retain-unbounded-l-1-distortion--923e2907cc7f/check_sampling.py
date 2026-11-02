#!/usr/bin/env python3
"""Finite supplementary check of the positive sampling normalization in one dimension."""
import numpy as np
from fractions import Fraction
assert Fraction(2,5)==Fraction(32,15)/Fraction(16,3)
a=1/16
v=np.arange(-10000,10001,dtype=float)
sums=[]
for x in (0.0,0.15,0.41,0.97):
    f=2*a*np.sinc(2*a*(v-x))
    g=f*f
    assert np.all(g>=0)
    sums.append(float(np.dot(g,g)))
assert max(sums)-min(sums)<1e-11
print('four positive sampling norms:',sums)
print('triangular-square coordinate variance:',Fraction(2,5))
print('SUPPLEMENTARY FINITE CHECK PASSED (not an infinite proof)')
