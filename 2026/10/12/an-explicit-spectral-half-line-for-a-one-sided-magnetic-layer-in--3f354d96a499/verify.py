#!/usr/bin/env python3
"""Exact arithmetic checks accompanying a spectral counting proof.

Only finite algebra/count samples are checked here. The continuum spectral
conclusion follows from the analytical proof in RESULT.md, not these tests.
"""
from fractions import Fraction as F
from math import floor, pi, sqrt


def add(a, b):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, F(0)) + v
    return {k: v for k, v in r.items() if v}


def mul(a, b):
    r = {}
    for (i, j), c in a.items():
        for (k, ell), d in b.items():
            key = (i + k, j + ell)
            r[key] = r.get(key, F(0)) + c * d
    return {k: v for k, v in r.items() if v}


def scale(a, c):
    return {k: c * v for k, v in a.items() if c * v}


def power(a, n):
    p = {(0, 0): F(1)}
    for _ in range(n):
        p = mul(p, a)
    return p


def check_symbolic():
    M = {(1, 0): F(1)}
    z = {(0, 1): F(1)}
    one = {(0, 0): F(1)}
    t = add(M, z)
    # Exact identity for the unrounded quadratic sum, M=floor(t), z=t-M.
    sumsq = scale(mul(mul(M, add(M, one)), add(scale(M, F(2)), one)), F(1, 6))
    lhs = add(add(mul(M, power(t, 2)), scale(sumsq, -1)),
              add(scale(power(t, 3), -F(2, 3)), scale(power(t, 2), F(1, 2))))
    rhs = add(mul(t, add(add(z, scale(power(z, 2), -1)), scale(one, -F(1, 6)))),
              add(add(scale(power(z, 3), F(1, 3)), scale(power(z, 2), -F(1, 2))), scale(z, F(1, 6))))
    assert lhs == rhs, (lhs, rhs)


def count_general(t, c):
    M = t.numerator // t.denominator
    return sum(1 + (c * (t*t - m*m)).numerator // (c * (t*t - m*m)).denominator
               for m in range(1, M + 1))


def count_q(q, x, B):
    if x < B:
        return 0
    m = 1
    count = 0
    while B + q*m*m <= x:
        s = (x - B - q*m*m) / (2*B)
        count += 1 + s.numerator // s.denominator
        m += 1
    return count


def check_integer_counts():
    for c in [F(1, 4), F(7, 5), F(2), F(99, 25)]:
        for t in [F(0), F(1, 3), F(3, 2), F(13, 4), F(125, 8), F(107, 3)]:
            N = count_general(t, c)
            main = c*(F(2, 3)*t**3 - F(1, 2)*t**2)
            assert abs(F(N) - main) <= t + c*(t + 1)/6
    for B in [F(1, 2), F(1), F(5, 3)]:
        for q in [F(1, 10), F(2, 3), F(3)]:
            for x in [B, B + F(1, 4), B + 7*B, B + 83*B]:
                a = count_q(q, x + 2*B, B) - count_q(q, x, B)
                expected = 0
                while B + q*(expected + 1)**2 <= x + 2*B:
                    expected += 1
                assert a == expected


def count_width(B, w, x):
    mmax = floor(w * sqrt(max(x - B, 0)) / pi)
    return sum(1 + floor((x - B - (pi*m/w)**2)/(2*B) + 1e-10)
               for m in range(1, mmax + 1))


def check_sample():
    B, d1, d2 = 1.0, 1.0, 2.0
    L = d1 + d2
    widths = [L, d1, d2]
    K = sum(w/pi + pi/(12*B*w) for w in widths)
    C = sum(pi*pi/(12*B*w*w) for w in widths)
    A = K + L/pi
    Q = C + L*sqrt(2*B)/pi
    tstar = 2*B*(A + sqrt(A*A + Q/B))
    n0 = next(n for n in range(10000)
              if 2*B*n + (pi/L)**2 > tstar*tstar)
    assert n0 == 99
    for n in [n0, n0 + 1, n0 + 100]:
        x = B*(2*n + 1) + (pi/L)**2
        assert count_width(B, L, x) > (
            count_width(B, d1, x + 2*B) + count_width(B, d2, x + 2*B))
    return n0


if __name__ == '__main__':
    check_symbolic()
    check_integer_counts()
    n0 = check_sample()
    print('VERIFY_OK exact_polynomial_identity exact_floor_counting sample_n0=', n0)
