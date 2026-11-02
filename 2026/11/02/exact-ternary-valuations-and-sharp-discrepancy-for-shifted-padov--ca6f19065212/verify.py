#!/usr/bin/env python3
"""Exact finite tests for a shifted Padovan valuation theorem.

The infinite valuation identity is proved by a matrix lifting argument;
these computations independently test its premises and consequences.
"""
from fractions import Fraction

M = ((0, 1, 0), (0, 0, 1), (1, 1, 0))
I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def matmul(a, b, modulus=None):
    c = tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                    for j in range(3)) for i in range(3))
    if modulus is not None:
        c = tuple(tuple(x % modulus for x in row) for row in c)
    return c


def matpow(a, n, modulus=None):
    assert n >= 0
    result = I
    while n:
        if n & 1:
            result = matmul(result, a, modulus)
        a = matmul(a, a, modulus)
        n //= 2
    return result


def padovan_matrix(n, modulus=None):
    z = matpow(M, n, modulus)
    ans = sum(z[0])
    return ans if modulus is None else ans % modulus


def valuation_3(n):
    assert n > 0
    e = 0
    while n % 3 == 0:
        n //= 3
        e += 1
    return e


def claimed(n):
    r = n % 13
    if r == 3:
        return 1
    if r == 4:
        return 1 + valuation_3(n + 9)
    if r == 7:
        return 1 + valuation_3(n + 6)
    return 0


def residue_set(t):
    if t == 0:
        return 13, {0, 1, 2, 5, 6, 8, 9, 10, 11, 12}
    if t == 1:
        return 39, {3, 4, 7, 16, 17, 20, 29}
    L = 13 * 3**t
    return L, {L//3 - 9, L//3 - 6, 2*L//3 - 9, 2*L//3 - 6}


def density(t):
    if t == 0:
        return Fraction(10, 13)
    if t == 1:
        return Fraction(7, 39)
    return Fraction(4, 13 * 3**t)


def sharp_discrepancy(t):
    if t == 0:
        return Fraction(15, 13)
    if t == 1:
        return Fraction(29, 13)
    return Fraction(4, 3) + Fraction(20, 13 * 3**t)


def check():
    assert matpow(M, 13) == ((7, 12, 9), (9, 16, 12), (12, 21, 16))
    A = tuple(tuple((matpow(M, 13)[i][j] - I[i][j]) // 3 for j in range(3)) for i in range(3))
    assert A == ((2, 4, 3), (3, 5, 4), (4, 7, 5))
    assert all((matpow(M, 13)[i][j] - I[i][j]) % 3 == 0 for i in range(3) for j in range(3))

    # Extend backwards by the integer companion inverse.
    p = {0: 1, 1: 1, 2: 1}
    for n in range(-1, -11, -1):
        p[n] = p[n + 3] - p[n + 1]
    assert p[-6] == p[-9] == -1

    # Independent exact integer recurrence and matrix formula.
    values = [1, 1, 1]
    for n in range(3, 4001):
        values.append(values[n-2] + values[n-3])
    for n, value in enumerate(values):
        assert valuation_3(value + 1) == claimed(n), (n, value)
    for n in (0, 1, 2, 3, 4, 7, 13, 26, 120, 400, 1000, 4000):
        assert padovan_matrix(n) == values[n], n

    # An independent modular recurrence checks a much longer prefix.
    modulus = 3**19
    a, b, c = 1, 1, 1
    terms = 200000
    for n in range(terms):
        assert valuation_3((a + 1) % modulus) == claimed(n), (n, a)
        a, b, c = b, c, (a+b) % modulus

    # Far-out special indices check exact high-order divisibility.
    for k in range(1, 14):
        m = 3**k - 1
        for r in (4, 7):
            x = (padovan_matrix(13*m + r, 3**(k+3)) + 1) % (3**(k+3))
            assert valuation_3(x) == k+1, (k, r)
        assert valuation_3((padovan_matrix(13*m+3, 27)+1) % 27) == 1

    # Full residue periods yield exact sharp errors, not extrapolations.
    for t in range(9):
        L, residues = residue_set(t)
        assert Fraction(len(residues), L) == density(t)
        assert all(claimed(n) == t for n in residues)
        assert all(claimed(n) != t for n in set(range(L)) - residues)
        count = 0
        best = Fraction(0)
        at = -1
        for N in range(L+1):
            error = abs(Fraction(count) - density(t)*N)
            if error > best:
                best, at = error, N
            if N < L and N in residues:
                count += 1
        assert best == sharp_discrepancy(t), (t, best, sharp_discrepancy(t))
        if t == 1:
            assert at == 21
    assert sharp_discrepancy(1) > max(sharp_discrepancy(t) for t in range(9) if t != 1)
    print('VERIFY_OK matrix_power=13 negative_roots=2 exact_terms=4001 modular_terms=200000 far_lifts=26 complete_period_levels=9 sharp_global=29/13')


if __name__ == '__main__':
    check()
