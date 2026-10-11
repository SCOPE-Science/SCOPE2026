"""Exact algebraic and independent finite Fourier checks for a five-mode Ferrers spectrum.

Run with Python 3.9+ without third-party dependencies. Exhaustive or random
finite checks corroborate, but do not replace, the general analytic proof.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
import cmath
import math
import random

S = ((0, 0), (1, 0), (2, 0), (0, 1), (1, 1))


def poly(**terms):
    return {tuple(map(int, k.split('_'))): Fraction(v) for k, v in terms.items()
            if Fraction(v) != 0}


def add(*args):
    ans = defaultdict(Fraction)
    for p in args:
        for m, c in p.items():
            ans[m] += c
    return {m: v for m, v in ans.items() if v}


def scale(p, n):
    return {m: n * c for m, c in p.items() if n * c}


def mul(a, b):
    out = defaultdict(Fraction)
    for (i, j), c in a.items():
        for (k, ell), d in b.items():
            out[(i + k, j + ell)] += c * d
    return {m: v for m, v in out.items() if v}


def power(a, n):
    p = {(0, 0): Fraction(1)}
    for _ in range(n):
        p = mul(p, a)
    return p


def derivative(p, idx):
    out = defaultdict(Fraction)
    for m, c in p.items():
        if m[idx]:
            n = list(m)
            n[idx] -= 1
            out[tuple(n)] += c * m[idx]
    return dict(out)


def embed(univariate):
    return {(i, 0): Fraction(v) for i, v in enumerate(univariate) if v}


def moment(coeff):
    conv = defaultdict(complex)
    for (x, y), a in zip(S, coeff):
        for (u, v), b in zip(S, coeff):
            conv[(x + u, y + v)] += a * b
    return sum(abs(a) ** 2 for a in conv.values())


def expanded_moment(coeff):
    a, b, c, d, e = coeff
    total = sum(abs(z) ** 2 for z in coeff)
    return (2 * total ** 2 - sum(abs(z) ** 4 for z in coeff)
            + 4 * (b * b * (a * c).conjugate()).real
            + 8 * (a * e * (b * d).conjugate()).real
            + 8 * (b * e * (c * d).conjugate()).real)


def direct_fourier(coeff, n, m):
    ans = 0.0
    for k in range(n):
        for ell in range(m):
            z = sum(c * cmath.exp(2j * math.pi * (k * x / n + ell * y / m))
                    for (x, y), c in zip(S, coeff))
            ans += abs(z) ** 4
    return ans / (n * m)


def rpol(r):
    return 2 * r ** 4 + 10 * r ** 3 - 19 * r - 4


def bracket():
    lo = Fraction(1320162, 1000000)
    hi = Fraction(1320163, 1000000)
    assert rpol(lo) < 0 < rpol(hi)
    for _ in range(100):
        mid = (lo + hi) / 2
        if rpol(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def main():
    nchecks = 0
    # Symbolic bivariate polynomial identities, not finite interpolation.
    R = {(1, 0): Fraction(1)}
    T = {(0, 1): Fraction(1)}
    one = {(0, 0): Fraction(1)}
    N = add(scale(one, 2), power(R, 2), scale(T, 2))
    Q = add(scale(one, 2), scale(power(T, 2), 2), power(R, 4),
            scale(power(R, 2), -4), scale(mul(R, T), -16))
    A = embed([2, 8, -4, 4, 1])
    B = embed([2, 8, 1])
    P = embed([14, 64, 28, 32, 5])
    D = embed([8, 32, -4, 16, 3])
    Rcrit = embed([-4, -19, 0, 10, 2])
    dt = add(scale(mul(derivative(Q, 1), N), -1),
             scale(mul(Q, derivative(N, 1)), 2))
    assert dt == scale(add(A, scale(mul(B, T), -1)), 4)
    nchecks += 1
    Nsub = add(mul(add(scale(one, 2), power(R, 2)), B), scale(A, 2))
    assert Nsub == D
    nchecks += 1
    Qsub = add(mul(add(scale(one, 2), power(R, 4),
                       scale(power(R, 2), -4)), power(B, 2)),
               scale(power(A, 2), 2), scale(mul(mul(R, A), B), -16))
    assert add(scale(power(D, 2), 2), scale(Qsub, -1)) == mul(P, D)
    nchecks += 1
    assert add(mul(derivative(P, 0), D),
               scale(mul(P, derivative(D, 0)), -1),
               scale(mul(B, Rcrit), 8)) == {}
    nchecks += 1
    # Enumerate pair-sum collisions without imposing equality by assumption.
    pair_counts = defaultdict(int)
    for u in S:
        for v in S:
            pair_counts[(u[0] + v[0], u[1] + v[1])] += 1
    assert Counter(pair_counts.values()) == Counter({1: 4, 2: 5, 3: 1, 4: 2})
    assert len(pair_counts) == 12
    assert pair_counts[(2, 0)] == 3
    assert pair_counts[(1, 1)] == pair_counts[(2, 1)] == 4
    nchecks += 1
    rng = random.Random(271828)
    for _ in range(2400):
        coeff = [complex(rng.randint(-3, 3), rng.randint(-3, 3)) for j in S]
        assert abs(moment(coeff) - expanded_moment(coeff)) < 1e-7
        nchecks += 1
    root = bracket()
    r = float(root)
    t = (r ** 4 + 4 * r ** 3 - 4 * r ** 2 + 8 * r + 2) / (r ** 2 + 8 * r + 2)
    const = (5 * r ** 4 + 32 * r ** 3 + 28 * r ** 2 + 64 * r + 14) / (3 * r ** 4 + 16 * r ** 3 - 4 * r ** 2 + 32 * r + 8)
    assert 1.320162 < r < 1.320163
    assert 1.24654 < t < 1.24655
    assert 2.6469151 < const < 2.6469152
    nchecks += 3
    for _ in range(2200):
        coeff = [complex(rng.uniform(-2, 2), rng.uniform(-2, 2)) for j in S]
        norm = sum(abs(c) ** 2 for c in coeff)
        if norm:
            assert moment(coeff) <= const * norm ** 2 + 1e-8
        nchecks += 1
    for n, m in ((5, 3), (7, 3), (5, 4), (8, 5)):
        for _ in range(20):
            coeff = [complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for j in S]
            assert abs(direct_fourier(coeff, n, m) - moment(coeff)) < 5e-9
            nchecks += 1
    for phi, psi in ((0., 0.), (0.42, 1.13), (2.5, -1.5)):
        coeff = [1, r * cmath.exp(1j * phi), cmath.exp(2j * phi),
                 math.sqrt(t) * cmath.exp(1j * psi),
                 math.sqrt(t) * cmath.exp(1j * (phi + psi))]
        norm = sum(abs(z) ** 2 for z in coeff)
        assert abs(moment(coeff) / norm ** 2 - const) < 5e-12
        assert abs(direct_fourier(coeff, 5, 3) / norm ** 2 - const) < 5e-12
        nchecks += 2
    print('PASS symbolic identities=4; pair-sum classification=1;'
          f' total checks={nchecks}; root={r:.15f}; t={t:.15f};'
          f' K={const:.15f}')


if __name__ == '__main__':
    main()
