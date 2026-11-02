#!/usr/bin/env python3
"""Independent finite checks for the powered-distance criterion on clique-leaf coronas.
Run: python3 corona_negative_type_checker.py
Uses only Python's standard library; verification is finite evidence, not the universal proof.
"""
from collections import deque
from math import log, isclose

def build_graph(n, t):
    vertices=n*(t+1)
    adj=[set() for _ in range(vertices)]
    def link(i,j):
        adj[i].add(j); adj[j].add(i)
    for i in range(n):
        for j in range(i): link(i,j)
        for r in range(t): link(i,n+i*t+r)
    dist=[]
    for src in range(vertices):
        ds=[-1]*vertices; ds[src]=0
        todo=deque([src])
        while todo:
            a=todo.popleft()
            for b in adj[a]:
                if ds[b]==-1: ds[b]=ds[a]+1;todo.append(b)
        assert -1 not in ds
        dist.append(ds)
    return dist

def quad(dist,vector,p):
    return sum(x*y*(dist[i][j]**p if dist[i][j] else 0.0)
               for i,x in enumerate(vector) for j,y in enumerate(vector))

def F(p): return 1.0+3.0**p-2.0**(p+1)
def H(n,t,p): return (n-1)*F(p)+(1-1/t)*2.0**p-2.0
def standard_determinant(n,t,p):
    a=2.0**p;b=3.0**p
    return t*b-(t-1)*a-t*(a-1)**2

def critical(n,t):
    lo,hi=1.0,2.0
    assert H(n,t,lo)<0<H(n,t,hi)
    for _ in range(75):
        mid=(lo+hi)/2
        if H(n,t,mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

def approx(x,y): return isclose(x,y,rel_tol=3e-12,abs_tol=3e-10)

def run():
    count=0
    for n in range(3,10):
      for t in range(1,6):
        dist=build_graph(n,t)
        N=n*(t+1)
        for i in range(N):
          for j in range(N):
            wanted=(0 if i==j else
                    1 if i<n and j<n else
                    1 if (i<n and j>=n and (j-n)//t==i) or (j<n and i>=n and (i-n)//t==j) else
                    2 if i>=n and j>=n and (i-n)//t==(j-n)//t else
                    2 if i<n or j<n else 3)
            assert dist[i][j]==wanted,(n,t,i,j,dist[i][j],wanted)
            count+=1
        alpha=critical(n,t)
        assert 1<alpha<2 and abs(H(n,t,alpha))<1e-12
        assert standard_determinant(n,t,alpha)>0
        count+=3
        for p in [0,0.5,1,0.5*(1+alpha),alpha,0.5*(alpha+2),2]:
          a,b=2.0**p,3.0**p
          # Global mass: -t at each core and +1 at every pendant.
          global_v=[-float(t)]*n+[1.0]*(n*t)
          lhs=quad(dist,global_v,p)
          rhs=n*t*t*H(n,t,p)
          assert approx(lhs,rhs),(n,t,p,lhs,rhs)
          count+=1
          # Standard mass: difference between hub labels 0,1.
          hub_v=[0.0]*N
          hub_v[0]=1.0; hub_v[1]=-1.0
          leaf_v=[0.0]*N
          for r in range(t):leaf_v[n+r]=1.0;leaf_v[n+t+r]=-1.0
          hub_rhs=-2.0
          leaf_rhs=2.0*t*((t-1)*a-t*b)
          cross_rhs=2*t*(1-a)
          assert approx(quad(dist,hub_v,p),hub_rhs)
          assert approx(quad(dist,leaf_v,p),leaf_rhs)
          assert approx((quad(dist,[x+y for x,y in zip(hub_v,leaf_v)],p)-hub_rhs-leaf_rhs)/2,cross_rhs)
          count+=3
          # Within-leaf-cluster fluctuations have eigenvalue -2**p.
          if t>1:
            pair=[0.0]*N;pair[n]=1;pair[n+1]=-1
            assert approx(quad(dist,pair,p),-2*a)
            count+=1
          if p <= alpha:
            assert standard_determinant(n,t,p)>0
          if p > alpha+1e-8: assert H(n,t,p)>0
          count+=1
    for n in range(3,10):
      for t in range(1,8):
        alpha=critical(n,t)
        assert critical(n+1,t)<alpha and critical(n,t+1)<alpha
        count+=2
    c=3*log(3)-4*log(2)
    for t in (1,2,5):
      for n in (1000,10000):
        delta=critical(n,t)-1
        approximation=2/(t*c*(n-1))
        assert abs(delta/approximation-1)<0.025
        count+=1
    for n in (3,5,11):
      for t in (1000,10000):
        delta=critical(n,t)-1
        approximation=2/(t*((n-1)*c+2*log(2)))
        assert abs(delta/approximation-1)<0.015
        count+=1
    print(f'CHECKS_PASSED {count} ; cases=35 graph families, p=0..2, 49 monotonicity pairs, asymptotic regimes')
    for n,t in [(3,1),(3,2),(4,1),(4,2),(5,2),(10,4)]:
      print(f'n={n},t={t}: critical_p={critical(n,t):.12f}')

if __name__=='__main__': run()
