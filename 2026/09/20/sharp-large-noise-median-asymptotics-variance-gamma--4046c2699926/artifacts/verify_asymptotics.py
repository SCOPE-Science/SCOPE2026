"""Numerical checks for large-noise variance-gamma median asymptotics.

Requires Python 3 and SciPy.  The normalized family has theta=1 and
kappa=sigma**2.  The median is obtained from the exact beta slice at zero
and direct integration of the variance-gamma Bessel density on (0,m).
"""
import math
import sys
import scipy
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import betainc, gamma, kv


def median_normalized(r, kappa):
    s = r / 2.0
    a = math.sqrt(1.0 + kappa)
    # F(0)=I_{1/2-1/(2a)}(s,s), so the positive mass needed to reach 1/2 is H.
    H = 0.5 - betainc(s, s, 0.5 - 0.5 / a)
    nu = (r - 1.0) / 2.0
    pref = 1.0 / (math.sqrt(kappa) * math.sqrt(math.pi) * gamma(s))

    def density(x):
        if x == 0.0:
            x = 1e-300
        z = x * a / kappa
        return pref * math.exp(x / kappa) * (x / (2.0 * a)) ** nu * kv(abs(nu), z)

    def residual(m):
        val = quad(density, 0.0, m, epsabs=2e-13, epsrel=2e-11, limit=300)[0]
        return val - H

    hi = max(2.0, r + 2.0)
    while residual(hi) < 0.0:
        hi *= 2.0
    return brentq(residual, 0.0, hi, xtol=2e-13, rtol=2e-13)


def predicted(r, kappa):
    if r < 1.0:
        C = (r * (2.0 ** r) * gamma((r + 1.0) / 2.0) / gamma((1.0 - r) / 2.0)) ** (1.0 / r)
        return C * kappa ** (-(1.0 - r) / (2.0 * r))
    if r == 1.0:
        den = 0.5 * math.log(kappa) + math.log(math.log(kappa)) + 1.0 - 0.5772156649015329
        return 1.0 / den
    if r < 3.0:
        nu = (r - 1.0) / 2.0
        A = 2.0 * (nu ** (2.0 * nu)) * gamma(1.0 - nu) / ((2.0 * nu + 1.0) * gamma(nu))
        return (r - 1.0) + A * kappa ** (-nu)
    if r == 3.0:
        return 2.0 + (2.0 / 3.0) * math.log(kappa) / kappa
    return (r - 1.0) + (2.0 * (r - 1.0) / (3.0 * (r - 3.0))) / kappa


def ratio(r, kappa):
    m = median_normalized(r, kappa)
    p = predicted(r, kappa)
    if r < 1.0 or r == 1.0:
        return m / p
    base = r - 1.0
    return (m - base) / (p - base)


print(f"Python {sys.version.split()[0]}; SciPy {scipy.__version__}")
print("Numerical check")
print("r      kappa        median             asymptotic          ratio")
for r, kappa in [
    (0.5, 1e6),
    (1.0, 1e8),
    (1.5, 1e8),
    (2.0, 1e8),
    (2.5, 1e8),
    (3.0, 1e8),
    (4.0, 1e8),
    (6.0, 1e6),
]:
    m = median_normalized(r, kappa)
    p = predicted(r, kappa)
    print(f"{r:3.1f}  {kappa:10.1e}  {m: .12e}  {p: .12e}  {ratio(r,kappa): .9f}")

# Exact r=2 consistency check: m=(1+a) log(1+1/a), a=sqrt(1+kappa).
kappa = 1e5
a = math.sqrt(1.0 + kappa)
m_num = median_normalized(2.0, kappa)
m_exact = (1.0 + a) * math.log1p(1.0 / a)
print("r=2 exact consistency absolute error:", f"{abs(m_num-m_exact):.3e}")
