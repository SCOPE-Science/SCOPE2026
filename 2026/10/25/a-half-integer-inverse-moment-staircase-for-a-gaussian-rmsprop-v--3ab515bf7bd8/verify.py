#!/usr/bin/env python3
"""Deterministic independent quadrature checks for a geometric Gaussian-square sum.

Run with Python 3.10+; standard library only. The mathematical assertions in the
accompanying text rely on analytic arguments, not on this finite test suite.
"""
import math

CHECKS = 0

def check(cond, message):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(message)

def log1pexp(z):
    return max(0.0, z) + math.log1p(math.exp(-abs(z)))

def negative_moment(beta, power, intervals=10000):
    """Numerically integrate the independent Laplace-transform representation."""
    assert 0 < beta < 1 and power > 0 and intervals % 2 == 0
    ell = -math.log(beta)
    start = -45.0
    stop = (2 * power + 4.0) * ell
    h = (stop - start) / intervals
    def f(x):
        z = x + math.log(2.0)
        summation = 0.0
        while z > -36:
            summation += log1pexp(z)
            z -= ell
        return math.exp(power * x - summation / 2.0 - math.lgamma(power))
    terms = [f(start + j * h) * (1 if j in (0, intervals) else (4 if j % 2 else 2)) for j in range(intervals + 1)]
    return (h / 3.0) * math.fsum(terms) / ((1.0-beta)**power)

def noncritical_prediction(beta, power):
    k = int(math.floor(2.0 * power))
    assert power > k/2 and power < (k+1)/2
    exponent = k*power - k*(k+1)/4.0
    logc = -power*math.log(2.0) + math.lgamma(power-k/2.0) + math.lgamma((k+1)/2.0-power) - math.lgamma(.5) - math.lgamma(power)
    return math.exp(logc - exponent*math.log(beta))

def critical_renormalized(beta, k):
    p=k/2.0
    return beta**(k*(k-1)/4.0)*negative_moment(beta,p)

# Gaussian Laplace transforms and the stationary autoregressive identity.
for beta in (0.03, .2, .7):
    for t in (0.1, 1.0, 10.0):
        product = math.prod((1+2*(1-beta)*t*beta**j)**(-.5) for j in range(90))
        tail = math.prod((1+2*(1-beta)*beta*t*beta**j)**(-.5) for j in range(90))
        check(abs(product - tail/(1+2*(1-beta)*t)**.5) < 1e-11,
              'stationary transform functional equation')

# Intermediate asymptotics provide checks distinct from the exact proof.
for power in (.25, .75, 1.25, 1.75):
    old = negative_moment(1e-4,power)
    new = negative_moment(1e-7,power)
    a = old / noncritical_prediction(1e-4,power)
    b = new / noncritical_prediction(1e-7,power)
    check(.60 < a < 1.1, f'first-scale asymptotic, p={power}')
    check(.80 < b < 1.1, f'second-scale asymptotic, p={power}')
    check(abs(b-1) < abs(a-1), f'scale convergence, p={power}')

# Critical logarithmic coefficients can be isolated by subtracting two scales.
for k in (1, 2, 3, 4):
    b1,b2=1e-5,1e-8
    y1=critical_renormalized(b1,k)
    y2=critical_renormalized(b2,k)
    slope=(y2-y1)/(math.log(1/b2)-math.log(1/b1))
    predicted=2**(-k/2.0)/math.gamma(k/2.0)
    check(abs(slope/predicted-1)<.03, f'critical logarithmic slope, k={k}: {slope/predicted}')

print(f'PASS: {CHECKS} deterministic numerical checks; finite tests are not infinite proofs')
