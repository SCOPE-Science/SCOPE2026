#!/usr/bin/env python3
"""Finite independently generated check of all equal-positive-digit fixed points."""
from math import isqrt

def E(n,b):
    ds=[]
    while n:
        n,d=divmod(n,b)
        ds.append(d)
    return ds[-1]*sum(d*d for d in ds)

def independent(b):
    out=set()
    for a in range(2,b):
        for digits in [(a,0),(a,a),(a,0,0),(a,0,a),(a,a,0),(a,a,a)]:
            n=0
            for d in digits:n=n*b+d
            if E(n,b)==n:out.add((digits,n))
    return out

def classified(b):
    candidates=[]
    for Ds,r in [((1,0),1),((1,1),2),((1,0,1),2),((1,1,0),2),((1,1,1),3)]:
        # number is a*sum(b^i); requires sum(b^i)=r*a^2
        poly=0
        for d in Ds:poly=poly*b+d
        if poly%r==0:
            a=isqrt(poly//r)
            if 2<=a<b and r*a*a==poly:
                candidates.append((tuple(a*d for d in Ds),a*poly))
    return set(candidates)

for b in range(2,1001):
    x=independent(b);y=classified(b)
    assert x==y,(b,x,y)

# Two independent Pell recurrences; witnesses with b>=2.
x,a=3,1
pell_three=[]
for i in range(8):
    b=(x-1)//2
    if b>=2:
        pell_three.append((b,a))
        assert b*b+b+1==3*a*a
        assert E(a*(b*b+b+1),b)==a*(b*b+b+1)
    x,a=7*x+24*a,2*x+7*a
assert pell_three[:3]==[(22,13),(313,181),(4366,2521)]
print('VERIFIED: classification all equal-positive-digit fixed points, bases 2..1000')
print('three-identical-digit Pell family:',pell_three[:4])
