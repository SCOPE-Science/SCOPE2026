#!/usr/bin/env python3
"""Exact integer verification of sixth Fourier moments for coordinate-pair spectra.

No external packages are required. Fourier convolution coefficients are Gaussian
integer pairs (real part, imaginary part), so all assertions are exact.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from random import Random


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])


def abs2(a):
    return a[0]*a[0] + a[1]*a[1]


def six_moment(a, b, modulus=None):
    n = len(a)
    zero = (0,)*n
    terms = []
    for i in range(n):
        u = [0]*n
        u[i] = 1
        terms.append((tuple(u), a[i]))
        u[i] = -1
        terms.append((tuple(u), b[i]))
    d = {zero:(1, 0)}
    for _ in range(3):
        next_d = {}
        for u, c in d.items():
            for v, cv in terms:
                k = tuple((x+y)%modulus if modulus else x+y for x,y in zip(u,v))
                next_d[k] = add(next_d.get(k,(0,0)), mul(c,cv))
        d = next_d
    return sum(abs2(c) for c in d.values())


def formula(a,b):
    n = len(a)
    s = [abs2(a[i])+abs2(b[i]) for i in range(n)]
    q = [mul(a[i],b[i]) for i in range(n)]
    S = sum(s)
    Q = (sum(z[0] for z in q), sum(z[1] for z in q))
    return (6*S**3 - 9*S*sum(v*v for v in s) + 4*sum(v**3 for v in s)
      + 15*sum(s[i]*abs2(q[i]) for i in range(n))
      - 18*S*sum(abs2(v) for v in q)
      + 9*sum(s[i]*abs2((2*Q[0]-q[i][0],2*Q[1]-q[i][1])) for i in range(n)))


def exact_deficit(a,b):
    n=len(a)
    s=[abs2(a[i])+abs2(b[i]) for i in range(n)]
    q=[mul(a[i],b[i]) for i in range(n)]
    S=sum(s)
    def real_conj(z,w): return z[0]*w[0]+z[1]*w[1]
    mass=sum((Fraction(v)-Fraction(S,n))**2 *
             (Fraction(45*S,2)-10*v-Fraction(20*S,n)) for v in s)
    imbalance=sum(Fraction(18*S-12*s[i],4) *
                  (abs2(a[i])-abs2(b[i]))**2 for i in range(n))
    phase_and_imbalance=sum(36*(2*S-s[i]-s[j]) *
             (Fraction(s[i]*s[j],4)-real_conj(q[i],q[j]))
             for i in range(n) for j in range(i+1,n))
    assert mass >= 0 and imbalance >= 0 and phase_and_imbalance >= 0
    return mass+imbalance+phase_and_imbalance


def sharp(n):
    return Fraction(15,1)-Fraction(45,2*n)+Fraction(10,n*n)


def verify():
    rng = Random(20261018)
    checks = 0
    for n in range(1,7):
        for _ in range(150):
            a = [(rng.randrange(-3,4),rng.randrange(-3,4)) for i in range(n)]
            b = [(rng.randrange(-3,4),rng.randrange(-3,4)) for i in range(n)]
            if all(z==(0,0) for z in a+b):
                continue
            F = six_moment(a,b)
            assert F == formula(a,b), (n,'sixth-moment identity')
            S = sum(abs2(z) for z in a+b)
            assert Fraction(F,S**3) <= sharp(n), (n,'sharp bound')
            assert sharp(n)*S**3-F == exact_deficit(a,b), (n,'exact deficit')
            checks += 3
    for n in range(1,7):
        a = b = [(1,0)]*n
        F = six_moment(a,b)
        S = 2*n
        assert Fraction(F,S**3) == sharp(n)
        checks += 1
        assert six_moment(a,b,7)==F
        checks += 1
        assert Fraction(six_moment(a,b,6),S**3)==sharp(n)+Fraction(1,4*n*n)
        checks += 1
    for n in range(1,5):
        for _ in range(50):
            a=[(rng.randrange(-2,3),rng.randrange(-2,3)) for i in range(n)]
            b=[(rng.randrange(-2,3),rng.randrange(-2,3)) for i in range(n)]
            assert six_moment(a,b,7)==six_moment(a,b)
            checks += 1
    # Phase sensitivity: equal magnitudes but misaligned opposite-pair products
    for n in range(2,7):
        a=[(1,0)]*n
        b=[(1,0)]*n
        b[0]=(0,1)
        assert Fraction(six_moment(a,b),(2*n)**3)<sharp(n)
        checks += 1
    print('EXACT_TESTS_PASSED', checks)
    for n in range(1,7):
        print('n=',n,'sharp_L6_sixth_power=',str(sharp(n)),
              'sixth_order_alias_at_mod6=',str(Fraction(1,4*n*n)))


if __name__ == '__main__':
    verify()
