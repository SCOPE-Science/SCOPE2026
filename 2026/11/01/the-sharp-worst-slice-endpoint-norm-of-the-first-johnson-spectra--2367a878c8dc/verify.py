#!/usr/bin/env python3
"""Exact-rational independent checks of the degree-one Johnson spectral projection.
Scientific source: explicit kernel and finite summation; no external packages.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, floor, sqrt, exp, factorial, pi

checks = 0

def exact(n,k):
    b = k*k//n
    p = Fraction(comb(k,b)*comb(n-k,k-b), comb(n,k))
    return Fraction(2*(n-1)*(k-b)**2,k*(n-k))*p

def direct_hyper(n,k):
    a = Fraction(n*(n-1), k*(n-k))
    mu = Fraction(k*k,n)
    denom=comb(n,k)
    return a*sum((abs(Fraction(j)-mu)*Fraction(comb(k,j)*comb(n-k,k-j),denom)
                 for j in range(max(0,2*k-n), k+1)),Fraction(0))

for n in range(2,101):
    for k in range(1,n):
        lhs=exact(n,k)
        rhs=direct_hyper(n,k)
        assert lhs == rhs,(n,k,lhs,rhs)
        assert exact(n,k)==exact(n,n-k)
        checks +=2

# Exhaustive direct matrix rows; symmetry independent of derivation.
for n in range(2,10):
    for k in range(1,n):
        sets=[set(x) for x in combinations(range(n),k)]
        A=sets[0]
        total=Fraction(0)
        for B in sets:
            overlap=len(A&B)
            row=Fraction(n*(n-1),k*(n-k))*(Fraction(overlap)-Fraction(k*k,n))
            total += abs(row)/len(sets)
        assert total == exact(n,k),(n,k,total,exact(n,k))
        checks +=len(sets)

# The discrete Stein/telescoping identity is tested term by term, all supports.
for n in range(2,101):
    for k in range(1,n):
        prob={j:Fraction(comb(k,j)*comb(n-k,k-j),comb(n,k))
              for j in range(max(0,2*k-n),k+1)}
        for j,p in prob.items():
            lhs=n*(Fraction(j)-Fraction(k*k,n))*p
            rhs=(k-j+1)**2*prob.get(j-1,Fraction(0))-(k-j)**2*p
            assert lhs==rhs,(n,k,j,lhs,rhs)
            checks+=1

# Limiting scalloped envelope: exact local extrema and cusp derivative signs.
for m in range(0,25):
    t=m+0.5
    g=2*sqrt(t)*exp(-t)*t**m/factorial(m)
    for delta in (0.01,0.09):
        l=t-delta; r=t+delta
        assert g>2*sqrt(l)*exp(-l)*l**m/factorial(m)
        assert g>2*sqrt(r)*exp(-r)*r**m/factorial(m)
        checks+=2
    if m:
        cusp=2*sqrt(m)*exp(-m)*m**m/factorial(m)
        left=2*sqrt(m)*exp(-m)*m**(m-1)/factorial(m-1)
        assert abs(cusp-left)<1e-12
        checks+=1

# Regime illustration (not an asymptotic proof).
for n in (10000,40000):
    print('N=',n)
    for k in (3,round(sqrt(n)/sqrt(2)),round(sqrt(n)),round(2*sqrt(n)),round(n**0.65),n//2):
        q=float(exact(n,k))
        t=k*k/n
        F=2*sqrt(t)*exp(-t)*t**floor(t)/factorial(floor(t)) if t<20 else None
        print(' k=',k,'norm=',round(q,7),'norm/sqrt(n)=',round(q/sqrt(n),7),'Poisson scaling=',None if F is None else round(F,7))
print('PASS',checks,'exact-rational or elementary numerical comparisons')
