#!/usr/bin/env python3
"""Independent finite checks for the contracted-rotation mode-locking period law.

Uses exact arithmetic for plateau widths and Euler divisor identities;
numerical orbit iteration and limiting-law convergence are corroborative only.
"""
from fractions import Fraction
from math import gcd, floor, exp, cosh, pi, isclose
from itertools import product


def totient(q):
    return sum(gcd(k, q) == 1 for k in range(1, q+1))

# Exact divisor identity yields the finite Lambert-series coefficient identity.
for n in range(1, 1001):
    assert sum(totient(d) for d in range(1, n+1) if n % d == 0) == n

checks = 0
orbit_checks = 0
for slope in (Fraction(1,2), Fraction(2,3)):
    for q in range(2, 13):
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            c = Fraction(1) + sum(
                (floor(Fraction((j+1)*p,q)) - floor(Fraction(j*p,q))) * slope**j
                for j in range(1, q-1)
            )
            left = (1-slope)*c/(1-slope**q)
            right = (1-slope)*(c+slope**(q-1)-slope**q)/(1-slope**q)
            width = (1-slope)**2 * slope**(q-1)/(1-slope**q)
            assert right-left == width
            assert 0 <= left < right <= 1
            checks += 1
            delta = float((left+right)/2)
            lam = float(slope)
            x = 0.3578125
            wraps = []
            for t in range(600):
                y = lam*x + delta
                wraps.append(int(y >= 1.0))
                x = y % 1.0
            assert sum(wraps[-q*10:]) == 10*p, (slope,p,q,wraps[-q*10:])
            orbit_checks += 1

# Exact distribution normalization follows the totient divisor identity.
# With h = -log(lambda), P(Q=q) = 2(cosh(h)-1)*phi(q)/(e^(h*q)-1).
# These limits are diagnostic rather than a proof of weak convergence.
try:
    from scipy.special import zeta
    mean_target = 12 * float(zeta(3,1)) / pi**2
    second_target = 2*pi**2/5
except ImportError:
    import mpmath as mp
    mean_target = 12 * float(mp.zeta(3)) / pi**2
    second_target = 2*pi**2/5
for h in (0.12, 0.06, 0.025, 0.01):
    Qmax = int(32/h)
    # sieve totients rather than arithmetic factoring.
    phis = list(range(Qmax+1))
    for v in range(2,Qmax+1):
        if phis[v] == v:
            for k in range(v,Qmax+1,v):
                phis[k] -= phis[k]//v
    phis[1]=1
    norm=moment1=moment2=0.0
    c=2*(cosh(h)-1)
    for q in range(1,Qmax+1):
        mass=c*phis[q]/(exp(h*q)-1)
        norm += mass
        moment1 += mass*h*q
        moment2 += mass*(h*q)**2
    assert abs(norm-1)<2.e-9, (h,norm)
    assert abs(moment1-mean_target)<0.2, (h,moment1,mean_target)
    assert abs(moment2-second_target)<0.7, (h,moment2,second_target)
    print('h',h,'norm',round(norm,12),'mean',round(moment1,9),'2nd',round(moment2,9))

print('VERIFY_OK',checks,'exact rational tongues;',orbit_checks,'midpoint rotation simulations; 1000 totient-divisor identities; 4 limiting-law mass/moment checks')
