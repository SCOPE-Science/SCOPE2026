#!/usr/bin/env python3
"""Exact rational checks of singleton/dimer covariance in edge percolation."""
from fractions import Fraction
from itertools import combinations

def evaluate(n,edges,p):
    m=len(edges);q=1-p; ei=di=eidi=Fraction(0)
    for mask in range(1<<m):
        nopen=mask.bit_count();pr=p**nopen*q**(m-nopen)
        deg=[0]*n
        for k,(a,b) in enumerate(edges):
            if mask>>k&1: deg[a]+=1;deg[b]+=1
        iso=sum(v==0 for v in deg)
        dimer=sum(bool(mask>>k&1) and deg[a]==deg[b]==1 for k,(a,b) in enumerate(edges))
        ei+=pr*iso;di+=pr*dimer;eidi+=pr*iso*dimer
    return eidi-ei*di

def predicted(n,edges,p):
    q=1-p;d=2*len(edges)//n
    assert n*d==2*len(edges)
    ed=set(tuple(sorted(e)) for e in edges)
    assert all(sum(i in e for e in edges)==d for i in range(n))
    tr=sum((a,b) in ed and (a,c) in ed and (b,c) in ed for a,b,c in combinations(range(n),3))
    return n*d*p*q**(3*d-3)*(d*p-1)+3*tr*p**3*q**(3*d-4),tr

def cycle(n):return [(i,(i+1)%n) for i in range(n)]
def clique(n):return list(combinations(range(n),2))
def cube(d):return [(x,x^(1<<j)) for x in range(1<<d) for j in range(d) if not(x>>j&1)]
def k33():return [(a,b) for a in range(3) for b in range(3,6)]
def prism():return cycle(3)+[(u+3,v+3) for u,v in cycle(3)]+[(i,i+3) for i in range(3)]
examples=[('K3',3,clique(3)),('C4',4,cycle(4)),('C5',5,cycle(5)),('K4',4,clique(4)),('K5',5,clique(5)),('Q3',8,cube(3)),('K33',6,k33()),('prism',6,prism())]
N=0
for name,n,edges in examples:
 for p in [Fraction(1,4),Fraction(1,2),Fraction(3,4)]:
  actual=evaluate(n,edges,p)
  theory,t=predicted(n,edges,p)
  assert actual==theory,(name,p,actual,theory)
  N+=1
 print(name,'degree',2*len(edges)//n,'edges',len(edges),'triangles',t,'PASS')
print('EXACT_EXHAUSTIVE_PASS',N,'graph-parameter strata')
