#!/usr/bin/env python3
"""Exact arithmetic checks for finite random dimer parking on a path."""
from fractions import Fraction
from itertools import permutations
from math import factorial

checks = 0

def a(n):
    return sum((Fraction((-1)**k, factorial(k)) for k in range(n)), Fraction())

def b(n):
    if n == 1:
        return Fraction(1)
    if n < 4:
        return Fraction()
    return sum((a(k)*a(n-k-2) for k in range(1,n-2)), Fraction())/(n-1)

def b_closed(n):
    if n == 1:
        return Fraction(1)
    if n < 4:
        return Fraction()
    m=n-4
    return sum((Fraction((-2)**j, factorial(j)) for j in range(m+1)), Fraction()) - Fraction(2*(-2)**m,(n-1)*factorial(m))

assert a(1)==1 and a(2)==0 and b(1)==1 and b(2)==0
checks += 4
for n in range(3,121):
    assert (n-1)*a(n)==sum((a(j) for j in range(1,n-1)),Fraction())
    checks+=1
    assert b(n)==b_closed(n)
    checks+=1
    c=b(n)-a(n)*a(n)
    assert (-1)**n*c>0
    checks+=1

for n in range(1,9):
    sl=sr=both=count=0
    for order in permutations(range(n-1)):
        occupied=[False]*n
        for e in order:
            if not occupied[e] and not occupied[e+1]:
                occupied[e]=occupied[e+1]=True
        L,R=(not occupied[0]),(not occupied[-1])
        sl+=L; sr+=R; both+=(L and R); count+=1
    assert Fraction(sl,count)==a(n)
    assert Fraction(sr,count)==a(n)
    assert Fraction(both,count)==b(n)
    checks+=3

for n in [30,50,70,90,120]:
    c=b(n)-a(n)**2
    ratio=c*factorial(n-1)/Fraction((-1)**n*2**(n-2))
    assert ratio>0
    checks+=1
    if n>=70:
        assert Fraction(3,4)<ratio<Fraction(5,4)
        checks+=1
    print('n=',n,'normalized_asymptotic_ratio=',float(ratio))
print('PASS:',checks,'exact assertion groups')
