"""Numerical checks for large-shape super-Gaussian Fourier-zero asymptotics.

This code is supplementary: it does not certify infinitely many zeros or uniform bounds.
"""
import math
import mpmath as mp
from scipy.integrate import quad
from scipy.optimize import brentq

mp.mp.dps = 50


def integral_transform(p, x):
    # With p >= 40, integrating over [0, 1.5] leaves a tail far below test tolerance.
    value, _ = quad(lambda t: math.exp(-t**p) * math.cos(x*t),
                    0.0, 1.5, epsabs=1e-12, epsrel=1e-12, limit=2400)
    return 2*value


def gamma_phase(s):
    return float(mp.im(mp.loggamma(1 + 1j*s)))


def phase_derivative(s):
    return float(mp.re(mp.digamma(1 + 1j*s)))


def ratio_real(s):
    z = 1 + 1j*s
    return float(mp.re(mp.polygamma(1, z) + mp.digamma(z)**2))


print("Super-Gaussian Fourier integral / gamma-phase root checks")
for p in (40, 80, 160):
    inds = sorted(set([1, 2, round(0.6*p/math.pi),
                       round(1.8*p/math.pi), round(2.7*p/math.pi)]))
    for k in inds:
        s = k*math.pi/p
        leading = k*math.pi - gamma_phase(s)
        delta = (gamma_phase(s)*phase_derivative(s)
                 - s*ratio_real(s)/2)/p
        z = brentq(lambda x: integral_transform(p, x),
                   leading - .35, leading + .35, xtol=1e-12)
        err1 = abs(z-leading)
        err2 = abs(z-(leading+delta))
        assert abs(integral_transform(p, z)) < 2e-10
        assert err2 < 0.002
        print(f"p={p:3d} k={k:3d} zero={z:.12f} first_error={err1:.6g} second_error={err2:.6g}")

# Cross-check the integration-by-parts identity using two independently
# parameterized integrations; use finite boundaries with negligible tails.
for p, x in ((40, 5.2), (80, 11.6), (120, 34.1)):
    lhs = x*integral_transform(p, x)/2
    rhs, _ = quad(lambda t: p*t**(p-1)*math.exp(-t**p)*math.sin(x*t),
                  0, 1.5, epsabs=2e-12, epsrel=2e-12, limit=2000)
    assert abs(lhs-rhs) < 2e-10
    print(f"Weibull identity p={p} x={x}: residual={abs(lhs-rhs):.3g}")

s_star = mp.findroot(lambda s: mp.im(mp.loggamma(1+1j*s)), (1.5, 2.0))
assert mp.mpf('1.8') < s_star < mp.mpf('1.81')
print("unique gamma-phase crossover candidate:", mp.nstr(s_star, 36))
print("Numerical checks passed; nonnumerical theorems require the accompanying proof.")
