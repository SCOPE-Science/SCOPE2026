#!/usr/bin/env python3
from math import gcd
import heapq

def in_H(x,n,p):
    if x < 0: return False
    for a in range(x//n + 1):
        if (x-a*n) % p == 0:
            return True
    return False

def lam_bruteforce(d,n,p):
    h=0
    while True:
        if in_H(h,n,p) and in_H(h-d,n,p):
            return h
        h += 1

def lam_explicit(d,n,p):
    if in_H(d,n,p): return d
    if n==1 or p==1: return d
    a=next(a for a in range(1,p) if (a*n-d)%p==0)
    b=next(b for b in range(1,n) if (b*p-d)%n==0)
    return min(a*n,b*p)

def frobenius(gens):
    gens=sorted(set(gens))
    if gcd(*gens)!=1: raise AssertionError(('not numerical',gens))
    a=gens[0]
    inf=10**100
    dist=[inf]*a; dist[0]=0
    pq=[(0,0)]
    while pq:
        d,r=heapq.heappop(pq)
        if d!=dist[r]: continue
        for g in gens[1:]:
            nd=d+g; nr=nd%a
            if nd<dist[nr]:
                dist[nr]=nd; heapq.heappush(pq,(nd,nr))
    return max(dist)-a

lam_checks=0
for n in range(1,11):
  for p in range(1,11):
    if gcd(n,p)!=1: continue
    Q=n*n+p*p
    for d in range(1,Q+1):
      x=lam_bruteforce(d,n,p); y=lam_explicit(d,n,p)
      assert x==y,(n,p,d,x,y)
      lam_checks += 1

cases=0
min_excess=None
max_case=None
for n in range(1,9):
  for p in range(n,10):
    if gcd(n,p)!=1: continue
    Q=n*n+p*p
    for m in range(Q+1,2*Q):
      if gcd(m,Q)!=1 or (m+n+p)%2 != 1: continue
      B=m*m-Q
      d=m-Q
      lam=lam_explicit(d,n,p)
      gH=n*p-n-p
      G0=m*B+2*m*gH
      E=B-2*m*lam
      assert E>0,(n,p,m,E)
      pred=G0+E
      actual=frobenius([2*m*n,2*m*p,B,m*m+Q])
      assert actual==pred,(n,p,m,actual,pred,G0,lam)
      cases += 1
      if min_excess is None or E<min_excess:
          min_excess=E; max_case=(n,p,m,Q,lam,actual,G0,E)
print(f'VERIFY_OK lambda_checks={lam_checks} subthreshold_cases={cases} exact_frobenius=all excess_positive=all min_excess={min_excess} witness={max_case}')
