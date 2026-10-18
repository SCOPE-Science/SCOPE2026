"""Exact and high-precision cross-checks for the pairwise taxonomic merger theorem.

Run: python3 check_hill_merge.py
Only Python's standard library is required. Finite checks complement the analytic proof.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import product
from random import Random


def add(p, q):
    v = [0] * max(len(p), len(q))
    for i, a in enumerate(p):
        v[i] += a
    for i, a in enumerate(q):
        v[i] += a
    return v


def mul(p, q):
    v = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            v[i + j] += a * b
    return v


def neg(p):
    return [-a for a in p]


def der(p):
    return [i * p[i] for i in range(1, len(p))]


def derivative_identity(q):
    # F(z) = N(z)/D(z), with N = 2(2+qz)^2 and D=(2+qz^2)(4+qz^2).
    N = [2 * a for a in mul([2, q], [2, q])]
    D = mul([2, 0, q], [4, 0, q])
    lhs = add(mul(der(N), D), neg(mul(N, der(D))))
    # Exact factorization: N'D - ND' = -4q(2+qz)(q^2 z^4+4q z^3+12z-8).
    rhs = [-4 * q * a for a in mul([2, q], [-8, 12, 0, 4 * q, q * q])]
    return lhs == rhs


def root(q):
    q = Decimal(q)
    lo, hi = Decimal(0), Decimal(1)
    for _ in range(260):
        z = (lo + hi) / 2
        p = q * q * z ** 4 + 4 * q * z ** 3 + 12 * z - 8
        if p > 0:
            hi = z
        else:
            lo = z
    return (lo + hi) / 2


def maximum(q, z):
    q = Decimal(q)
    return 2 * (2 + q * z) ** 2 / ((2 + q * z * z) * (4 + q * z * z))


def direct_loss(integer_counts):
    s = sum(integer_counts)
    p = [Fraction(x, s) for x in integer_counts]
    before = sum(x * x for x in p)
    after = before + 2 * p[0] * p[1]
    return 1 / before - 1 / after, 2 * p[0] * p[1] / after


def run():
    assert all(derivative_identity(q) for q in (1, 2, 3, 4, 8, 25, 98, 998))
    with localcontext() as ctx:
        ctx.prec = 70
        critical = {}
        for n in list(range(3, 22)) + [50, 100, 1000, 100000]:
            q = n - 2
            z = root(q)
            val = maximum(q, z)
            assert 0 < z < Decimal(2) / 3
            a = 1 / (2 + Decimal(q) * z)
            b = z * a
            assert abs(2 * a + Decimal(q) * b - 1) < Decimal('1e-65')
            assert val > 1
            assert val > Decimal(2 * n) / Decimal(n + 2)  # equal-abundance merger
            critical[n] = (z, val)
        rng = Random(20261016)
        tests = 0
        for n in range(3, 19):
            q = n - 2
            upper = critical[n][1]
            for _ in range(1400):
                v = [rng.randint(1, 250) for _ in range(n)]
                drop, fraction = direct_loss(v)
                value = Decimal(drop.numerator) / Decimal(drop.denominator)
                assert value <= upper + Decimal('1e-60'), (n, v, value, upper)
                assert 0 < fraction < Fraction(1, 2)
                tests += 1
        for n in (3, 4, 5):
            upper = critical[n][1]
            for v in product(range(1, 9), repeat=n):
                drop, fraction = direct_loss(v)
                value = Decimal(drop.numerator) / Decimal(drop.denominator)
                assert value <= upper + Decimal('1e-60')
                assert fraction < Fraction(1, 2)
                tests += 1
        asymptote = Decimal(3) - 2 * Decimal(2).sqrt()
        nlarge = 100000
        assert abs(critical[nlarge][1] / Decimal(nlarge - 2) - asymptote) < Decimal('0.002')
        print('derivative identities: 8 exact polynomial checks passed')
        print('positive rational profiles:', tests)
        for n in (3, 4, 10, 100, 1000, 100000):
            z, loss = critical[n]
            print('n', n, 'z', str(z)[:20], 'max loss', str(loss)[:23])
        print('asymptotic coefficient', str(asymptote)[:24])
        print('PASS')


if __name__ == '__main__':
    run()
