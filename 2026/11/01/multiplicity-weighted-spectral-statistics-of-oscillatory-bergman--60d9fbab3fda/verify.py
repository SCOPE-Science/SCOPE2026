#!/usr/bin/env python3
"""Finite sanity checks for the mathematical formulas in RESULT.md.

Requires NumPy and SciPy. Finite tests do not establish infinite claims.
"""
import math
import cmath
import numpy as np
from scipy.special import loggamma, gammaln

assertions = 0

def check(condition, label):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(label)

a = math.sqrt(math.pi/math.sinh(math.pi))
a_f = math.exp(-0.5)


def weighted_probabilities(d, M):
    m = np.arange(M+1, dtype=float)
    lw = gammaln(m+d) - gammaln(m+1) - gammaln(d)
    w = np.exp(lw-np.max(lw))
    return w/w.sum()


def wrapped_arc_mass(d, theta, gamma):
    # Cos(theta-v) < -cos(gamma); take all periodic translated intervals.
    mass = 0.0
    for k in range(-7, 15):
        lo = theta - math.pi - gamma + 2*math.pi*k
        hi = theta - math.pi + gamma + 2*math.pi*k
        L = max(0.0, lo)
        H = max(0.0, hi)
        if H > L:
            mass += math.exp(-d*L)-math.exp(-d*H)
    return mass


for d in (1, 2, 3, 6, 12, 20):
    rd = abs(cmath.exp(loggamma(d+1+1j) - gammaln(d+1)))
    # Euler product for r_d = |Gamma(1+i)| product up to d.
    product = a
    for j in range(1, d+1):
        product *= math.hypot(1.0,1.0/j)
    check(abs(rd-product) < 2e-12, ('gamma-product', d))
    c = a*(1+rd)/2
    gamma = math.acos((1+rd)/2)
    lo = math.expm1(2*d*gamma)/math.expm1(2*math.pi*d)
    hi = -math.expm1(-2*d*gamma)/(-math.expm1(-2*math.pi*d))
    check(0<lo<hi<1, ('limits',d))
    # Exact wrapped-exponential arc function sampled at many phases;
    # extrema agree with the closed expressions to grid resolution.
    vals = [wrapped_arc_mass(d,2*math.pi*j/1200,gamma) for j in range(1200)]
    check(abs(min(vals)-lo) < 0.003, ('min arc',d,min(vals),lo))
    check(abs(max(vals)-hi) < 0.003, ('max arc',d,max(vals),hi))
    # Every finite empirical weighted measure is a probability distribution.
    w=weighted_probabilities(d,5000)
    check(abs(float(np.sum(w))-1) < 1e-11, ('normalization',d))

# Fock weighted Weyl moment checks: qualitative finite convergence only.
for d in (1,2,4):
    M=100000
    m=np.arange(M+1, dtype=float)
    w=weighted_probabilities(d,M)
    phase=2*np.sqrt(m+d)
    for k in (1,2,3):
        check(abs(np.dot(w, np.exp(1j*k*phase))) < 0.12,
              ('Fock Fourier coefficient',d,k))

# Bergman exact gamma eigenvalues vs the phase model and its first moment.
for d in (1,2,6):
    M=80000
    m=np.arange(M+1, dtype=float)
    w=weighted_probabilities(d,M)
    z=complex(loggamma(1-1j))
    alpha=cmath.exp(z)
    r=abs(cmath.exp(loggamma(d+1+1j)-gammaln(d+1)))
    c=a*(1+r)/2
    exact=c+np.real(np.exp(z + loggamma(m+d+1) - loggamma(m+d+1-1j)))
    phase=cmath.phase(alpha)+math.log(M)
    theoretical=c+a*(cmath.exp(1j*phase)*d/(d+1j)).real
    check(abs(float(np.dot(w,exact))-theoretical)<0.004,
          ('Bergman first moment', d))

# D=1 canonical disk counterexample differs from the all-d c_d family;
# do not substitute its 1/2 offset in this test.
print('PASS', assertions, 'finite assertions')
