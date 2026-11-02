"""Finite numerical diagnostics for angular Toeplitz moment-curvature asymptotics.

Run: python checks/moment_curvature_check.py (requires mpmath).
These tests do not replace the analytic proof of infinite-index assertions.
"""
from mpmath import mp

mp.dps = 65
checks = 0


def assert_close(actual, target, tolerance, context):
    global checks
    if abs(actual / target - 1) >= tolerance:
        raise AssertionError(f"{context}: obtained {actual}, expected {target}")
    checks += 1


def moment_log(x, family, parameter):
    if family == "disk":
        alpha = parameter
        return mp.loggamma(alpha + 2) + mp.loggamma(x + 1) - mp.loggamma(x + alpha + 2)
    a = parameter
    return mp.loggamma((x + 1) / a) - mp.loggamma(1 / a)


def square_weight(n, m, family, parameter):
    value = (2 * moment_log(n + mp.mpf(m) / 2, family, parameter)
             - moment_log(n, family, parameter) - moment_log(n + m, family, parameter))
    return mp.exp(value)


def commutator_diagonal(n, m, family, parameter):
    return square_weight(n, m, family, parameter) - (
        square_weight(n - m, m, family, parameter) if n >= m else 0
    )


def coefficient(m, family, parameter):
    if family == "disk":
        return mp.mpf(m) ** 3 * (parameter + 1) / 2
    return mp.mpf(m) ** 3 / (4 * parameter)


for family, parameters in (("disk", (mp.mpf("-0.5"), mp.mpf("0"), mp.mpf("2"))),
                           ("fock", (mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2")))):
    exponent = 3 if family == "disk" else 2
    for parameter in parameters:
        for m in (1, 2, 4):
            previous = mp.mpf("0")
            for n in range(60):
                w = square_weight(n, m, family, parameter)
                if not (0 < w < 1):
                    raise AssertionError("Toeplitz phase weight must belong to (0,1)")
                checks += 1
                if n > 0 and not w > previous:
                    raise AssertionError("Toeplitz phase weights must strictly increase")
                if n > 0:
                    checks += 1
                previous = w
                q = commutator_diagonal(n, m, family, parameter)
                if q <= 0:
                    raise AssertionError("Self-commutator diagonal must be positive")
                checks += 1
            for n in (1000, 5000, 20000):
                ratio = commutator_diagonal(n, m, family, parameter) * n ** exponent / coefficient(m, family, parameter)
                assert_close(ratio, 1, mp.mpf("0.035"), (family, parameter, m, n))
            # The finite telescoping trace equals the final m squared weights exactly.
            end = 80
            trace = mp.fsum(commutator_diagonal(n, m, family, parameter) for n in range(end + 1))
            tail = mp.fsum(square_weight(k, m, family, parameter) for k in range(end - m + 1, end + 1))
            if abs(trace - tail) >= mp.mpf("1e-48"):
                raise AssertionError("Finite trace telescoping identity")
            checks += 1

print(f"PASS: {checks} finite numerical assertions across disk and power-Fock families")
