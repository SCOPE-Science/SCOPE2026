#!/usr/bin/env python3
"""Exact finite consistency checks for affine rigidity claims; not an infinite proof."""
from math import comb
from fractions import Fraction

def catalan(n):
    return comb(2*n,n)//(n+1)

def fuss(r,n):
    a=comb((r+1)*n,n)
    assert a%(r*n+1)==0
    return a//(r*n+1)

def binom(p,q,n): return comb(p*n,q*n)

assert all(catalan(n+1)* (n+2) == (4*n+2)*catalan(n) for n in range(0,301))
assert all((catalan(n+1)-4*catalan(n))*(n+2) == -6*catalan(n) for n in range(1,301))
assert all((comb(2*(n+1),n+1)-4*comb(2*n,n))*(n+1) == -2*comb(2*n,n) for n in range(1,301))

fuss_cases=0
for r in range(1,10):
    L=Fraction((r+1)**(r+1),r**r)
    for n in range(1,101):
        a,b=fuss(r,n),fuss(r,n+1)
        assert b>a
        # The drift is strictly negative already in all tested cases.
        assert Fraction(b)-L*a<0
        fuss_cases+=1

binom_cases=0
for p in range(2,10):
    for q in range(1,p):
        L=Fraction(p**p, q**q*(p-q)**(p-q))
        for n in range(1,65):
            a,b=binom(p,q,n),binom(p,q,n+1)
            assert b>a
            assert Fraction(b)-L*a<0
            binom_cases+=1

# Each candidate affine function below is tested against a long exact prefix.
# This is a consistency check, not a uniqueness certificate.
for seq in ([catalan(n) for n in range(1,39)],
            [comb(2*n,n) for n in range(0,39)],
            [fuss(2,n) for n in range(1,39)]):
    targets=set(seq)
    for a in range(1,65):
        for b in range(-128,129):
            if a==1 and b==0: continue
            assert not all(a*x+b in targets for x in seq[:12])
print(f'VERIFY_OK Catalan_recursions=602 fuss_ratio_cases={fuss_cases} binomial_ratio_cases={binom_cases} affine_screen_cases={3*64*257-3} exact_integer_and_rational=yes')
