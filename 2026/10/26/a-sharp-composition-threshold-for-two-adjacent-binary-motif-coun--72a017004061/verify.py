#!/usr/bin/env python3
"""Exact checks for finite fixed-composition 001/010 covariance."""
from fractions import Fraction
from itertools import combinations
from math import comb

checks = 0

def assert_equal(x, y):
    global checks
    assert x == y, (x, y)
    checks += 1


def falling(x, k):
    y = 1
    for j in range(k):
        y *= x-j
    return y


def moment(a, b, num_ones, num_zeros):
    n = a+b
    return Fraction(falling(a, num_ones)*falling(b, num_zeros), falling(n, num_ones+num_zeros))


def poly(a, b):
    return (2*a**3*b-2*a**3-a*a*b-2*a*b**3+8*a*b*b-9*a*b+2*a
            +b**3-3*b*b+2*b)


def theoretical(a, b):
    n = a+b
    assert a >= 1 and b >= 2 and n >= 6
    e = (n-2)*moment(a,b,1,2)
    mixed = ((n-4)*(n-5)*moment(a,b,2,4)
             +(n-4)*moment(a,b,2,3)+(n-3)*moment(a,b,1,3))
    factor = Fraction(-a*b*(b-1)*poly(a,b), n*n*(n-3)*(n-2)*(n-1)**2)
    assert_equal(mixed-e*e, factor)
    return e, mixed, factor


def brute(a, b):
    n = a+b
    total = comb(n, a)
    sumu = sumv = sumuv = 0
    for loc in combinations(range(n), a):
        w = ['0']*n
        for pos in loc:
            w[pos] = '1'
        u = v = 0
        for i in range(n-2):
            word = ''.join(w[i:i+3])
            if word == '001':
                u += 1
            if word == '010':
                v += 1
        sumu += u
        sumv += v
        sumuv += u*v
    return Fraction(sumu,total), Fraction(sumv,total), Fraction(sumuv,total)


for n in range(6, 14):
    for a in range(1, n-1):
        b = n-a
        e, mixed, cv = theoretical(a,b)
        eu, ev, euv = brute(a,b)
        assert_equal(eu,e)
        assert_equal(ev,e)
        assert_equal(euv,mixed)
        assert_equal(euv-eu*ev,cv)
        assert_equal(cv > 0, b >= a+2)
        assert_equal(cv < 0, b <= a+1)

for a in range(1, 81):
    for b in range(2, 81):
        if a+b < 6:
            continue
        e, mixed, cv = theoretical(a,b)
        assert_equal(cv>0,b>=a+2)
        assert_equal(cv<0,b<=a+1)
        if b <= a+1:
            v=a-b+1
            expanded=(2*b*(b-1)*(b-2)
                      +(4*b**3-12*b*b+11*b-4)*v
                      +(6*b*b-13*b+6)*v*v
                      +(2*b-2)*v**3)
            assert_equal(poly(a,b),expanded)
            assert_equal(poly(a,b)>0,True)
        else:
            v=b-a-2
            expanded=(-2*a**3+2*a
                      +(-4*a**3-6*a*a+5*a+2)*v
                      +(-6*a*a-a+3)*v*v
                      +(1-2*a)*v**3)
            assert_equal(poly(a,b),expanded)
            assert_equal(poly(a,b)<0,True)

print('PASS exact assertions:', checks)
