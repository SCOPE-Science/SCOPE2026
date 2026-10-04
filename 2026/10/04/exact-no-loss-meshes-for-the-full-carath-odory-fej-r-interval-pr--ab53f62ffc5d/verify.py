#!/usr/bin/env python3
"""Corroborative checks for the finite-grid Carathéodory--Fejér sampling theorem.

The theorem itself is proved analytically in RESULT.md.  This script checks the
explicit continuous extremizer identity, the positive dual contact weights, and
the exact contact-grid divisibility criterion over broad finite ranges.
"""
from __future__ import annotations
import cmath
import math
from math import gcd

TOL = 2.0e-10


def check_extremizer(n: int) -> None:
    r = n + 2
    alpha = math.pi / r
    c = math.cos(alpha)
    coeff = [math.sin((j + 1) * alpha) for j in range(n + 1)]

    # Constant normalization and first cosine coefficient of (2/r)|B|^2.
    s0 = sum(x * x for x in coeff)
    s1 = sum(coeff[j] * coeff[j + 1] for j in range(n))
    assert abs((2.0 / r) * s0 - 1.0) < TOL
    assert abs((4.0 / r) * s1 - 2.0 * c) < TOL

    # Polynomial identity (1 - 2 c z + z^2) B(z) = sin(alpha)(1+z^r)
    # at a deterministic set of unit-circle points.
    for h in range(1, 18):
        t = 2.0 * math.pi * h / 37.0
        z = cmath.exp(1j * t)
        B = sum(coeff[j] * z**j for j in range(n + 1))
        lhs = (1.0 - 2.0 * c * z + z * z) * B
        rhs = math.sin(alpha) * (1.0 + z**r)
        assert abs(lhs - rhs) < 2.0e-9

    # The n remaining odd 2r-th roots are precisely zeros of B.
    for j in range(1, n + 1):
        t = (2 * j + 1) * alpha
        z = cmath.exp(1j * t)
        B = sum(coeff[k] * z**k for k in range(n + 1))
        assert abs(B) < 2.0e-9


def check_dual_weights(n: int) -> None:
    r = n + 2
    alpha = math.pi / r
    c = math.cos(alpha)
    ts = [(2 * j + 1) * alpha for j in range(1, n + 1)]
    ys = [(2.0 / r) * (c - math.cos(t)) for t in ts]
    assert min(ys) > 0.0
    assert abs(sum(ys) - 2.0 * c) < TOL
    assert abs(sum(y * math.cos(t) for y, t in zip(ys, ts)) + 1.0) < TOL
    for k in range(2, n + 1):
        moment = sum(y * math.cos(k * t) for y, t in zip(ys, ts))
        assert abs(moment) < TOL


def root_on_grid(odd: int, q: int, N: int) -> bool:
    # angle/(2*pi) = odd/q in lowest terms; it is an N-grid point iff
    # its reduced denominator divides N.
    den = q // gcd(odd, q)
    return N % den == 0


def check_contact_divisibility(n: int, N: int) -> None:
    q = 2 * (n + 2)
    all_contacts = all(root_on_grid(2 * j + 1, q, N) for j in range(1, n + 1))
    assert all_contacts == (N % q == 0)


def main() -> None:
    identity_cases = 0
    moment_cases = 0
    grid_cases = 0
    for n in range(3, 81):
        check_extremizer(n)
        check_dual_weights(n)
        identity_cases += 1
        moment_cases += 1
        for N in range(3, 501):
            check_contact_divisibility(n, N)
            grid_cases += 1
    print(f"extremizer_cases={identity_cases}")
    print(f"dual_weight_cases={moment_cases}")
    print(f"grid_divisibility_cases={grid_cases}")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
