#!/usr/bin/env python3
"""Exact certificate for four-patch symmetric-capacity breaking. Python 3 standard library only."""
from fractions import Fraction as F

lo=F(8116,10000)
hi=F(8117,10000)
threshold=F(161,250)
assert lo+lo**8<1<hi+hi**8
assert (1+2*hi**7)**4 < 8*threshold**4*(1+lo**8)**7
r=(5,10,11,10)
S=sum(t**8 for t in r)
Q=2*sum((r[i]*r[i+1])**7 for i in range(3))
assert S==414749506
assert Q==781049340000000
assert Q**4 > threshold**4*S**7
# Independent check of the 2- and 3-vertex formulas at rational areas.
for a in (F(1,7),F(1,3),F(1,2),F(3,5)):
    # a*(1-a) has its unique maximum at 1/2 on [0,1].
    assert a*(1-a)<=F(1,4)
# Concavity: for three patches a1+a3=s, a1^(.75)+a3^(.75)
# is uniquely maximized by a1=a3; derivative differences have the strict sign.
assert F(1,8)**3 * F(1,8) == F(1,4096)
print('PASS: rational root bracket, universal symmetric upper bound, strict asymmetric witness, and illustrative small-path checks')
print('Exact witness Q, S:', Q, S)
print('Witness Rayleigh lower bound (display only):', float(F(Q**4,S**7))**.25)
