#!/usr/bin/env python3
"""Supplementary finite checks of cyclic Gabor two-site real-amplitude rank formula.
Standard library only; finite floating-point testing is supplementary, not proof.
"""
import math, cmath, itertools, collections

def tot_rank(n,a,z):
    d=math.gcd(n,a); m=n//d
    if abs(z-1)<1e-9: return n
    loss=(n-1 if abs(z+1)<1e-9 else 0)
    if abs(z-(1-n/4))<1e-9: loss+=n-3
    if abs(z+3)<1e-9: loss+=2*(d-1)
    loss+=4*d*sum(abs(z+1+2*math.cos(2*math.pi*k/m))<1e-9 for k in range(1,(m-1)//2+1))
    return n*n-loss

def direct_ambiguity_rank(n,a,z, eps=1e-7):
    roots=[cmath.exp(2j*math.pi*k/n) for k in range(n)]
    g=[z if j==0 or j==a else 1 for j in range(n)]
    zeros=[]
    for t in range(n):
      for b in range(n):
        val=sum(g[(j+t)%n]*g[j]*roots[(-b*j)%n] for j in range(n))
        if abs(val)<eps: zeros.append((t,b))
    return n*n-len(zeros),zeros

checks=0
for n in range(5,26,2):
 for a in range(1,n):
    m=n//math.gcd(n,a)
    zz=[-4,-3,-1,0,1,1-n/4,2,7/3]
    zz += [-1-2*math.cos(2*math.pi*k/m) for k in range(1,(m-1)//2+1)]
    for z in zz:
      expect=tot_rank(n,a,z)
      got,_=direct_ambiguity_rank(n,a,z)
      if got!=expect:
       print('FAIL',n,a,z,expect,got)
       raise SystemExit(1)
      checks+=1
print('PASS',checks,'all-direct-ambiguity complex summation cases, n=5,7,...,25; every spacing and exceptional value')
for n in (5,7,9,15,21):
  for a in (1,3):
   if a>=n:continue
   m=n//math.gcd(n,a)
   for z in (-3,-1,0,1-n/4,-1-2*math.cos(2*math.pi/m)):
    v,zeros=direct_ambiguity_rank(n,a,z)
    print('EXAMPLE',n,a,round(z,9),v,'deficiency',n*n-v)

def projector_span_rank(n,a,z,eps=1e-7):
    """Direct coordinate elimination of the N²-by-N² projector coordinate matrix."""
    roots=[cmath.exp(2j*math.pi*k/n) for k in range(n)]
    g=[z if j==0 or j==a else 1 for j in range(n)]
    cols=[]
    for t in range(n):
        for b in range(n):
            v=[roots[(b*j)%n]*g[(j-t)%n] for j in range(n)]
            cols.append([v[i]*v[j].conjugate() for i in range(n) for j in range(n)])
    # Column Gaussian elimination, all N² rows, first available pivot.
    basis={};rank=0
    for v in cols:
        for pivot,w in sorted(basis.items()):
            if abs(v[pivot])>eps:
                fac=v[pivot]
                for j in range(pivot,n*n):v[j]-=fac*w[j]
        pivot=next((i for i,x in enumerate(v) if abs(x)>eps),None)
        if pivot is None: continue
        div=v[pivot]
        for j in range(pivot,n*n):v[j]/=div
        basis[pivot]=v
        rank+=1
    return rank

count_direct=0
for n in (5,7,9):
    for a in (1,3):
        if a>=n:continue
        m=n//math.gcd(n,a)
        for z in (1,0,-1,-3,1-n/4,2,-1-2*math.cos(2*math.pi/m)):
            got=projector_span_rank(n,a,z)
            want=tot_rank(n,a,z)
            if got!=want: raise AssertionError(('projector',n,a,z,got,want))
            count_direct+=1
print('PASS',count_direct,'direct rank-of-projector-family elimination cases')
