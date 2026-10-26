#!/usr/bin/env python3
"""Finite exact-rational diagnostics for periodic real endpoint inequality.

This enumeration checks dimensions 3..11, not a proof for all dimensions.
"""
from fractions import Fraction
from itertools import product
from math import sin, pi, sqrt


def green(n, i, j):
    d = (j-i) % n
    return Fraction(n*n-1,12*n)-Fraction(d*(n-d),2*n)


def predicted(n):
    m=n//2
    t=m*(n-m)
    return Fraction(t*(t+2),3*n)


def one_n(n):
    g=[[green(n,i,j) for j in range(n)] for i in range(n)]
    assert all(sum(row)==0 for row in g)
    assert all(g[i][j]==g[j][i] for i in range(n) for j in range(n))
    for j in range(n):
        assert all(2*g[i][j]-g[(i-1)%n][j]-g[(i+1)%n][j]==(1-Fraction(1,n) if i==j else -Fraction(1,n)) for i in range(n))
    maxq=Fraction(0)
    maxpatterns=[]
    for signs in product((-1,1),repeat=n):
        val=sum(signs[i]*g[i][j]*signs[j] for i in range(n) for j in range(n))
        if val>maxq:
            maxq=val
            maxpatterns=[signs]
        elif val==maxq:
            maxpatterns.append(signs)
    assert maxq==predicted(n),(n,maxq,predicted(n))
    m=n//2
    expected=[]
    for k in (m,n-m):
        for begin in range(n):
            pattern=tuple(1 if (i-begin)%n<k else -1 for i in range(n))
            if pattern not in expected:
                expected.append(pattern)
    assert set(maxpatterns)==set(expected),(n,maxpatterns,expected)
    real=sqrt(float(maxq))
    complex_=(sqrt(n)/(2*sin(pi/n)))
    assert real<=complex_+1e-10
    if n!=4:
        assert real<complex_-1e-6
    print(f'n={n:2d} C_real^2={maxq} maximizing_signs={len(maxpatterns):2d} ratio={real/complex_:.9f}')


if __name__=='__main__':
    for n in range(3,12):
        one_n(n)
    print('All exact finite checks passed (not an infinite theorem proof).')
