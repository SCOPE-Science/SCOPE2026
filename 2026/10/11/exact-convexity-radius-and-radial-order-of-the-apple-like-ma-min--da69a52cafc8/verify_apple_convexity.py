#!/usr/bin/env python3
"""Supplementary exact and numerical checks for the apple-like convexity radius.

The analytic proof, rather than this finite verifier, establishes the
universal quantifiers. Standard-library Python 3 only.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext
import cmath
import math
import random


def coefficients(N):
    a = [Q(1), Q(3, 2)]
    for n in range(1, N):
        a.append(((Q(3, 2) - n) * a[n] + a[n-1]) / (n+1))
    return a


def rational_checks():
    a = coefficients(120)
    assert a[2:7] == [Q(7, 8), Q(17, 48), Q(11, 128),
                      Q(107, 3840), -Q(89, 46080)]
    assert all((x > 0 if n % 2 else x < 0)
               for n, x in enumerate(a) if n >= 5)
    edge = Q(17, 50)
    assert Q(3, 2) - Q(7, 2)*edge - Q(11, 8)*edge**3 > 0
    assert 1 - 2*edge/(1-edge**2) > 0
    assert Q(58, 81)*Q(102, 125) - Q(7, 12) == Q(13, 13500)
    assert Q(147149, 250000) - Q(493, 825) == -Q(74083, 8250000)
    assert Q(17, 50)*(1 + 1/(2*(1-Q(17, 50)))) == Q(493, 825)
    print('exact: 120 Taylor coefficients, tail signs, comparison and endpoint certificates PASS')


def decimal_root():
    with localcontext() as ctx:
        ctx.prec = 62
        def h(r):
            return (-r).exp()*(1-r).sqrt() - r*(1+1/(2*(1-r)))
        lo, hi = Decimal(1)/3, Decimal(17)/50
        assert h(lo)>0 and h(hi)<0
        for _ in range(220):
            mid=(lo+hi)/2
            if h(mid)>0:lo=mid
            else:hi=mid
        root=(lo+hi)/2
        assert abs(h(root)) < Decimal('1e-58')
        assert str(root).startswith('0.33387693225135744484210636081305')
        print('root:',root, '|H|:',abs(h(root)))
        return float(root)


def complex_checks(root):
    rand = random.Random(731944)
    count = 0
    for _ in range(5000):
        r = root * rand.random()**.5
        theta = rand.random()*math.tau
        z = r*cmath.exp(1j*theta)
        aa = .99*rand.random() * cmath.exp(1j*math.tau*rand.random())
        lam = cmath.exp(1j*math.tau*rand.random())
        B = lam*(z-aa)/(1-aa.conjugate()*z)
        Bprime = lam*(1-abs(aa)**2)/(1-aa.conjugate()*z)**2
        w=z*B
        zp=z*(B+z*Bprime)
        phi=cmath.exp(w)*cmath.sqrt(1+w)
        P=phi+zp*(1+1/(2*(1+w)))
        H=math.exp(-r)*math.sqrt(1-r)-r*(1+1/(2*(1-r)))
        assert P.real>=H-2e-12,(r,P.real,H)
        count += 1
    print('Schwarz–Blaschke numerical spot checks:',count,'PASS')


def main():
    rational_checks()
    root=decimal_root()
    complex_checks(root)
    print('SUPPLEMENTARY_VERIFIER_PASS; analytic proof required for infinite statement')

if __name__=='__main__':
    main()
