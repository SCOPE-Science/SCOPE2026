"""Reproduce finite-size algebra and spectral checks for a directed cyclic walk.

The infinite-size asymptotic and spectral ordering require the proof in RESULT.md.
Run with Python 3 using only the standard library.
"""
from fractions import Fraction
from math import fsum, pi, log, isclose
from cmath import log as clog


def rates(n):
    return [Fraction(4 * (k + 1) * (n - k), (n + 1) ** 2)
            for k in range(n)]


def harmonic(n, order=1):
    return sum((Fraction(1, k ** order) for k in range(1, n + 1)), Fraction())


def exact_moments(n):
    pp = rates(n)
    s1 = sum((1 / p for p in pp), Fraction())
    s2 = sum((1 / p ** 2 for p in pp), Fraction())
    h1, h2 = harmonic(n), harmonic(n, 2)
    assert s1 == Fraction(n + 1, 2) * h1
    assert s2 == Fraction((n + 1) ** 2, 8) * h2 + Fraction(n + 1, 4) * h1
    assert all(0 < p <= 1 for p in pp)
    return float(s1), float(s2)


def near_one_eigenvalue(n):
    pp = [float(v) for v in rates(n)]
    s1 = fsum(1.0 / p for p in pp)
    s2 = fsum(1.0 / (p * p) for p in pp)
    delta = -2j * pi / s1 + 2 * pi ** 2 * s2 / s1 ** 3
    for _ in range(100):
        value = sum(clog(1.0 - delta / p) for p in pp) - 2j * pi
        derivative = -sum(1.0 / (p - delta) for p in pp)
        next_delta = delta - value / derivative
        if abs(next_delta - delta) < 2e-14:
            delta = next_delta
            break
        delta = next_delta
    residual = abs(sum(clog(1.0 - delta / p) for p in pp) - 2j * pi)
    assert residual < 1e-8, (n, residual)
    return 1.0 - delta, s1, s2


def main():
    for n in range(2, 41):
        exact_moments(n)
    print('EXACT_MOMENT_IDENTITIES_OK 2..40')
    for n in (20, 50, 100, 200, 500):
        lam, s1, s2 = near_one_eigenvalue(n)
        gap = 1.0 - abs(lam)
        lead = 2 * pi ** 2 * (s2 - s1) / s1 ** 3
        assert 0 < gap < 1 and abs(gap - lead) / gap < 0.2
        print(f'n={n} exact_root_gap={gap:.12g} moment_lead={lead:.12g} ratio={gap/lead:.7f}')
    print('FINITE_ROOT_CHECKS_OK; asymptotic and root dominance remain analytic')


if __name__ == '__main__':
    main()
