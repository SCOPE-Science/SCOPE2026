#!/usr/bin/env python3
"""Finite exact-rational diagnostics for an explicit toral coding theorem.
This tests identities on finite grids, not the infinite-time generator property.
"""
from fractions import Fraction as Q
from itertools import product

def tau(s):
    return min(2*s/5, 2*(1-s))

def split(s,t):
    a=(s+t/2)%1
    return int(a < 3*t)

def word(x,y,N):
    ans=[]
    for k in range(N):
        d=int(3*y)
        if d==0:
            ans.append(0 if x<3*y else 1)
        else:
            ans.append(d+1)
        x=(x+y)%1; y=(3*y)%1
    return ans

ct=0
for i in range(1,120):
  s=Q(i,120)
  for j in range(1,100):
    t=Q(j,300)
    if t==tau(s): continue
    assert split(s,t)==int(t>tau(s)),(s,t,split(s,t),tau(s))
    ct+=1
for xnum,ynum,n in product(range(1,19),range(1,19),range(1,15)):
    x=Q(xnum,19);y=Q(ynum,19)
    xk=x;yk=y
    for _ in range(n): xk=(xk+yk)%1;yk=(3*yk)%1
    assert xk==(x+(3**n-1)*y/2)%1,(x,y,n)
    assert yk==(3**n*y)%1
    v=(3**n*y)%2
    assert xk==(x-y/2+v/2)%1
print('EXACT_THRESHOLD_TESTS_PASS',ct)
print('EXACT_SKEW_ORBIT_IDENTITIES_PASS',18*18*14)
print('SYMBOLIC_THRESHOLD_COLLISION', (Q(5,12),Q(11,12)), (tau(Q(5,12)),tau(Q(11,12))))
print('ANALYTIC_DENSITY_AND_ENTROPY_STEPS_NOT_CERTIFIED_BY_FINITE_TESTS')
