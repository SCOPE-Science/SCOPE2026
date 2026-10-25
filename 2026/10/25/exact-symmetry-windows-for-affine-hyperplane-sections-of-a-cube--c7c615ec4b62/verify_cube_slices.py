#!/usr/bin/env python3
"""Exact finite smoke checks for hyperplane sections of cubes.

Uses rational hyperplane-edge intersections; not a substitute for the all-dimensional proof.
"""
from fractions import Fraction as F
from itertools import product

def vertices(a,t):
    d=len(a)
    out=set()
    for j in range(d):
        for oth in product((0,1),repeat=d-1):
            p=list(oth);p.insert(j,0)
            s=sum(a[k]*p[k] for k in range(d))
            if a[j]:
                r=F(t-s,a[j])
                if 0<=r<=1:
                    p[j]=r;out.add(tuple(map(F,p)))
            elif t==s:
                out.add(tuple(map(F,p)))
                p[j]=1;out.add(tuple(map(F,p)))
    return out

def symmetric(V):
    if not V:return False
    n=len(V); d=len(next(iter(V)))
    c2=[2*sum(v[j] for v in V)/n for j in range(d)]
    return all(tuple(c2[j]-v[j] for j in range(d)) in V for v in V)

def predicted(a,t):
    weights=[abs(x) for x in a if x]
    if not weights:return False
    A=sum(weights)
    if not(0<t<A):return False
    if len(weights)<=2:return True
    m=max(weights)
    return 2*t==A or (A-m<=t<=m)

cases=0
for d in (3,4,5):
 for a in product(range(4), repeat=d):
  if not any(a):continue
  A=sum(a)
  for tw in range(1,2*A):
   t=F(tw,2)
   V=vertices(a,t)
   seen=symmetric(V)
   expect=predicted(a,t)
   if seen!=expect:
    raise AssertionError((d,a,t,seen,expect,V))
   cases+=1
print('CUBE_HYPERPLANE_SYMMETRY_OK',cases,'exact rational sections')
