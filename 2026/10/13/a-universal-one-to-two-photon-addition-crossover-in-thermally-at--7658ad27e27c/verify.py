"""Finite independent checks for a two-addition Wigner-negativity crossover.

These tests are diagnostic, not a proof of the continuous parameter theorem.
Run with Python 3, NumPy and SciPy: python verify.py.
"""
import math

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import eval_laguerre, j0

S = math.sqrt(2.0)


def negative_volume_1(theta):
    return math.expm1(-theta) / (1.0 - theta) + theta / (1.0 - theta)


def negative_volume_2(theta):
    z = S * theta
    return 2.0 * math.exp(-2.0 * theta) * (
        z * math.cosh(z) - math.sinh(z)
    ) / (1.0 - theta) ** 2


def radial_wigner(m, a, v, radius):
    # Fourier-transform the symmetric characteristic function independently.
    return 2.0 / math.pi * quad(
        lambda x: x * math.exp(-a * x * x)
        * eval_laguerre(m, v * x * x) * j0(2.0 * radius * x),
        0.0, max(16.0, 15.0 / math.sqrt(a)), epsabs=1.0e-11,
        limit=200,
    )[0]


def closed_wigner(m, a, v, radius):
    d = v - a
    if abs(d) < 1.0e-13:
        # The limit uses only the highest Laguerre monomial.
        return math.exp(-radius * radius / a) / (math.pi * a) * (
            (v * radius * radius / (a * a)) ** m / math.factorial(m)
        )
    return math.exp(-radius * radius / a) / (math.pi * a) * (
        ((a - v) / a) ** m * eval_laguerre(m, -v * radius ** 2 / (a * (a - v)))
    )


def fock_characteristic(m, thermal_mean, x):
    # Independent input Fock-basis sum, with a controlled omitted tail.
    q = thermal_mean / (1.0 + thermal_mean)
    probs = []
    for j in range(m, 240):
        k = j - m
        probs.append(math.comb(j, m) * (1.0 - q) ** (m + 1) * q ** k)
    omitted = 1.0 - sum(probs)
    assert abs(omitted) < 1.0e-12
    return math.exp(-x / 2.0) * sum(
        p * eval_laguerre(j, x) for j, p in enumerate(probs, start=m)
    )


def independent_volume(theta, m):
    a = 1.0
    v = 1.0 / (1.0 - theta)
    lo, hi = ((0, 1) if m == 1 else (2 - S, 2 + S))
    return quad(
        lambda y: theta * (theta / (1.0 - theta)) ** m
        * math.exp(-theta * y)
        * max(0, -(-1) ** m * eval_laguerre(m, y)),
        lo, hi, epsabs=2.0e-14,
    )[0]


def main():
    checks = 0
    for m in (1, 2, 3):
        for mean in (0.0, 0.2, 0.7, 1.5):
            for x in (0.05, 0.7, 2.2):
                direct = fock_characteristic(m, mean, x)
                formula = math.exp(-(mean + 0.5) * x) * eval_laguerre(m, (mean + 1) * x)
                assert abs(direct - formula) < 2.0e-11, (m, mean, x)
                checks += 1
    fock_checks = checks
    # Independent radial Fourier integration of input-output characteristic,
    # including a nonzero reservoir occupation and both sides of positivity.
    for mean, bath, eta in (
        (0, 0, 1), (0.25, 0, 0.6), (0.12, 0.3, 0.8),
        (0.75, 0.2, 0.95), (1.0, 1.5, 0.48),
    ):
        a = 0.5 + eta * mean + (1 - eta) * bath
        v = eta * (mean + 1)
        for m in (1, 2):
            for radius in (0.0, 0.25, 0.9, 1.4):
                direct = radial_wigner(m, a, v, radius)
                proposed = closed_wigner(m, a, v, radius)
                assert abs(direct - proposed) < 3.0e-9, (mean, bath, eta, m, radius, direct, proposed)
                checks += 1
    radial_checks = checks - fock_checks
    for theta in (0.05, 0.13, 0.2, 0.3, 0.4, 0.5):
        assert abs(independent_volume(theta, 1) - negative_volume_1(theta)) < 2.0e-11
        assert abs(independent_volume(theta, 2) - negative_volume_2(theta)) < 2.0e-11
        checks += 2
    volume_checks = 12
    root = brentq(lambda t: negative_volume_2(t) - negative_volume_1(t), 0.2, 0.4, xtol=1.e-15)
    assert abs(root - 0.3013805517222017) < 1.0e-13
    previous = 0.0
    # Sampling does not establish monotonicity: the analytical proof does.
    for theta in np.linspace(0.025, 0.5, 200):
        ratio = negative_volume_2(theta) / negative_volume_1(theta)
        assert ratio > previous
        previous = ratio
    # Independently check physical reparameterization for thermally populated inputs.
    for mean in (0.0, 0.2, 0.5, 0.8):
        for bath in (0.0, 0.2, 1.0):
            threshold = (bath + 0.5) / (bath + 1)
            assert 0.5 <= threshold < 1.0
            if mean < 1.0 / (2.0 * root) - 1.0:
                eta_cross = (bath + 0.5) / (bath + 1.0 - root * (mean + 1.0))
                assert threshold < eta_cross < 1
                theta = (eta_cross * (bath + 1.0) - bath - 0.5) / (eta_cross * (mean + 1.0))
                assert abs(theta - root) < 5e-14
            else:
                assert 1.0 / (2.0 * (mean + 1.0)) < root
    print('VERIFY_OK input_fock_characteristic=%d independent_hankel=%d integrated_volume=%d ratio_samples=200 thermal_phase_pairs=12 crossing=%.15f' % (
        fock_checks, radial_checks, volume_checks, root
    ))


if __name__ == '__main__':
    main()
