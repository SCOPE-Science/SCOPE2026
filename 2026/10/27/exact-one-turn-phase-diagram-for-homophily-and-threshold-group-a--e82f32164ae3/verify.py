"""Exact finite checks of the two-binomial homophily response theorem.

All finite checks supplement, rather than replace, the proof for all group sizes.
Run with: python3 verify.py
"""
from fractions import Fraction as Q
from math import comb


def plus(p, q):
    z = [Q(0)] * max(len(p), len(q))
    for i, v in enumerate(p):
        z[i] += v
    for i, v in enumerate(q):
        z[i] += v
    return z


def mul(p, q):
    z = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            z[i + j] += a * b
    return z


def power(p, k):
    out = [Q(1)]
    for _ in range(k):
        out = mul(out, p)
    return out


def scale(p, s):
    return [s * v for v in p]


def poly_tail(n, m, p):
    one_minus = [Q(1) - p[0]] + [-x for x in p[1:]]
    out = [Q(0)]
    for k in range(m, n + 1):
        out = plus(out, scale(mul(power(p, k), power(one_minus, n - k)), Q(comb(n, k))))
    return out


def eval_poly(p, h):
    acc = Q(0)
    for c in reversed(p):
        acc = acc * h + c
    return acc


def tail(n, m, z):
    return sum((Q(comb(n, k)) * z ** k * (1 - z) ** (n - k) for k in range(m, n + 1)), Q(0))


def F(n, m, A, h):
    B = 1 - A
    return A * tail(n, m, A + B * h) + B * tail(n, m, A * (1 - h))


def dF(n, m, A, h):
    B = 1 - A
    p = A + B * h
    q = A * (1 - h)
    return A * B * n * comb(n - 1, m - 1) * (
        p ** (m - 1) * (1 - p) ** (n - m)
        - q ** (m - 1) * (1 - q) ** (n - m))


def sign(x):
    return (x > 0) - (x < 0)


def classification(n, m, A):
    a, b = m - 1, n - m
    if a > b:
        return 'minimum' if A > Q(a, n - 1) else 'increasing'
    if a < b:
        return 'maximum' if A < Q(a, n - 1) else 'decreasing'
    if A == Q(1, 2):
        return 'constant'
    return 'increasing' if A < Q(1, 2) else 'decreasing'


def run():
    checks = 0
    test_A = [Q(1, 5), Q(1, 3), Q(2, 5), Q(1, 2), Q(3, 5), Q(2, 3), Q(4, 5)]
    for n in range(2, 11):
        for m in range(1, n + 1):
            for A in test_A:
                B = 1 - A
                pp = [A, B]
                qq = [A, -A]
                polynomial = plus(scale(poly_tail(n, m, pp), A), scale(poly_tail(n, m, qq), B))
                derivative = [i * polynomial[i] for i in range(1, len(polynomial))]
                shape = classification(n, m, A)
                signs = []
                for k in range(1, 21):
                    h = Q(k, 21)
                    assert eval_poly(polynomial, h) == F(n, m, A, h)
                    analytic = dF(n, m, A, h)
                    assert eval_poly(derivative, h) == analytic
                    t = h / (1 - h)
                    aa, bb = m - 1, n - m
                    ratio_sign = sign((1 + t / A) ** aa - (1 + t / B) ** bb)
                    assert sign(analytic) == ratio_sign
                    signs.append(sign(analytic))
                    checks += 3
                nz = [v for v in signs if v]
                if shape == 'increasing':
                    assert all(v == 1 for v in signs)
                elif shape == 'decreasing':
                    assert all(v == -1 for v in signs)
                elif shape == 'constant':
                    assert all(v == 0 for v in signs)
                elif shape == 'minimum':
                    assert nz == sorted(nz)
                elif shape == 'maximum':
                    assert nz == sorted(nz, reverse=True)
                checks += 1
    A = Q(4, 5)
    hstar = Q(8, 13)
    assert classification(4, 3, A) == 'minimum'
    assert F(4, 3, A, 0) == Q(512, 625)
    assert F(4, 3, A, hstar) == Q(8704, 10985)
    assert F(4, 3, A, 1) == A
    assert dF(4, 3, A, hstar) == 0
    assert dF(4, 3, A, Q(1, 2)) < 0
    assert dF(4, 3, A, Q(3, 4)) > 0
    for h in [Q(1, 5), Q(1, 2), Q(3, 4), Q(9, 10)]:
        assert dF(4, 3, A, h) == Q(48, 625) * h * (1 - h) * (13 * h - 8)
        checks += 1
    for n in (2, 3):
        for m in range(1, n + 1):
            for A in test_A:
                assert classification(n, m, A) not in ('minimum', 'maximum')
                checks += 1
    print(f'PASS: {checks} exact-rational equalities and shape checks; four-person optimum checked.')
    print('The proof of the universal no-more-than-one-turn law is analytic, not by enumeration.')


if __name__ == '__main__':
    run()
