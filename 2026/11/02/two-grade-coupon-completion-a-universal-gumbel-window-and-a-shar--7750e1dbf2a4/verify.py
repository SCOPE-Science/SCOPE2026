"""Reproducible finite checks for adjacent-quota coupon extremes.

Dependencies: Python 3.10+, scipy, numpy. These tests illustrate the
asymptotic theorem but do not substitute for its analytic proof.
"""
from fractions import Fraction
from math import factorial, log, exp
from scipy.special import gammaincc, gammaln
from scipy.optimize import brentq
from scipy.integrate import quad

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

# Polynomial identity that creates the one-extra-arrival distinction.
for m in range(1, 101):
    for z in (Fraction(1, 3), Fraction(2, 3), Fraction(3, 2), Fraction(5, 4)):
        s = sum((z**j)/factorial(j) for j in range(m))
        t = sum((z**j)/factorial(j) for j in range(m+1))
        check(t-s == z**m/factorial(m), f"Gamma polynomial identity {m} {z}")

def run_row(n, m):
    half = n // 2
    qa = lambda u: gammaincc(m, u)
    qb = lambda u: gammaincc(m + 1, u)
    u = brentq(lambda u: half * (qa(u)+qb(u)) - 1,
               float(m), max(10.0*max(m, log(n)), float(m+10)))
    b = u/(u-m)
    check(abs(half*(qa(u)+qb(u))-1)<3e-8, 'centering equation')
    check(u>m and b>0, 'admissible centering and scale')
    r = qb(u)/qa(u)
    check(1 <= r <= (u/m)*1.25, 'adjacent shape tail ratio')
    def integrand(x):
        t=u+b*x
        if t<=0: return 0.0
        a,c=qa(t),qb(t)
        if a>=1 or c>=1:return 0.0
        density=exp(-t + m*log(t)-gammaln(m+1))
        return half*b*density*exp(half*log1p(-a)+(half-1)*log1p(-c))
    # integral for the density of the plus-class maximum times minus-class CDF
    from math import log1p
    p,err=quad(integrand, -28, 28, epsabs=1e-10, limit=300)
    predicted=r/(1+r)
    check(err<2e-6,'quadrature error')
    check(0<=p<=1,'valid winner probability')
    check(abs(p-predicted)<0.015,'finite-n check against intensity split')
    for x in (-1.,0.,1.):
        t=u+b*x
        actual=(1-qa(t))**half*(1-qb(t))**half
        limit=exp(-exp(-x))
        check(abs(actual-limit)<0.065,'Gumbel approximation')
    print(f"n={n}, m={m}, center={u:.6g}, scale={b:.6g}, "
          f"winner_probability={p:.8f}, local_prediction={predicted:.8f}")

for n,m in [(1000,3),(10000,4),(100000,11),
            (1000,100),(10000,1000),(1000,10000)]:
    run_row(n,m)
print('finite assertions passed:',checks)
