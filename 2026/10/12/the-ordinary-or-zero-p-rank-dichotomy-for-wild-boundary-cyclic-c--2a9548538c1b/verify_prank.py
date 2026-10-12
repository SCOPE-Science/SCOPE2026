#!/usr/bin/env python3
"""Exact small symbolic checks for the odd-characteristic cyclic boundary p-rank table.

The mathematical proof uses Deuring--Shafarevich and Cartier theory;
these checks independently replay the indicated polynomial and arithmetic steps.
Only the Python standard library is required.
"""
from math import comb


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
        if not out[k]:
            del out[k]
    return out


def mul(a, b):
    out = {}
    for i, u in a.items():
        for j, v in b.items():
            out[i + j] = out.get(i + j, 0) + u * v
    return {k: v for k, v in out.items() if v}


def power(a, k):
    out = {0: 1}
    for _ in range(k):
        out = mul(out, a)
    return out


def mono(k):
    return {k: 1}


def polynomial_identity_check():
    # For the three Kummer bases, set z=u^d and w=u^e*v,
    # with v^2=f(u), and compare w^m=z^alpha(z-1)^beta.
    cases = [
        (4, 2, 0, 1, 2, {3: 1, 1: -1}),
        (6, 3, 1, 2, 3, {3: 1, 0: -1}),
        (10, 5, 1, 2, 5, {5: 1, 0: -1}),
    ]
    for m, d, e, alpha, beta, f in cases:
        assert m % 2 == 0
        lhs = mul(mono(e * m), power(f, m // 2))
        rhs = mul(mono(d * alpha), power(add(mono(d), {0: -1}), beta))
        assert lhs == rhs, (m, lhs, rhs)


def hasse_witt_checks():
    # For elliptic v^2=f(u), ordinarity is the coefficient of u^(p-1)
    # in f^((p-1)/2). Both coefficients vanish here.
    for p, f in [(3, {3: 1, 1: -1}), (5, {3: 1, 0: -1})]:
        coeffs = power(f, (p - 1) // 2)
        assert coeffs.get(p - 1, 0) % p == 0
    # For the genus-two quotient v^2=u^5-1 in characteristic three,
    # H_ij=[u^(pi-j)] f^((p-1)/2) for 1<=i,j<=2.
    p = 3
    coeffs = power({5: 1, 0: -1}, (p - 1) // 2)
    H = [[coeffs.get(p * i - j, 0) % p for j in (1, 2)]
         for i in (1, 2)]
    assert H == [[0, 0], [1, 0]], H
    H2 = [[sum(H[i][k] * H[k][j] for k in range(2)) % p
           for j in range(2)] for i in range(2)]
    assert H2 == [[0, 0], [0, 0]]


def rank_and_genus_checks():
    # p, genus base, base p-rank, pole orders on base,
    # genus of the full cover, predicted p-rank of full cover.
    cases = [
        (3, 0, 0, (1, 1), 2, 2),
        (3, 0, 0, (4,), 3, 0),
        (3, 0, 0, (1, 1, 1, 1), 6, 6),
        (3, 1, 0, (4,), 6, 0),
        (5, 1, 0, (6,), 15, 0),
        (3, 2, 0, (10,), 15, 0),
        (3, 0, 0, (1, 1, 1, 1, 1), 8, 8),
        (5, 0, 0, (1, 1, 1), 8, 8),
    ]
    for p, h, base_rank, poles, genus, rank in cases:
        assert poles and all(d >= 1 and d % p for d in poles)
        twice_genus_minus_two = p * (2 * h - 2) + (p - 1) * sum(d + 1 for d in poles)
        assert twice_genus_minus_two == 2 * genus - 2
        computed_rank = p * base_rank + (p - 1) * (len(poles) - 1)
        assert computed_rank == rank
        assert computed_rank in (0, genus)


if __name__ == '__main__':
    polynomial_identity_check()
    hasse_witt_checks()
    rank_and_genus_checks()
    print('VERIFY_OK: three Kummer transformations, three Hasse computations, eight genus/p-rank rows')
