#!/usr/bin/env python3
"""Finite arithmetic checks for the natural-seed Z-triangle fixed-row theorem."""
from fractions import Fraction
from math import gcd, comb

def Z(a,b):
    g=gcd(a,b)
    return (a//g)*(b//g)

def mask(m):
    return [j for j in range(m+1) if comb(m,j)%2]

def v(n,p):
    k=0
    while n%p==0:
        k+=1;n//=p
    return k

def evolution(a):
    a=list(a)
    while len(a)>1:
        a=[abs(a[i]-a[i+1]) for i in range(len(a)-1)]
    return a[0]

integer_cases=0
for m in range(11):
    js=mask(m)
    assert len(js)==1<<m.bit_count()
    for n in range(1,181):
        row=list(range(n,n+m+1))
        for _ in range(m):
            row=[Z(row[i],row[i+1]) for i in range(len(row)-1)]
        actual=row[0]
        P=1
        for j in js: P*=n+j
        rat=Fraction(actual,P)
        for p in [2,3,5,7]:
            f=evolution(v(n+j,p) for j in range(m+1))
            expected=sum(v(n+j,p) for j in js)
            # Independent p-adic factorization of both exact integers.
            assert f==v(actual,p)
            assert f-expected == v(rat.numerator,p)-v(rat.denominator,p)
            if p>m: assert f==expected
        if m==2: assert rat==Fraction(1,4) if n%2==0 else rat==1
        if m==3: assert rat==(Fraction(1,36) if n%3==0 else Fraction(1,4))
        integer_cases+=1

synthetic_cases=0
for m in range(2,13):
    for p in [2,3,5,7,11]:
        if p>m: continue
        B=0
        while p**(B+1)<=m: B+=1
        H=2**(m+1)*(B+1)+1
        for j in range(m+1):
            rest=[(i*7+j)% (B+1) for i in range(m+1)]
            a=list(rest); a[j]=H
            b=list(rest); b[j]=H+10**4
            delta=(10000 if j in mask(m) else 0)
            assert evolution(b)-evolution(a)==delta,(m,p,j,evolution(a),evolution(b))
            synthetic_cases+=1
print('VERIFY_OK', 'integer_cases',integer_cases,'synthetic_high_spike',synthetic_cases,'rows',11,'exact_examples_m2_m3',360)
