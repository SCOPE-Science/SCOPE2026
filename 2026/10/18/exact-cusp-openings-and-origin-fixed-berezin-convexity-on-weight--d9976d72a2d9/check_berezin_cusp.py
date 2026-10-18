"""Finite consistency checks for local Berezin-range cusp opening.

This is not an infinite-dimensional proof; see RESULT.md for that proof.
Standard library only; execute: python3 check_berezin_cusp.py
"""
import cmath
import math


def rho_berezin(t, theta, exponent, a, b, m):
    w = math.sqrt(t) * cmath.exp(1j * theta)
    phi = a * w + b * w ** (m + 1)
    z = (1.0 - t) / (1.0 - w.conjugate() * phi)
    return z ** exponent


def find_t(x, theta, exponent, a, b, m, rot):
    lo, hi = 0.0, 0.10
    for _ in range(48):
        mid = (lo + hi) / 2
        got = (rot * (1 - rho_berezin(mid, theta, exponent, a, b, m))).real
        if got < x:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def test_case(exponent, a, b, m, x):
    rot = ((1 - a) / abs(1 - a)).conjugate()
    t0 = find_t(x, 0.0, exponent, a, 0.0j, m, rot)
    baseline = (rot * (1 - rho_berezin(t0, 0, exponent, a, 0, m))).imag
    y = []
    for j in range(360):
        theta = 2 * math.pi * j / 360
        t = find_t(x, theta, exponent, a, b, m, rot)
        y.append((rot * (1 - rho_berezin(t, theta, exponent, a, b, m))).imag)
    nu = 1 + m / 2
    predicted = abs(b) / (exponent ** (m / 2) * abs(1 - a) ** nu) * x ** nu
    plus = (max(y) - baseline) / predicted
    minus = (baseline - min(y)) / predicted
    assert abs(plus - 1) < 0.09, (exponent, a, b, m, x, 'plus', plus)
    assert abs(minus - 1) < 0.09, (exponent, a, b, m, x, 'minus', minus)
    return plus, minus


def main():
    tested = 0
    for exponent in (0.37, 0.82):
        for a, b in ((0.10 + 0.15j, 0.12 + 0.03j), (-0.13 + 0.08j, -0.09 + 0.11j)):
            for m in (1, 2, 3):
                for x in (0.0015, 0.003):
                    plus, minus = test_case(exponent, a, b, m, x)
                    tested += 2
    print('PASS: {} one-sided scaled cusp diagnostics across {} symbol families.'.format(tested, tested // 4))


if __name__ == '__main__':
    main()
