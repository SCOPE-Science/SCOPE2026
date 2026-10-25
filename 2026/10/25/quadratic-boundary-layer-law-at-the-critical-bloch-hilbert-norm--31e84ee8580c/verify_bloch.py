#!/usr/bin/env python3
"""Numerical cross-checks of the Bloch–Hilbert boundary-layer formulas.

Requires Python 3 and SciPy. Finite samples are not a proof of the asymptotic law.
"""
import math
import warnings
from scipy.integrate import quad, IntegrationWarning
from scipy.optimize import minimize_scalar
from scipy.special import beta, hyp2f1, gamma


def error_kernel(alpha, t):
    u = 1.0 - t
    return (2.0 ** (-alpha) * u ** (2.0 - alpha)
            / (2.0 - alpha) * hyp2f1(alpha, 2.0 - alpha, 3.0 - alpha, u / 2.0))


def radial_value(alpha, r):
    if not 0.0 < r < 1.0:
        raise ValueError("r must lie strictly between zero and one")
    delta = alpha - 1.5
    d = 0.0 if delta == 0.0 else (
        delta * beta(0.5, 2.0 - alpha) / (2.0 * (alpha - 1.0)))
    m = quad(lambda y: (1 + r) ** alpha * (1 - y) * y ** (1 - alpha)
             * (2 - (1 + r) * y) ** (1 - alpha)
             * (1 - r * y) ** (2 * alpha - 3), 0, 1,
             epsabs=2e-10, epsrel=2e-10, limit=400)[0]
    rr = ((1 - r * r) ** alpha * quad(
        lambda t: t * error_kernel(alpha, t) / (1 - r * t) ** 2,
        0, 1, epsabs=2e-10, epsrel=2e-10, limit=400)[0])
    jj = ((1 - r * r) ** alpha
          * (r / (1 - r) + math.log1p(-r)) / (r * r))
    return m / (2 * (alpha - 1)) + d * jj - rr


def main():
    a = 1.5
    mp = a * beta(2-a, a) + (5 - 3*a) * beta(3-a, a-1)
    rp = beta(3-a, a-1) / (2-a)
    assert abs(mp - math.pi) < 1e-12
    assert abs(rp - math.pi) < 1e-12
    assert abs(mp / (2*(a-1)) + rp - 2 * math.pi) < 1e-12
    print("Exact beta coefficients: M' = pi, R/epsilon = pi, total = 2*pi")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", IntegrationWarning)
        for eps in [0.01, 0.001]:
            slope = (math.pi - radial_value(1.5, 1 - eps)) / eps
            print(f"critical epsilon={eps:g}, slope={slope:.7f}")
            assert 5.0 < slope < 6.5
        for delta in [0.05, 0.02, 0.01]:
            alpha = 1.5 + delta
            result = minimize_scalar(
                lambda x: -radial_value(alpha, 1 - delta*delta*x),
                bounds=(0.15, 1.5), method="bounded",
                options={"xatol": 1e-6})
            x = result.x
            gain = (radial_value(alpha, 1 - delta*delta*x)
                    - math.pi / math.sin(math.pi*(alpha-1))) / (delta*delta)
            print(f"delta={delta:.3f}, scaled_radius={x:.6f}, "
                  f"scaled_excess={gain:.6f}, limiting_values=(0.5, pi)")
            assert 0.2 < x < 0.6 and gain > 0
    print("Numerical cross-checks passed (not a proof).")

if __name__ == '__main__':
    main()
