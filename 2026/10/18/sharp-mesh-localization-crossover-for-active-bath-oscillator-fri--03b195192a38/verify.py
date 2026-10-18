"""Numerical checks for cyclic Fourier aliasing and the von Mises localization limit.

Requires numpy and scipy. Run: python verify.py
Finite checks supplement, but do not replace, the accompanying proof.
"""
from math import pi, sqrt, sin
import numpy as np
from scipy.special import ive


def weights(n, k, p):
    """Finite symmetric truncation of the explicitly convergent harmonic sums."""
    h = int(15 * sqrt(p) + 20 * n + 60)
    js = np.arange(-h, h + 1)
    js = js[(js % n) == k]
    aa = (ive(abs(js), p) / ive(0, p)) ** 2
    return float(aa.sum()), float((aa / (js.astype(float) ** 2)).sum())


def independent_mode(n, k, p, alpha):
    """Diagonalize the site-space cosine friction kernel directly."""
    h = int(15 * sqrt(p) + 20 * n + 60)
    aa = np.arange(1, h + 1)
    cc = (ive(aa, p) / ive(0, p)) ** 2 * ((alpha / aa) ** 2 - 1)
    js = np.arange(n)
    matrix = np.zeros((n, n))
    for a, c in zip(aa, cc):
        matrix += c * np.cos(2 * pi * a * (js[:, None] - js[None, :]) / n)
    vector = np.exp(2j * pi * k * js / n)
    return float(np.real(np.vdot(vector, matrix @ vector) / np.vdot(vector, vector)))


def run():
    checks = 0
    for n in (3, 4, 5, 7):
        for k in range(1, n):
            for p in (3.0, 10.0, 40.0, 120.0):
                a, b = weights(n, k, p)
                # Independent exact roots-of-unity extraction from I_0(2p cos(theta/2)).
                rhs = sum(np.exp(-2j * pi * k * h / n) *
                          ive(0, 2 * p * abs(np.cos(pi * h / n))) *
                          np.exp(2 * p * abs(np.cos(pi * h / n)) - 2 * p)
                          for h in range(n))
                rhs = float((rhs / n / (ive(0, p) ** 2)).real)
                # Note ive(0,p)^2 encodes e^{-2p}; rhs explicitly rescales I_0.
                assert abs(a - rhs) < 3e-9 * max(1, a), (n, k, p, a, rhs)
                checks += 1
                for alpha in (0.3, 1.2, 3.7, 11.0):
                    direct = independent_mode(n, k, p, alpha)
                    alias = n / 2 * (alpha * alpha * b - a)
                    assert abs(direct - alias) < 1e-8 * max(1, abs(alias)), (n, k, p, alpha, direct, alias)
                    checks += 1
                critical = sqrt(a / b)
                assert critical > 0
                assert critical * critical * b - a < 1e-8
                checks += 2
        for k in range(1, n):
            p = 1600.0
            a, b = weights(n, k, p)
            a_target = sqrt(pi) / n
            b_target = pi * pi / (n * n * sin(pi * k / n) ** 2)
            threshold = sqrt(a / b)
            target = n ** .5 * abs(sin(pi * k / n)) / pi ** .75
            assert abs(a / sqrt(p) / a_target - 1) < .006
            assert abs(b / b_target - 1) < .28
            assert abs(threshold / p ** .25 / target - 1) < .18
            checks += 3
    print(f"PASS: {checks} independent finite numerical assertions")


if __name__ == '__main__':
    run()


def critical_mesh_tests():
    """Check the genuinely joint lattice/localization scaling independently."""
    for p in (400.0, 1600.0, 6400.0):
        for target_rho in (0.6, 1.2, 2.0):
            n = max(3, round(target_rho * sqrt(p)))
            k = max(1, min(n - 1, round(0.3 * n)))
            rho, x = n / sqrt(p), k / n
            a, b = weights(n, k, p)
            m = np.arange(-60.0, 61.0)
            w = np.exp(-(rho * (m + x)) ** 2)
            theta = float(w.sum())
            psi = float((w / (m + x) ** 2).sum())
            assert abs(a / theta - 1.0) < .001, (p, n, k)
            assert abs(p * b * rho ** 2 / psi - 1) < .001, (p, n, k)
            assert abs(sqrt(a / b) / (sqrt(p) * rho * sqrt(theta / psi)) - 1) < .001
    print("PASS: 27 additional joint-scaling assertions")


if __name__ == '__main__':
    critical_mesh_tests()
