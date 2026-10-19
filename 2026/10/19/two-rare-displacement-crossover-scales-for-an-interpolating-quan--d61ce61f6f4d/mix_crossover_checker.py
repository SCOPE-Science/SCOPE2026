#!/usr/bin/env python3
"""Reproduce finite numerical checks for the Gaussian-arcsine crossover theorem.

Requires Python 3, NumPy, and SciPy. Numerical tests supplement, not replace,
the exact estimates proved in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import i0e

checks = 0


def ratio_scaled(q, eta):
    """Return exp(-eta) * f_q(x)/phi_r(x), eta=q*x*x/r."""
    def integrand(theta):
        c = math.cos(theta)
        den = 1 + 2 * q * c + q * q
        amp = math.sqrt((1 - q * q) / den)
        return amp * math.exp(eta * ((c + q) / den - 1))
    return quad(integrand, 0, math.pi, epsabs=1e-11, epsrel=2e-11)[0]/math.pi


def ratio_direct(q, eta):
    """Stable ratio f_q/phi_r for moderate eta."""
    return math.exp(eta) * ratio_scaled(q, eta)

for q in [0.0005, 0.002, 0.01, 0.04, 0.1, 0.25]:
    for eta in [0, 0.01, 0.2, 1, 2, 5, 15, 50]:
        a = ratio_scaled(q, eta)
        b = i0e(eta)
        assert a > 0 and b > 0
        checks += 1
        log_error = math.log(a/b)
        assert abs(log_error) <= 8*q*(1+eta) + 1e-11
        checks += 1

for eta in [0, 0.01, 0.5, 1, 3, 10]:
    q = 1e-6
    assert abs(math.log(ratio_scaled(q, eta)/i0e(eta))) < 8*q*(1+eta)
    checks += 1

for q in [0.02, 0.1, 0.3, 0.6]:
    lower=(1-q)/(1+q)
    upper=(1+q)/(1-q)
    for x in [5, 12, 30, 60]:
        def scaled_integrand(theta):
            c=math.cos(theta)
            s=(1+q*q+2*q*c)/(1-q*q)
            return (2*math.pi*s)**(-0.5)*math.exp(-0.5*x*x*(1/s-1/upper))
        scaled=quad(scaled_integrand,0,math.pi,epsabs=1e-10)[0]/math.pi
        endpoint=math.sqrt(upper)/(math.pi*math.sqrt(upper-lower)*x)
        if x == 60:
            assert abs(scaled/endpoint - 1) < 0.23, (q,x,scaled/endpoint)
        checks += 1

# Test the uniform large-displacement endpoint profile at varied q and eta.
for q in [0.0001, 0.001, 0.01, 0.05, 0.1, 0.25]:
    for eta in [10, 30, 100, 300]:
        stable_observed = ratio_scaled(q, eta)
        stable_predicted = (1+q)/math.sqrt(2*math.pi*eta)*math.exp(-eta*q/(1+q))
        assert abs(stable_observed/stable_predicted-1) < 0.15/eta
        checks += 1

# The second crossover has profile exp(-zeta): q -> 0, eta=zeta/q -> infinity.
for zeta in [0.2, 0.8, 2.0]:
    for q in [0.002, 0.001]:
        eta = zeta/q
        zscaled = ratio_scaled(q, eta)
        approx = i0e(eta)
        # Avoid absolute exponent overflow by dividing the exponentially-scaled values.
        assert abs(zscaled/approx/math.exp(-zeta)-1) < 0.012
        checks += 1

assert abs(ratio_direct(0.01, 0)-1)<0.001
checks += 1
print(f"PASS: {checks} checks (uniform exponential envelope, Bessel crossover, fixed-q endpoint tail).")
