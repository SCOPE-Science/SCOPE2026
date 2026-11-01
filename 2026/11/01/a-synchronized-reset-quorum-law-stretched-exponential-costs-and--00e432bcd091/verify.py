#!/usr/bin/env python3
"""Self-contained deterministic supplementary checks for Brownian quorum resetting.
Only Python 3 standard library required. These quadratures are not a proof of limits.
"""
import math

D = 1.0
d = 1.0
c = d / math.sqrt(math.pi * D)
a = d / math.sqrt(4.0 * D)

def integrate_midpoint(f, end=45.0, subdivisions=45000):
    h = end / subdivisions
    return h * sum(f((j + 0.5) * h) for j in range(subdivisions))

def F(t):
    return math.erfc(a / math.sqrt(t))

def q_n(N, r):
    # v=rt: q = integral e^-v F(v/r)^N dv
    def integrand(v):
        x = F(v/r)
        return 0.0 if x == 0 else math.exp(-v + N * math.log(x))
    return integrate_midpoint(integrand)

def psi(lam):
    return integrate_midpoint(lambda y: math.exp(-y - lam/(y*y)))

def psi_alt(lam):
    return integrate_midpoint(lambda v: math.exp(-v - math.sqrt(lam/v)))

def H(lam):
    p = psi(lam)
    return (1.0-p)/(lam*p)

checks = 0

def check(cond, why):
    global checks
    assert cond, why
    checks += 1

# Single-particle first-passage Laplace transform, integrated independently.
for rate in (0.15, 1.0, 4.0):
    check(abs(q_n(1, rate) - math.exp(-d*math.sqrt(rate/D))) < 2e-5,
          'Brownian first-passage transform')

# The Fréchet-law transform has two distinct integral representations.
for lam in (0.2, 1.0, 4.3036838, 10.0):
    check(abs(psi(lam) - psi_alt(lam)) < 2e-5, 'Frechet Laplace integral')

# Distributional N^2 scaling; exact finite-N Laplace transform.
lam = 4.3036838
limit_q = psi(lam)
for N, tolerance in ((10, 0.025), (50, 0.006), (100, 0.004), (300, 0.002)):
    rate = lam/(c*c*N*N)
    Q = q_n(N, rate)
    check(abs(Q - limit_q) < tolerance, 'scaled quorum success probability')
    scaled_mean = (1-Q)/(rate*Q*N*N)
    check(abs(scaled_mean - c*c*H(lam)) < 0.15 if N == 10
          else abs(scaled_mean - c*c*H(lam)) < (0.03 if N == 50 else 0.015),
          'scaled mean completion')

# Fixed-rate stretched exponential, which converges more slowly.
exponent = 3.0*(c*c/4.0)**(1/3)
for N in (30, 60, 100):
    Q = q_n(N, 1.0)
    check(Q > 0.0, 'strict positive success chance')
    check(abs(-math.log(Q)/(N**(2/3)) - exponent) < 0.08,
          'fixed rate stretched exponential')

# Illustrative minimizer is local in a coarse tested grid; no uniqueness asserted.
center = H(lam)
check(center < H(2.0) and center < H(8.0), 'finite clock optimum bracket')
print('PASS:', checks, 'deterministic integration/identity checks')
print('dimensionless limiting minimum trial:', round(center, 9))
print('scaled success probability:', round(limit_q, 9))
