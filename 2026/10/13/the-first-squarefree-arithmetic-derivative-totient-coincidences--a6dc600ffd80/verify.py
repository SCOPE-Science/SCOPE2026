#!/usr/bin/env python3
"""Exact finite residue verification for an arithmetic-derivative/totient theorem.
The infinite exclusion is proved algebraically in RESULT.md, not by this program.
"""
from fractions import Fraction
from math import isqrt

def prime(n):
    if n<2:return False
    for d in range(2,isqrt(n)+1):
        if n%d==0:return False
    return True

def deriv(n):
    v=n;ans=0
    for p in range(2,isqrt(v)+2):
        if p*p>v:break
        if v%p==0:
            e=0
            while v%p==0:v//=p;e+=1
            ans+=e*(n//p)
    if v>1:ans+=n//v
    return ans

def phi(n):
    v=n;ans=n
    for p in range(2,isqrt(v)+2):
        if p*p>v:break
        if v%p==0:
            while v%p==0:v//=p
            ans=ans//p*(p-1)
    if v>1:ans=ans//v*(v-1)
    return ans

def squarefree(n):
    v=n
    for p in range(2,isqrt(v)+2):
        if p*p>v:break
        if v%p==0:
            v//=p
            if v%p==0:return False
            while v%p==0:v//=p
    return True

candidates={
    (3,7,17):Fraction(549,1),
    (3,7,19):Fraction(123,1),
    (3,7,23):Fraction(747,13),
    (3,7,29):Fraction(189,5),
    (3,7,31):Fraction(1011,29),
    (3,11,13):Fraction(669,25),
    (3,11,17):Fraction(881,49),
}
for (p,q,r),answer in candidates.items():
    t=(1-Fraction(1,p))*(1-Fraction(1,q))*(1-Fraction(1,r))
    s=Fraction(1,p)+Fraction(1,q)+Fraction(1,r)
    assert (1+t)/(t-s)==answer
    assert not(answer.denominator==1 and prime(answer.numerator))
assert deriv(2)==phi(2)==1
assert deriv(15)==phi(15)==8
for n in range(1,20001):
    if squarefree(n) and deriv(n)==phi(n):
        assert n in (2,15),n
print('EXACT_CHECK_OK candidate_triples=7 direct_squarefree_bound=20000 solutions=2,15')
