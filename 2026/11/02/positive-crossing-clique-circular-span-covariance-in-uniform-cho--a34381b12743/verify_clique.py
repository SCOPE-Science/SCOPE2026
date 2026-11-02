"""Exact checks for crossing-clique and circular-span covariance.
Run: python3 verify_clique.py. Standard library only.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import comb, factorial

def choose(a,b):
    return comb(a,b) if 0<=b<=a else 0

def oddprod(n,r):
    v=1
    for j in range(1,r):v*=2*n-2*j-1
    return v

def df(k):
    out=1
    for j in range(1,k+1,2):out*=j
    return out

def formula(n,r):
    mean_t=Q(comb(n,r),df(2*r-1))
    first=Q(choose(n-1,r),df(2*r-1))-mean_t
    expected=Q(0)
    for d in range(1,2*n):
        w=min(d,2*n-d)
        expected+=w*(first+Q(choose(d-1,r-1)*choose(2*n-d-1,r-1),oddprod(n,r)))
    return Q(n,2*n-1)*expected

def all_matchings(v):
    if not v:
        yield ()
    else:
        x=v[0]
        for i in range(1,len(v)):
            y=v[i]
            for others in all_matchings(v[1:i]+v[i+1:]):
                yield ((x,y),)+others

def crosses(a,b):
    x,y=a;u,v=b
    return (x<u<y<v) or (u<x<v<y)

def stats(m):
    n=len(m)
    length=sum(min(y-x,2*n-(y-x)) for x,y in m)
    c=[]
    for r in range(3,n+1):
        c.append(sum(all(crosses(m[i],m[j]) for i,j in combinations(subset,2)) for subset in combinations(range(n),r)))
    return length,c

def exhaustive(n):
    total=0; lh=0; tv=[0]*(n-2); ht=[0]*(n-2)
    for m in all_matchings(tuple(range(2*n))):
        h,cs=stats(m)
        total+=1;lh+=h
        for idx,t in enumerate(cs):
            tv[idx]+=t;ht[idx]+=h*t
    assert total==df(2*n-1)
    assert Q(lh,total)==Q(n**3,2*n-1)
    for ix,r in enumerate(range(3,n+1)):
        assert Q(tv[ix],total)==Q(choose(n,r),df(2*r-1))
        brute=Q(ht[ix],total)-Q(lh*tv[ix],total**2)
        exact=formula(n,r)
        assert brute==exact,(n,r,brute,exact)
        if r==3:
            explicit=Q(n**3*(n-2)*(n-1)**2*(3*n-7),60*(2*n-5)*(2*n-3)*(2*n-1))
            assert brute==explicit,(n,brute,explicit)
        assert exact>0
    print('exhaustive',n,'matchings',total,'passed')

if __name__=='__main__':
    for n in range(3,7): exhaustive(n)
    for n in range(3,65):
        for r in range(3,n+1):
            c=formula(n,r)
            assert c>0
            if r==3:
                rhs=Q(n**3*(n-2)*(n-1)**2*(3*n-7),60*(2*n-5)*(2*n-3)*(2*n-1))
                assert c==rhs,(n,c,rhs)
    print('PASS: exhaustive n=3..6, exact triangle formula n=3..64, positivity r=3..n through n=64')
