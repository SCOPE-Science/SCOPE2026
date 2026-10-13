#!/usr/bin/env python3
"""Exact arithmetic certificates for the minimum-length statement."""
from fractions import Fraction as Q
from math import lcm

P=(3,5,11)
W=(3,5,9,11,15,25,27,33,45,55,75,81,99,125,225,891,1125)

# Enumerate all smooth integers <= 135; loops terminate at a proved
# finite bound used only to certify the first sixteen denominators.
def smooth_upto(bound):
    out=set()
    a=1
    while a<=bound:
        b=a
        while b<=bound:
            c=b
            while c<=bound:
                if c>1:out.add(c)
                c*=11
            b*=5
        a*=3
    return sorted(out)

S=smooth_upto(135)
assert S == [3,5,9,11,15,25,27,33,45,55,75,81,99,121,125,135]
sum14=sum((Q(1,x) for x in S[:14]),Q())
sum15=sum((Q(1,x) for x in S[:15]),Q())
assert sum14 == Q(243508,245025)<1
assert sum15 == Q(1227341,1225125)>1
assert sum15-Q(1,99)+Q(1,135)==Q(1224041,1225125)<1
r=1-sum((Q(1,x) for x in S[:13]),Q())
assert r==Q(322,22275)
assert Q(22275,161)<139
xs=[x for x in S if 99<x<139]
assert xs==[121,125,135]
ys=[1/(r-Q(1,x)) for x in xs]
assert ys == [Q(245025,1517),Q(111375,719),Q(22275,157)]
assert all(y.denominator>1 for y in ys)
assert len(W)==17 and list(W)==sorted(set(W))
for n in W:
    t=n
    for p in P:
        while t%p==0:t//=p
    assert t==1
assert sum((Q(1,x) for x in W),Q())==1
L=lcm(*W)
assert L==111375 and sum(L//x for x in W)==L
print('EXACT_EGYPTIAN_3_5_11_MINIMUM_17_OK')
