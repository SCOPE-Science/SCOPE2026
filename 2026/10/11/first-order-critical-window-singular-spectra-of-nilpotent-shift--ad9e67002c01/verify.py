"""Finite checks for critical-window nilpotent-shift resolvents.

Install dependencies from requirements.txt, then run `python verify.py`.
The rational identity is exact; floating-point comparisons sample finite n only.
"""
from fractions import Fraction
from math import sqrt, tan, tanh, pi, isfinite
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq


def critical_exact(n):
    r = Fraction(n + 1, n)
    y = [Fraction(n - i) for i in range(n)]
    for i in range(n):
        d = Fraction(1) if i == 0 else 1 + r * r
        out = d * y[i]
        if i:
            out -= r * y[i - 1]
        if i + 1 < n:
            out -= r * y[i + 1]
        assert out == y[i] / (n * n), (n, i)


def root(s, j):
    if j == 1:
        if s == 1:
            return 0.0
        if s > 1:
            u = brentq(lambda x: x / tanh(x) - s, 1e-9, max(2, s + 1))
            return -u * u
        t = brentq(lambda x: x / tan(x) - s, 1e-9, pi - 1e-9)
        return t * t
    t = brentq(lambda x: x / tan(x) - s,
               (j - 1) * pi + 1e-9, j * pi - 1e-9)
    return t * t


def constant(s, w):
    if s == 1:
        return 0.0
    d = s * s + w
    return (s - 1) * w / (2 * sqrt(d) * (s * (1 - s) - w))


def singular(n, s, j):
    r = 1 + s / n
    diagonal = [1] + [1 + r * r] * (n - 1)
    eig = eigh_tridiagonal(diagonal, [-r] * (n - 1),
                           select='i', select_range=(j - 1, j - 1),
                           eigvals_only=True)[0]
    return 1 / sqrt(eig)


def main():
    for n in range(2, 51):
        critical_exact(n)
    for s in (-2.0, 0.0, 0.5, 1.0, 2.0):
        for j in (1, 2, 3):
            w = root(s, j)
            d = s * s + w
            assert d > 0
            c = constant(s, w)
            if s < 1:
                assert c > 0
            elif s > 1:
                assert c < 0
            else:
                assert c == 0
            for n in (80, 160, 320):
                numerical = singular(n, s, j)
                residual = numerical - (n / sqrt(d) + c)
                assert isfinite(residual) and abs(residual) < 12 / n, (s, j, n, residual)
                if s == 1 and j == 1:
                    assert abs(numerical - n) < 1e-7, (n, numerical)
    print('JORDAN_CRITICAL_WINDOW_CHECK_OK')


if __name__ == '__main__':
    main()
