#!/usr/bin/env python3
"""Independently enumerate order-preserving maps satisfying two strong-negation modal axioms on a finite involutive chain."""
from itertools import combinations_with_replacement
from math import comb

def axioms(n,f):
    assert len(f)==n
    assert all(f[i]<=f[i+1] for i in range(n-1))
    def neg(x): return n-1-x
    positive=all(neg(f[max(z,neg(z))])<=f[max(z,neg(z))] for z in range(n))
    consistent=all((lambda y: f[y] <= max(f[x],neg(f[y])))(max(x,min(z,neg(z)))) for x in range(n) for z in range(n))
    return positive and consistent

def predicted_normal(n):
    if n==1: return 1
    r=n//2
    if n%2: return comb(2*r,r)*comb(2*r-1,r-1)+comb(2*r-1,r)
    return comb(2*r-1,r)*comb(2*r-2,r-1)+comb(2*r-1,r)

def predicted(n):
    r=n//2
    if n%2: return comb(2*r,r)**2+comb(2*r,r+1)
    return comb(2*r-1,r)**2+comb(2*r,r+1)

if __name__=='__main__':
    for n in range(1,11):
        count=sum(axioms(n,f) for f in combinations_with_replacement(range(n),n))
        theoretical=predicted(n)
        assert count==theoretical,(n,count,theoretical)
        normal=sum(axioms(n,f) and f[-1]==n-1 for f in combinations_with_replacement(range(n),n))
        assert normal==predicted_normal(n),(n,normal,predicted_normal(n))
        print(f'n={n}: {count} (normal {normal}) / {comb(2*n-1,n)} monotone maps, binomial formulas match')
    print('VERIFY_OK')
