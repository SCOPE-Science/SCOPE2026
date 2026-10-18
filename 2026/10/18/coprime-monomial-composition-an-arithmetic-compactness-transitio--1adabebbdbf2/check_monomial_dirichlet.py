#!/usr/bin/env python3
"""Finite and asymptotic diagnostics for monomial-composition mixed commutators.

Run: python check_monomial_dirichlet.py. Requires only the Python standard library.
Finite checks do not certify the asymptotic theorem.
"""
import math


def log_weight(n, alpha):
    assert n >= 1 and alpha > -1
    if alpha == 0:
        return math.log(n)
    return (math.lgamma(alpha + 2) + 2 * math.log(n)
            + math.lgamma(n) - math.lgamma(n + alpha + 1))


def ratio(n, q, alpha):
    return math.exp((log_weight(q * n, alpha) - log_weight(n, alpha)) / 2)


def apply_mixed(m, k, n, alpha):
    """Sparse column of C_m^* C_k - C_k C_m^* on e_n (n>=1)."""
    out = {}
    if k * n % m == 0:
        j = k * n // m
        out[j] = ratio(n, k, alpha) * ratio(j, m, alpha)
    if n % m == 0:
        j = k * (n // m)
        out[j] = out.get(j, 0) - ratio(n // m, m, alpha) * ratio(n // m, k, alpha)
    return {j: v for j, v in out.items() if abs(v) > 1e-12}


def delta(j, m, k, alpha):
    a = log_weight(m * k * j, alpha)
    b = (log_weight(m * j, alpha) + log_weight(k * j, alpha)) / 2
    c = log_weight(j, alpha)
    return math.exp(a - b) - math.exp(b - c)


def sharp_coefficient(m, k, alpha):
    return (abs(alpha * (alpha + 1)) / 2
            * (m - 1) * (k - 1) / (m * k)
            * (m * k) ** ((1 - alpha) / 2))


def main():
    count = 0
    for alpha in [-0.5, 0, 0.5, 1, 2]:
        for m, k in [(2, 3), (3, 4), (4, 6)]:
            for n in range(1, 61):
                a = apply_mixed(m, k, n, alpha)
                if math.gcd(m, k) == 1:
                    expected = {} if n % m else {k * (n // m): delta(n // m, m, k, alpha)}
                    expected = {j: v for j, v in expected.items() if abs(v) > 1e-12}
                    assert set(a) == set(expected), (alpha, m, k, n, a, expected)
                    for j in a:
                        assert abs(a[j] - expected[j]) < 1e-10
                if alpha == 0 and math.gcd(m, k) == 1:
                    assert not a, (m, k, n, a)
                count += 1
    for alpha in [-0.75, -0.25, 0.5, 1, 2, 4]:
        lam = sharp_coefficient(2, 3, alpha)
        j = 180
        measured = abs(j * delta(j, 2, 3, alpha))
        assert abs(measured - lam) < max(0.05 * lam, 0.002), (alpha, measured, lam)
    for alpha in [0, 0.5, 1]:
        # Noncoprime indices n=2*j (j odd) witness a persistent column norm.
        m, k, n = 4, 6, 2 * 101
        assert n % m != 0 and (k * n) % m == 0
        c = apply_mixed(m, k, n, alpha)
        assert len(c) == 1 and next(iter(c.values())) > 0.05
    print(f"PASS: {count} finite sparse-column checks, six asymptotic diagnostics, three gcd witnesses")


if __name__ == "__main__":
    main()
