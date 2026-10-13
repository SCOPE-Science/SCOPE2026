"""Standalone exact-rational checks for a two-/multimode noisy inverse safeguard theorem.

Run with Python 3: python verify.py. No third-party dependencies.
Finite computations are consistency checks, not a proof of universal claims.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
from random import Random


def worst_diagonal_ratio(eigs, delta, omega):
    """Enumerate all endpoint perturbations; exact for fixed commuting spectra."""
    m = F(1)
    for signs in product((-1, 1), repeat=len(eigs)):
        values = [1 + lam * (omega + s * delta) for lam, s in zip(eigs, signs)]
        assert min(values) > 0
        ratio = max(values) / min(values)
        m = max(m, ratio)
    return m


def k2(mu, L, delta, omega):
    plus = (1 + L * (omega + delta)) / (1 + mu * (omega - delta))
    minus = (1 + mu * (omega + delta)) / (1 + L * (omega - delta))
    return max(plus, minus)


def k3(mu, L, delta, omega):
    if omega <= delta:
        return (1 + L * (omega + delta)) / (1 + L * (omega - delta))
    return (1 + L * (omega + delta)) / (1 + mu * (omega - delta))


def one_step_worst_squared(a, b):
    # A unit residual has squared endpoint eigencoordinates b/(a+b), a/(a+b).
    p, q = b / (a + b), a / (a + b)
    norm1 = p * a + q * b
    norm2 = p * a * a + q * b * b
    alpha = norm1 / norm2
    final = p * (1 - alpha * a) ** 2 + q * (1 - alpha * b) ** 2
    assert final == ((b - a) / (b + a)) ** 2
    return final


def run():
    rng = Random(1729)
    exact_cases = 0
    residual_cases = 0
    for _ in range(2100):
        mu = F(rng.randint(1, 7), rng.randint(1, 7))
        L = mu + F(rng.randint(1, 9), rng.randint(1, 7))
        delta = F(rng.randint(1, 10), rng.randint(15, 40)) / L
        omega = F(rng.randint(0, 60), rng.randint(2, 40)) / L
        assert 0 < delta < 1 / L
        e2 = worst_diagonal_ratio((mu, L), delta, omega)
        e3 = worst_diagonal_ratio((mu, L, L), delta, omega)
        assert e2 == k2(mu, L, delta, omega), (e2, k2(mu, L, delta, omega))
        assert e3 == k3(mu, L, delta, omega), (e3, k3(mu, L, delta, omega))
        assert e3 >= e2
        if omega <= delta:
            a, b = 1 + L * (omega - delta), 1 + L * (omega + delta)
        else:
            a, b = 1 + mu * (omega - delta), 1 + L * (omega + delta)
        assert b / a == e3
        one_step_worst_squared(a, b)
        exact_cases += 1
        residual_cases += 1
    # Exact-rational inequalities at the critical noise: equality throughout upper branch.
    phase_cases = 0
    for mu, L in ((F(1), F(2)), (F(1), F(5, 2)), (F(1), F(3, 2))):
        critical = (L - mu) / (2 * mu * L)
        assert critical < 1 / L
        for omega in (critical, critical + F(1, 7), critical + F(7, 3)):
            assert k2(mu, L, critical, omega) == L / mu
            assert k3(mu, L, critical, omega) == L / mu
            phase_cases += 1
    # Explicit noise-tolerant regime, including the distinct optimal dimension-dependent offsets.
    mu, L, d = 1.0, 2.0, 0.2
    w2 = (sqrt(1 + d * d * (mu + L) ** 2) - 1) / (mu + L)
    assert 0 < w2 < d
    assert abs((mu + L) * (w2 ** 2 - d ** 2) + 2 * w2) < 1e-13
    def k2float(w):
        return max((1+L*(w+d))/(1+mu*(w-d)), (1+mu*(w+d))/(1+L*(w-d)))
    def k3float(w):
        return (1 + L * (w + d)) / (1 + (L if w < d else mu) * (w - d))
    for i in range(10001):
        w = 4 * i / 10000
        assert k2float(w) + 1e-11 >= k2float(w2)
        assert k3float(w) + 1e-11 >= k3float(d)
    assert abs((k3float(d)-1)/(k3float(d)+1) - 2/7) < 1e-14
    # High-noise branch: decreasing finite-alpha worst bounds approach no-preconditioner limit.
    mu, L, d = 1.0, 2.0, 0.3
    assert 0.25 < d < 1/L
    kfunc = lambda w: max((1+L*(w+d))/(1+mu*(w-d)), (1+mu*(w+d))/(1+L*(w-d)))
    assert kfunc(0) > kfunc(d) > kfunc(1000) > L/mu
    print('VERIFY_OK exact_endpoint_enumerations=', exact_cases,
          'exact_worst_GMRES1_witnesses=', residual_cases,
          'exact_critical_phase_equalities=', phase_cases,
          'numerical_minimax_grid_checks=20002')


if __name__ == '__main__':
    run()
