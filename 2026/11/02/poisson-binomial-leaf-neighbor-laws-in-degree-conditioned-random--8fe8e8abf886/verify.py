#!/usr/bin/env python3
"""Exact checks for a marked vertex in uniformly labelled Cayley trees."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial
from heapq import heapify, heappop, heappush


def conditional_pgf(n,d):
    assert n>=3 and 1<=d<=n-1
    if d==n-1: return [Fraction(0)]*d+[Fraction(1)]
    N=n-1; M=N-d
    p=[0]*d; p[d-1]=1
    for _ in range(M-1):
        # N*f + (1-t)*f'
        p=[(N-i)*p[i]+(i+1)*p[i+1] if i+1<len(p) else (N-i)*p[i] for i in range(len(p))]
    den=N**(M-1)
    assert sum(p)==den
    return [Fraction(c,den) for c in p]


def brute_counts(n):
    counts=defaultdict(lambda:defaultdict(int))
    for code in product(range(n),repeat=n-2):
        deg=[1]*n
        for x in code: deg[x]+=1
        finaldeg=deg[:]
        leaf=[i for i in range(n) if deg[i]==1]
        heapify(leaf)
        neighbors=[]
        for x in code:
            u=heappop(leaf)
            if x==0: neighbors.append(u)
            if u==0: neighbors.append(x)
            deg[u]-=1;deg[x]-=1
            if deg[x]==1: heappush(leaf,x)
        u=heappop(leaf);v=heappop(leaf)
        if u==0: neighbors.append(v)
        if v==0: neighbors.append(u)
        L=sum(finaldeg[x]==1 for x in neighbors)
        counts[finaldeg[0]][L]+=1
    return counts


def falling(x,r):
    q=1
    for j in range(r):q*=x-j
    return q


def check():
    tests=0
    for n in range(3,9):
        independent=brute_counts(n)
        for d in range(1,n):
            P=conditional_pgf(n,d)
            freq=independent[d]
            total=sum(freq.values())
            assert total==comb(n-2,d-1)*(n-1)**(n-d-1)
            for ell in range(max(len(P),max(freq,default=0)+1)):
                assert Fraction(freq[ell],total)==(P[ell] if ell<len(P) else 0),(n,d,ell,freq,P)
                tests+=1
    # Exact factorial moment formula from deletion of marked pendant leaves.
    for n in range(3,51):
        N=n-1
        for d in range(1,n):
            P=conditional_pgf(n,d)
            for r in range(0,d+1):
                moment=sum(comb(l,r)*p for l,p in enumerate(P) if l>=r)
                if r==0: expected=Fraction(1)
                elif d==n-1: expected=Fraction(comb(N,r))
                elif r>=d: expected=Fraction(0)
                else:
                    M=n-d-1
                    expected=Fraction(comb(N,r)*comb(n-r-2,d-r-1)*(n-r-1)**M,
                                      comb(n-2,d-1)*(n-1)**M)
                assert moment==expected,(n,d,r,moment,expected)
                tests+=1
    # Compare the independent two-leaf covariance with real-root / Poisson-binomial variance bound.
    for n in range(4,101):
        for d in range(2,n):
            N=n-1; M=n-d-1
            p1=Fraction(d-1,n-2)*Fraction(n-2,n-1)**M
            if d==n-1: p2=Fraction(1)
            else: p2=Fraction((d-1)*(d-2),(n-2)*(n-3))*Fraction(n-3,n-1)**M
            assert p2<=p1*p1,(n,d,p1,p2)
            if d<=n-2:assert p2<p1*p1,(n,d)
            tests+=1
    # Demonstrate negative-rootedness with exact real-root isolation up to moderate sizes.
    try:
        import sympy as s
        x=s.Symbol('x')
        for n in range(3,17):
            for d in range(1,n):
                P=conditional_pgf(n,d)
                poly=s.Poly(sum(s.Rational(v.numerator,v.denominator)*x**i for i,v in enumerate(P)),x)
                deg=poly.degree()
                nr=sum(factor.count_roots(-s.oo,0)*m for factor,m in poly.sqf_list()[1])
                assert nr==deg,(n,d,deg,nr)
                tests+=1
    except ImportError:
        print('SymPy unavailable: exact Sturm-root checks skipped')
    print('PASS',tests,'exact independent comparisons and symbolic-root checks')
    for n,d in [(5,2),(8,3),(10,5),(12,8)]:
        P=conditional_pgf(n,d)
        print('EXAMPLE',n,d,[(i,str(v)) for i,v in enumerate(P) if v])

if __name__=='__main__': check()
