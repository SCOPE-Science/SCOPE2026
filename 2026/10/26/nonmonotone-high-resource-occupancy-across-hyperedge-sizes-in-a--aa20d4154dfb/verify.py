"""Exact checks for the frozen-strategy two-state group-transition theorem."""
from fractions import Fraction
from math import comb

def h(k,g):
    return Fraction(k*k, g*g-g*k+k*k)

def finite(n,m,g):
    total=Fraction(0)
    for k in range(g+1):
        if k<=m and 0<=g-k<=n-m:
            total += Fraction(comb(m,k)*comb(n-m,g-k),comb(n,g))*h(k,g)
    return total

def B2(n,m):
    return Fraction(m*(m+2*n-3),3*n*(n-1))

def B3(n,m):
    return Fraction(m*(3*n*n+6*n*m-15*n-2*m*m-6*m+14),7*n*(n-1)*(n-2))

def b2(x):
    return (2*x+x*x)/3

def b3(x):
    return (3*x+6*x*x-2*x*x*x)/7

def hx(x):
    return x*x/(1-x+x*x)

checks=0
for n in range(3,38):
    for m in range(n+1):
        assert finite(n,m,2)==B2(n,m)
        assert finite(n,m,3)==B3(n,m)
        assert B3(n,m)-B2(n,m)==Fraction(-m*(m-n)*(6*m-5*n+4),21*n*(n-1)*(n-2))
        assert finite(n,m,n)==h(m,n)
        checks+=4
for n in range(3,7):
    for m in range(1,n):
        assert not (finite(n,m,3)<finite(n,m,2)<finite(n,m,n))
        checks+=1
assert finite(7,5,2)==Fraction(40,63)
assert finite(7,5,3)==Fraction(31,49)
assert finite(7,5,7)==Fraction(25,39)
assert finite(7,5,3)<finite(7,5,2)<finite(7,5,7)
checks+=4
for j in range(1,400):
    x=Fraction(j,400)
    assert b3(x)-b2(x)==x*(1-x)*(6*x-5)/21
    assert hx(x)-b2(x)==x*(1-x)*(x*x+2*x-2)/(3*(x*x-x+1))
    assert hx(x)-b3(x)==x*(1-x)*(3-x)*(2*x*x-1)/(7*(x*x-x+1))
    checks+=3
print('PASS: exact-rational verifications',checks)
