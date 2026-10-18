"""Reproduce exact one-step identities and finite-tolerance tests for a scalar adaptive Euler blow-up estimator.

Standard Python library only; finite tests supplement, not replace, the proof.
"""
from fractions import Fraction
from math import sqrt, isfinite


def estimate(x0, k, epsilon):
    assert x0 > 0 and k > 1 and epsilon > 0
    r = 1.0 / epsilon
    assert x0 < r
    x, elapsed, n, early, correction = x0, 0., 0, 0, 0.
    while x < r:
        h = epsilon / sqrt(2.0 * min(k * x, r))
        if k*x < r:
            early += 1
        increment = h*h*x / (1+h*x)
        correction += increment
        x += h*x*x
        elapsed += h
        n += 1
        assert n < 5000000
    return elapsed, n, early, x, correction


def verify():
    total = 0
    # Verify the telescoping inverse transformation exactly on a grid of rational states.
    for xi in [Fraction(1, 2), Fraction(3, 2), Fraction(2, 3), Fraction(7, 5)]:
        for hh in [Fraction(1, 29), Fraction(1, 8), Fraction(2, 7)]:
            xnext = xi + hh*xi*xi
            lhs = hh - (1/xi - 1/xnext)
            rhs = hh*hh*xi / (1+hh*xi)
            assert lhs == rhs, (xi, hh)
            total += 1

    # Fixed-parameter one-sided limits and tuned cancellation.
    for x0, k in [(0.5, 1.1), (0.5, 4.0), (1.0, 2.0), (1.0, 3.0), (3.0, 1.5)]:
        pred = sqrt(2/(k*x0))-1
        errors = []
        early_counts = []
        for eps in [1/400, 1/1600, 1/6400]:
            t, n, early, xend, defect = estimate(x0, k, eps)
            error = t - 1/x0
            assert isfinite(t)
            assert abs(error + 1/xend - defect) < 3e-10
            assert xend >= 1/eps
            assert n > early > 0
            assert abs(eps*n - 2*sqrt(2*k)/sqrt(x0)) < 8*sqrt(eps)
            errors.append((eps, error))
            early_counts.append(early)
            total += 5
        if abs(pred) > 0.1:
            assert abs(errors[-1][1]/errors[-1][0] - pred) < 0.045, (x0, k, pred, errors)
        else:
            assert abs(errors[-1][1]) < 4*errors[-1][0]**1.5
        total += 1
    print(f"PASS: {total} rational-algebraic and deterministic numerical assertions; universal claims require the analytical proof.")


if __name__ == '__main__':
    verify()
