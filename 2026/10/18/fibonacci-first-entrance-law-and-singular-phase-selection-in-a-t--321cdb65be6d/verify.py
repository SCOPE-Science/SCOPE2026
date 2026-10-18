#!/usr/bin/env python3
"""Exact rational checks of first passage polygons in the critical tent-memory map."""
from fractions import Fraction as Q
from math import sqrt

def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def area(poly):
    if len(poly)<3: return Q(0)
    s=sum(poly[i][0]*poly[(i+1)%len(poly)][1] - poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly)))
    return abs(s)/2

def clip(poly,a,b,c,keep_le=True):
    def val(pt):
        return a*pt[0]+b*pt[1]-c
    def inside(v):
        return v<=0 if keep_le else v>=0
    ret=[]
    for i in range(len(poly)):
        p,q=poly[i-1],poly[i]
        u,v=val(p),val(q)
        if inside(u)!=inside(v):
            t=u/(u-v)
            ret.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
        if inside(v):ret.append(q)
    return ret

square=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1))]
for n in range(1,20):
    triangle=clip(square,fib(n),fib(n+1),Q(1))
    expected=Q(1,2*fib(n)*fib(n+1))
    assert area(triangle)==expected,(n,area(triangle),expected)
    first=clip(triangle,fib(n+1),fib(n+2),Q(1),False)
    exact=Q(1,2*fib(n)*fib(n+2))
    assert area(first)==exact,(n,area(first),exact)
    # Independently verify the matrix iterate identity at polygon vertices
    for x,y in first:
        u,v=x,y
        for k in range(n):
            assert u+v<=1 or k==n-1, (n,k,u,v)
            u,v=v,u+v
        assert u+v>=1,(n,u,v)
    if n<=7: print(f'n={n}: survival={expected}, first={exact}')

phi=(1+sqrt(5))/2
print('golden eigenvalue',phi)
print('limiting entrance mean y=',2*(1-phi**-3)/(3*(1-phi**-2)))
print('VERIFY_OK')
