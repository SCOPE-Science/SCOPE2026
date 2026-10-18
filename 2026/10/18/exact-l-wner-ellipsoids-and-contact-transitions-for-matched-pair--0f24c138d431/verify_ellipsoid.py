#!/usr/bin/env python3
"""Exact rational grid verification of matched-pair Lipschitz enclosing ellipsoids.

Run with Python 3 (standard library). For each rational t=p/q, a vertex
has all differences in (1/q)Z, by connected tight-edge incidence;
therefore every polytope vertex appears in the enumerated min-zero grid.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

def weights(n,t):
    if n==4:
        return 1/(1+(t-1)**2),F(1)
    if n==6 and t>F(5,3):
        return (3-t)/2,(1+t)/4
    return F(4,n),F(4,n)

def expected_contacts(n,t):
    if n==4:
        return 6 if t==1 or t==2 else 10
    if n==6:
        if t<F(5,3):return 20
        if t==F(5,3):return 56
        return 24
    return comb(n,n//2)+(n if n==8 and t==2 else 0)

def verify(n,p,q):
    t=F(p,q)
    a,b=weights(n,t)
    count=0
    feasible=0
    maxscore=F(0)
    for seq in product(range(p+1),repeat=n):
        if 0 not in seq:continue
        if any(abs(seq[i]-seq[j])>q for i in range(n) for j in range(i+1,n) if i//2!=j//2):
            continue
        feasible+=1
        U=F(sum((seq[2*j]-seq[2*j+1])**2 for j in range(n//2)),2*q*q)
        S=sum(seq)
        total=F(n*sum(z*z for z in seq)-S*S,n*q*q)
        V=total-U
        score=a*U+b*V
        assert score<=1,(n,t,seq,score)
        if score==1:count+=1
        maxscore=max(score,maxscore)
    assert maxscore==1,(n,t,maxscore)
    assert count==expected_contacts(n,t),(n,t,count,expected_contacts(n,t))
    print(f'n={n} t={t}: a={a}, b={b}, contacts={count}, feasible_grid={feasible}: PASS')

CASES=[(4,1,1),(4,3,2),(4,2,1),(6,1,1),(6,3,2),(6,5,3),(6,7,4),(6,2,1),
       (8,1,1),(8,3,2),(8,2,1),(10,1,1),(10,2,1)]
for args in CASES:verify(*args)
print(f'EXACT_ELLIPSOID_PASS: {len(CASES)}')
