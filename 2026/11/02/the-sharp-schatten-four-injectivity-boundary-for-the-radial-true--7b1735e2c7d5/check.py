#!/usr/bin/env python3
"""Finite arithmetic checks for the true-order-two Fock Berezin-kernel example.

Only the finite identities below are checked computationally. Infinite
spectral and Schatten conclusions require the proof in RESULT.md.
"""
from fractions import Fraction
from math import comb, factorial, exp, pi, sqrt, cos

def L(n):
    return sum(((-1)**k)*Fraction(comb(n,k), factorial(k)) for k in range(n+1))

checks = 0
vals = [L(n) for n in range(61)]
for n in range(1,60):
    assert (n+1)*vals[n+1] == 2*n*vals[n] - n*vals[n-1]
    checks += 1
for n in range(61):
    # The coefficient of x^n/n! in xF''+(1-2x)F'+xF.
    prev = vals[n-1] if n > 0 else 0
    nxt = vals[n+1] if n+1 < len(vals) else L(n+1)
    assert (n+1)*nxt - 2*n*vals[n] + n*prev == 0
    checks += 1
for x in (0.01, 0.2, 1.0, 3.0, 6.0):
    # Truncated coherent-state expectation of diagonal L_n(1).
    s = x*float(vals[0]); fac = 1.0; power = 1.0
    for n in range(1,61):
        fac *= n
        power *= x
        s += float(vals[n])*power*(x-n)**2/(fac*x)
    assert abs(exp(-x)*s) < 1e-8, (x, s)
    checks += 1

# Plancherel--Rotach is asymptotic, so these are loose numerical stress tests.
for n in (2000, 5000, 10000, 30000, 50000):
    approx = exp(.5)/sqrt(pi)*n**(-.25)*cos(2*sqrt(n)-pi/4)
    # recalculate via recurrence without unstable large-factorial sums
    a,b=1.,0.
    if n==1:
        b=0.
    else:
        for j in range(1,n):
            a,b=b,((2*j)*b-j*a)/(j+1)
    assert abs(b-approx)<.016, (n,b,approx)
    checks+=1

if __name__ == '__main__':
    print('Passed',checks,'finite checks')
    print('Predicted singular counting coefficient:',3*exp(2)/(8*pi*pi))
