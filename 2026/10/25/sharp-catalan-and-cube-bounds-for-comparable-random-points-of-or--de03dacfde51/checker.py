#!/usr/bin/env python3
"""Finite exact checks of coordinatewise comparability for order polytopes."""
from fractions import Fraction
from math import factorial, comb
from functools import lru_cache
from itertools import combinations

def extensions(n, relations):
    pre=[0]*n
    for i,j in relations:
        assert 0<=i<n and 0<=j<n and i!=j
        pre[j] |=1<<i
    @lru_cache(None)
    def f(mask):
        if mask == (1<<n)-1: return 1
        return sum(f(mask | (1<<i)) for i in range(n) if not(mask>>i &1) and (pre[i]&mask)==pre[i])
    return f(0)

def comparison(n,rels):
    e=extensions(n,rels)
    qrels=rels+[(a+n,b+n) for (a,b) in rels]+[(k,k+n) for k in range(n)]
    e2=extensions(2*n,qrels)
    return Fraction(e2,comb(2*n,n)*e*e)

counts=0
for n in range(1,6):
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        rels=[r for i,r in enumerate(pairs) if mask>>i&1]
        p=comparison(n,rels)
        assert Fraction(1,2**n)<=p<=Fraction(1,n+1),(n,rels,p)
        if not rels: assert p==Fraction(1,2**n)
        else: assert p>Fraction(1,2**n)
        if extensions(n,rels)==1: assert p==Fraction(1,n+1)
        elif n>1: assert p<Fraction(1,n+1), (n,rels,p)
        counts+=1

for k in range(1,8):
    n=k+1
    rels=[(i,k) for i in range(k)]
    actual=comparison(n,rels)
    predicted=Fraction((k+1)*2**(k-1)*factorial(k)**2,factorial(2*k+1))
    assert actual==predicted,(k,actual,predicted)
    print('star',k,str(actual))
print('VERIFY_OK poset_instances=',counts,'star_formula_cases=',7)
