#!/usr/bin/env python3
"""Finite consistency checks for the higher-moment entropy bound.

These checks corroborate algebraic reductions; the all-parameter theorem is proved
in RESULT.md.
"""
import math


def R(N, q):
    out = float(N ** (q - 1))
    for j in range(1, q):
        out /= N + j
    return out


def closed_bound(N, q, eps, eta):
    r = R(N, q)
    return (
        2 * q / (math.e * (q - 1) * math.log(2))
        * eta ** (1 - 1 / q)
        * (((2 + eps) * math.factorial(q) * r) / 2) ** (1 / q)
    )


def cutoff_bound(N, q, eps, eta):
    r = R(N, q)
    B = (((2 + eps) * math.factorial(q) * r) / (2 * eta)) ** (1 / q)
    val = (1 / (math.e * math.log(2))) * (
        2 * eta * B
        + (2 + eps) * math.factorial(q) * r / ((q - 1) * B ** (q - 1))
    )
    return B, val


def main():
    for N in (2, 4, 16, 1024):
        for q in (2, 4, 6, 10):
            r = R(N, q)
            assert 0 < r <= 1
            for eps in (0.0, 0.5, 1.0):
                for eta in (1e-6, 1e-3, 0.1):
                    B, a = cutoff_bound(N, q, eps, eta)
                    b = closed_bound(N, q, eps, eta)
                    assert B > 0
                    assert math.isclose(a, b, rel_tol=2e-13, abs_tol=2e-13)
                    if q == 2:
                        source_form = 4 * math.sqrt((2 + eps) * r * eta) / (math.e * math.log(2))
                        assert math.isclose(b, source_form, rel_tol=2e-13, abs_tol=2e-13)
    c = 8 * math.sqrt(3 / 2) / math.log(2)
    assert c < 15
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
