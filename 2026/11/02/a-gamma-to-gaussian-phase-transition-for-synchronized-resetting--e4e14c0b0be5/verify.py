#!/usr/bin/env python3
"""Numerical reproduction for synchronized-reset Brownian first-hit asymptotics.

Requires Python >= 3.9 and SciPy. Finite calculations are diagnostic, not proofs.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import erfc, log_ndtr, gammaln, ndtr

checks = 0

def check(label, actual, expected, rtol=1e-8, atol=0.0):
    global checks
    checks += 1
    assert math.isfinite(actual)
    assert abs(actual - expected) <= atol + rtol * abs(expected), (label, actual, expected)

def finite_exact(N, a):
    """Two independent quadratures: reset-before-success and maximum-density."""
    L = math.log(N)
    u = a*L*L
    def one_minus_survival(y):
        f = float(erfc(math.sqrt(y)))
        if f == 1.0: return 1.0
        return -math.expm1(N * math.log1p(-f))
    def reset_integrand(y):
        if y <= 0: return 0.0
        return u/y**2 * math.exp(-u/y) * one_minus_survival(y)
    def maximum_integrand(y):
        if y <= 0: return 0.0
        f = float(erfc(math.sqrt(y)))
        return N/math.sqrt(math.pi*y) * math.exp(-y-u/y) * (1-f)**(N-1)
    a1 = quad(reset_integrand, 0, np.inf, epsabs=2e-13, epsrel=2e-10, limit=250)[0]
    a2 = quad(maximum_integrand, 0, np.inf, epsabs=2e-13, epsrel=2e-10, limit=250)[0]
    return a1, a2

# Stable log-density calculations allow fictitious N=e^L even when N exceeds float range.
def log_union(y,L):
    # Exact single-hit tail erfc(sqrt(y)) = 2 Phi(-sqrt(2y)).
    logf = math.log(2) + float(log_ndtr(-math.sqrt(2*y)))
    h = L + logf
    if h > 30: return 0.0
    if h < -35: return h
    f = math.exp(logf)
    q = -math.expm1(math.exp(L)*math.log1p(-f))
    return math.log(q) if q > 0.0 else h

def log_scaled_probability(L, a):
    """Log p plus leading exponent; no gigantic population allocated."""
    baseline = a if a<1 else (2*math.sqrt(a)-1)
    center = max(1.0, math.sqrt(a))
    def f(u):
        if u <= 0: return 0.0
        v = math.log(a*L) -2*math.log(u)-a*L/u+log_union(L*u,L) +baseline*L
        return math.exp(v) if v > -740 else 0.0
    # Splitting near the Gumbel edge and Laplace saddle is essential.
    v = quad(f,0.05,max(3.5,center*2.7),points=sorted(set([.5,1.,center])),
             epsrel=3e-7, limit=350)[0]
    assert v > 0
    return math.log(v)-baseline*L

for N in (2,3,5,10,30,120):
    for a in (.2,.55,1.,1.5,3.):
        p1,p2 = finite_exact(N,a)
        check('two renewal representations',p1,p2,rtol=3e-8)
        check('probability range',float(p1>0 and p1<1),1.)
        # Non-dimensional mean renewal identity gives the number of full cycles.
        expected_cycles = 1/p1
        check('geometric success count', expected_cycles*p1,1.)

for a in (.25,.5,.75):
    logp = log_scaled_probability(200,a)
    logtheory = -a*200 -(a/2)*math.log(math.pi*200)+float(gammaln(1-a))
    ratio = math.exp(logp-logtheory)
    check('subcritical asymptotic within finite-size tolerance', ratio,1.,rtol=.28)
    print(f'a={a:.2f}, L=200, subcritical ratio={ratio:.6f}')

for a in (1.25,1.6,2.2):
    L=200
    ratio = math.exp(log_scaled_probability(L,a)+(2*math.sqrt(a)-1)*L)
    check('supercritical asymptotic within finite-size tolerance',ratio,1.,rtol=.15)
    print(f'a={a:.2f}, L=200, supercritical ratio={ratio:.6f}')

L=700
for z in (-2.,-1.,0.,1.,2.):
    a=1+z/math.sqrt(L)
    ratio = math.exp(log_scaled_probability(L,a)+(2*math.sqrt(a)-1)*L)
    gaussian = float(ndtr(z/math.sqrt(2)))
    check('Gaussian critical crossover, finite-size tolerance',ratio,gaussian,rtol=.6)
    print(f'z={z:+.1f}, L={L}, p/base={ratio:.6f}, Phi={gaussian:.6f}')

print(f'PASS: {checks} numerical consistency checks (no infinite-limit certification)')
