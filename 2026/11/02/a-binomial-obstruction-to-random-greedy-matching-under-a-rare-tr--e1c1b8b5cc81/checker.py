"""Exact and independently enumerated checks for rare-class greedy matchings.
No external dependencies; run: python checker.py
"""
from fractions import Fraction
from itertools import permutations
from functools import lru_cache
from collections import Counter
from math import comb, ceil, sqrt

@lru_cache(maxsize=None)
def dp(a,b,c):
    q=a*b+a*c+b*c
    if q==0:
        return {a+b+c:Fraction(1)}
    out={}
    for aa,bb,cc,weight in ((a-1,b-1,c,a*b),(a-1,b,c-1,a*c),(a,b-1,c-1,b*c)):
        if weight<=0:
            continue
        for r,p in dp(aa,bb,cc).items():
            out[r]=out.get(r,Fraction(0))+Fraction(weight,q)*p
    return out

def enumerate_edge_orders(n,k):
    # Use vertex-level edge permutations, independent of the lumped-state recursion.
    vertices = [('A',i) for i in range(n)]+[('B',i) for i in range(n)]+[('C',i) for i in range(k)]
    edges=[(i,j) for i in range(len(vertices)) for j in range(i+1,len(vertices)) if vertices[i][0]!=vertices[j][0]]
    counts=Counter()
    for perm in permutations(edges):
        used=0; unmatched=len(vertices)
        for i,j in perm:
            if not ((used>>i)&1 or (used>>j)&1):
                used|=(1<<i)|(1<<j); unmatched-=2
        counts[unmatched]+=1
    total=sum(counts.values())
    return {r:Fraction(v,total) for r,v in counts.items()}

def target(k):
    out={}
    for x in range(k+1):
        u=abs(k-2*x)
        out[u]=out.get(u,Fraction(0))+Fraction(comb(k,x),2**k)
    return out

def tv(x,y):
    return sum(abs(x.get(z,0)-y.get(z,0)) for z in x.keys()|y.keys())/2

checks=0
for n,k in [(1,1),(1,2),(1,3),(2,1)]:
    e=enumerate_edge_orders(n,k)
    d=dp(n,n,k)
    assert e==d,(n,k,e,d)
    checks+=1
for n in range(1,13):
    for k in range(1,7):
        d=dp(n,n,k)
        assert sum(d.values())==1
        assert all(0<=r<=k and (r-k)%2==0 for r in d)
        checks+=2
for k in range(1,8):
    t=target(k)
    expectation=sum(r*p for r,p in t.items())
    assert expectation==Fraction(k*comb(k-1,(k-1)//2),2**(k-1))
    checks+=1
for n,k in [(32,2),(48,2),(64,3),(80,4),(100,2)]:
    M=ceil(sqrt(k*n))
    assert M>=4*k
    bound=Fraction(k*M,n)+Fraction(k*k,4*(M-k))
    distance=tv(dp(n,n,k),target(k))
    assert distance<=bound,(n,k,distance,bound)
    checks+=2
print('PASS',checks,'independent enumeration, exact DP, parity, mean, coupling-bound checks')
for n,k in [(16,2),(32,2),(100,2),(100,3),(100,4)]:
    d=dp(n,n,k);t=target(k)
    print('n,k',n,k,'Popt',float(d.get(k%2,0)),'lim',float(t.get(k%2,0)),'TV',float(tv(d,t)))
