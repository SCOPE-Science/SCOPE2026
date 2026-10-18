#!/usr/bin/env python3
"""Reproducible numerical cross-checks for skew-normal/Brownian transport.

Analytical claims follow from the proof and do not rely on these finite checks.
Needs Python 3, NumPy, SciPy.
"""
import math
import numpy as np
from scipy.special import roots_hermitenorm, ndtr
from scipy.stats import norm, skewnorm

m = math.sqrt(2 / math.pi)
checks = 0

def require(test, why):
    global checks
    checks += 1
    if not test:
        raise AssertionError(why)

# Directly compare the original skew-normal density with the Henze representation's moments.
# Gauss-Hermite expectation with stable survival-function inversion at positive tails.
z, w = roots_hermitenorm(75)
w = w / math.sqrt(2 * math.pi)
for a in [-12, -4, -1.5, -0.5, -0.1, 0, 0.1, 0.5, 1.5, 4, 12]:
    q = np.asarray([skewnorm.ppf(norm.cdf(v), a) if v <= 0
                    else skewnorm.isf(norm.sf(v), a) for v in z])
    mean = float(np.dot(w,q))
    second = float(np.dot(w,q*q))
    require(abs(mean-m*a/math.sqrt(1+a*a)) < 1e-7, 'mean')
    require(abs(second-1)<1e-7,'second moment')
    W2 = float(np.dot(w, (q-z)**2))
    H = 2*(1-1/math.sqrt(1+a*a))
    require(W2 <= H+1e-10, 'optimal quadratic transport')
    if a != 0:
        require(W2 < H-1e-7,'strict optimality')
        bound = .5*a*a+m*abs(a)**3/3
        require(abs(math.sqrt(W2)-m*abs(a)) < bound+1e-5,'transport-distance consequence')
        remainder=float(np.sqrt(np.dot(w,(q-z-m*a)**2)))
        require(remainder < bound+1e-7,'L2 quantile displacement bound')

# Exact implicit differentiation identity for the skew-normal quantile.
for a in [-2,-1,-.3,-.02,.02,.3,1,2]:
    for v in [-3,-2,-1,-.3,0,.3,1,2,3]:
        q = float(skewnorm.ppf(norm.cdf(v), a))
        slope = norm.pdf(a*q)/((1+a*a)*norm.cdf(a*q))
        eps=1e-5
        q_plus = float(skewnorm.ppf(norm.cdf(v), a+eps))
        q_minus = float(skewnorm.ppf(norm.cdf(v), a-eps))
        require(abs(slope-(q_plus-q_minus)/(2*eps)) < 2e-6,'quantile ODE')

# The normal inverse Mills slope is globally between -1 and zero.
for t in np.linspace(-7,7,281):
    r=norm.pdf(t)/norm.cdf(t)
    derivative=-r*(t+r)
    require(-1 < derivative < 0, 'inverse Mills derivative')

# Small-skew factor for the published coupling versus quantile coupling.
for a in [.003,.005,.01,.015,.025,.04]:
    q = np.asarray([skewnorm.ppf(norm.cdf(v),a) if v<=0 else
                    skewnorm.isf(norm.sf(v),a) for v in z])
    W2 = float(np.dot(w,(q-z)**2))
    H = 2*(1-1/math.sqrt(1+a*a))
    require(abs(W2/a**2 - 2/math.pi) < a*a, 'optimal coefficient')
    require(abs(H/a**2-1) < a*a,'Henze coefficient')
    require(abs(H/W2-math.pi/2)<0.07,'asymptotic penalty')

# SDE physical parameter: drift b and volatility sigma, step h.
for b,sigma in [(1.0,1.5),(-2.0,0.75),(3.0,4.0)]:
    for h in [1e-5,2e-5,5e-5]:
        a=math.sqrt(math.pi/2)*math.sqrt(h)*b/sigma
        q = np.asarray([skewnorm.ppf(norm.cdf(v),a) if v<=0 else
                        skewnorm.isf(norm.sf(v),a) for v in z])
        W2 = float(np.dot(w,(q-z)**2))
        H = 2*(1-1/math.sqrt(1+a*a))
        require(abs((sigma*sigma*h*W2)/(b*b*h*h)-1)<.002,'optimal local drift unit')
        require(abs((sigma*sigma*h*H)/(b*b*h*h)-math.pi/2)<.002,'Henze local drift unit')

print(f'PASS {checks} deterministic numerical comparisons')
