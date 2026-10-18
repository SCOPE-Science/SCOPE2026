#!/usr/bin/env python3
"""Reproduce finite mixing identities for a noisy cyclic-bit register.
Only Python standard library. Finite checks are not a proof of asymptotics.
"""
from fractions import Fraction
from itertools import product
from math import comb, exp, log, sqrt, erf, cosh

checks = 0

def assert_eq(a, b):
    global checks
    assert a == b, (a,b)
    checks += 1

def formula(k, a, t):
    m, r = divmod(t, k)
    u, v = a**m, a**(m+1)
    s = Fraction(0)
    for i in range(k-r+1):
        for j in range(r+1):
            L = (1+u)**i * (1-u)**(k-r-i) * (1+v)**j * (1-v)**(r-j)
            s += comb(k-r, i)*comb(r,j)*abs(L-1)
    return s / (2**(k+1))

def direct(k, a, t, initial):
    dist = {initial: Fraction(1)}
    for _ in range(t):
        nxt = {}
        for x, prob in dist.items():
            for new in (-1, 1):
                y = x[1:] + (new,)
                nxt[y] = nxt.get(y, Fraction(0)) + prob*(1+a*x[0]*new)/2
        dist = nxt
    return sum(abs(dist.get(x,Fraction(0))-Fraction(1,2**k))
               for x in product((-1,1),repeat=k))/2

for k in range(1,7):
    for a in (Fraction(0), Fraction(1,4), Fraction(1,2), Fraction(3,4)):
        states = list(product((-1,1), repeat=k))
        starts = [states[0], states[len(states)//2], states[-1]]
        for t in range(0,3*k+2):
            exact = formula(k,a,t)
            for x in starts:
                assert_eq(direct(k,a,t,x), exact)
            if t>0:
                assert_eq(exact <= formula(k,a,t-1), True)
            if t%k==0:
                single=Fraction(0)
                for j in range(k+1):
                    z=a**(t//k)
                    single+=comb(k,j)*abs((1+z)**j*(1-z)**(k-j)-1)
                assert_eq(exact, single/(2**(k+1)))

for a in (0.1,0.5,0.9):
    b=-log(a)
    assert 1 < sqrt(cosh(b)) < exp(b/2)
    for s in (-1.0,0.0,1.0):
        for phase in (0.0,0.2,0.5,0.8,1.0):
            h=exp(b*phase)*sqrt((1-phase)+phase*a*a)
            assert h>=1-1e-12
            assert 0 <= erf(exp(-b*s)*h/(2*sqrt(2))) <= 1
            checks += 2

print('PASS:', checks, 'finite exact-rational or deterministic assertions')
