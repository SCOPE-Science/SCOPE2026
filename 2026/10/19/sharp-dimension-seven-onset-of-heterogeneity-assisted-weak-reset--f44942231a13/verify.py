"""Reproduce the sharp dimension-seven weak-resetting calculation.

Run: python verification_brownian_reset.py
Dependencies: Python 3.10+; mpmath is optional for numerical Bessel checks.
The exact arithmetic and sharp threshold checks use only Python's standard library.
"""
from fractions import Fraction as Q
from math import isclose

checks = 0

def witness(d, p, u1):
    a = (1-p)*u1 + p
    b = (1-p)*u1*u1 + p
    return 4*a+d*b-2*(d+2)*a*a

for d in range(2, 81):
    t = Q(4, d+4)
    assert t > 0 and t < 1
    if d <= 6:
        assert d*d - 4*d - 16 < 0
        for j in range(0, 31):
            a = t+(1-t)*Q(j,30)
            upper = (a-t)*(d-2*(d+2)*a)
            assert upper <= 0
            checks += 1
    else:
        pmax = Q(d*d-4*d-16, 2*d*(d+2))
        assert Q(0) < pmax < 1
        p = pmax/2
        assert witness(d, p, t) > 0
        assert witness(d, p, t+Q(1,1000000)) > 0
        checks += 3

assert witness(7, Q(1,50), Q(4,11)) == Q(217,75625)
checks += 1

# A finite difference of the exact Bessel hitting-time transform provides
# an independent check of the radial moment calculation and renewal law.
try:
    import mpmath as mp
except ImportError:
    print('PASS:', checks, 'exact checks. Optional mpmath checks skipped.')
else:
    mp.mp.dps = 65
    for d in (2,3,4,5,6,7,8,10,20):
        t = mp.mpf(4)/(d+4)
        p = mp.mpf(1)/50
        a=(1-p)*t+p
        b=(1-p)*t*t+p
        F=4*a+d*b-2*(d+2)*a*a
        derivative=-F/(8*d*d*(d+2))  # R=D=1
        nu=mp.mpf(d)/2-1
        def phi_one(u, rate):
            x=mp.sqrt(1-u)
            z=mp.sqrt(rate)
            if x == 0:
                return (z/2)**nu/(mp.gamma(nu+1)*mp.besseli(nu,z))
            return x**(-nu)*mp.besseli(nu,x*z)/mp.besseli(nu,z)
        h=mp.mpf('0.0000001')
        phi=(1-p)*phi_one(t,h)+p*phi_one(mp.mpf(1),h)
        mean=(1/phi-1)/h
        baseline=a/(2*d)
        finite=(mean-baseline)/h
        assert abs(finite-derivative) < mp.mpf('2e-9'), (d, finite, derivative)
        checks+=1
    print('PASS:',checks,'checks, including independent Bessel-transform comparisons.')
