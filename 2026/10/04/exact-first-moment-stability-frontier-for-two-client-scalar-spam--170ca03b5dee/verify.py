#!/usr/bin/env python3
"""Numerical cross-checks for the scalar SPAM first-moment factorization."""

import cmath
import math


def mat_for_h(a, h, p, gamma):
    q = 1.0 - p
    r = 1.0 / (1.0 + gamma * h)
    return [
        [r, gamma * r * q * h, -gamma * r * q],
        [1.0, 0.0, 0.0],
        [h, -q * h, q],
    ]


def avg2(A, B):
    return [[0.5 * (A[i][j] + B[i][j]) for j in range(3)] for i in range(3)]


def det3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def char_coeffs(A):
    # det(lambda I-A) = lambda^3 + c2 lambda^2 + c1 lambda + c0.
    tr = A[0][0] + A[1][1] + A[2][2]
    principal2 = (
        A[0][0] * A[1][1] - A[0][1] * A[1][0]
        + A[0][0] * A[2][2] - A[0][2] * A[2][0]
        + A[1][1] * A[2][2] - A[1][2] * A[2][1]
    )
    return (-tr, principal2, -det3(A))


def closed_form(a, delta, p, gamma):
    rho = delta / a
    t = gamma * a
    q = 1.0 - p
    D = (1.0 + t) ** 2 - (rho * t) ** 2
    alpha = (1.0 + t) / D
    c = q * (rho * t) ** 2 / D
    # (lambda-q)(lambda^2-alpha*lambda+c)
    coeffs = (-(alpha + q), c + alpha * q, -c * q)
    roots = (
        q,
        0.5 * (alpha + cmath.sqrt(alpha * alpha - 4.0 * c)),
        0.5 * (alpha - cmath.sqrt(alpha * alpha - 4.0 * c)),
    )
    stable_formula = (2.0 - p) * (rho * t) ** 2 < (1.0 + t) ** 2
    stable_roots = max(abs(z) for z in roots) < 1.0
    return coeffs, roots, stable_formula, stable_roots


def check_close(x, y, tol=2e-11):
    scale = 1.0 + abs(x) + abs(y)
    if abs(x - y) > tol * scale:
        raise AssertionError((x, y))


def main():
    for a in (0.7, 1.0, 3.0):
        for rho in (0.0, 0.2, 0.8, 1.0):
            delta = rho * a
            for p in (0.05, 0.1, 0.5, 0.9, 1.0):
                for t in (0.01, 0.25, 1.0, 3.0, 20.0, 100.0):
                    gamma = t / a
                    Aminus = mat_for_h(a, a - delta, p, gamma)
                    Aplus = mat_for_h(a, a + delta, p, gamma)
                    M = avg2(Aminus, Aplus)
                    direct = char_coeffs(M)
                    expected, roots, sf, sr = closed_form(a, delta, p, gamma)
                    for x, y in zip(direct, expected):
                        check_close(x, y)
                    if sf != sr:
                        raise AssertionError(("stability mismatch", a, rho, p, t, roots))

    # Displayed maximal-heterogeneity t=20 examples.
    _, roots09, sf09, sr09 = closed_form(1.0, 1.0, 0.9, 20.0)
    _, roots01, sf01, sr01 = closed_form(1.0, 1.0, 0.1, 20.0)
    assert sf09 and sr09
    assert not sf01 and not sr01

    pcrit = 2.0 - (1.0 + 1.0 / 20.0) ** 2
    check_close(pcrit, 0.8975, 1e-14)
    threshold09 = 1.0 / (math.sqrt(2.0 - 0.9) - 1.0)
    threshold01 = 1.0 / (math.sqrt(2.0 - 0.1) - 1.0)
    assert 20.0 < threshold09
    assert 20.0 > threshold01

    print("verification ok")
    print("pcrit(t=20,rho=1) =", f"{pcrit:.10f}")
    print("tmax(p=0.9,rho=1) =", f"{threshold09:.10f}")
    print("tmax(p=0.1,rho=1) =", f"{threshold01:.10f}")
    print("spectral radius at p=0.9,t=20 =", f"{max(abs(z) for z in roots09):.10f}")
    print("spectral radius at p=0.1,t=20 =", f"{max(abs(z) for z in roots01):.10f}")


if __name__ == "__main__":
    main()
