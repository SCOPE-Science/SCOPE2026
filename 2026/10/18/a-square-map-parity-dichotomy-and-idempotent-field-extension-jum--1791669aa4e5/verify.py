#!/usr/bin/env python3
"""Finite-field verification of idempotent counts for unweighted cubelike evolution algebras.

Directly evaluates the evolution product; enumeration tests finite instances only.
"""
from itertools import product

IRR = {1: 0b11, 2: 0b111, 3: 0b1011}


def gf_mul(a, b, m):
    p = IRR[m]
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & (1 << m):
            a ^= p
    return r


def rank2(rows, n):
    basis = [0] * n
    rank = 0
    for x in rows:
        while x:
            pos = x.bit_length() - 1
            if not basis[pos]:
                basis[pos] = x
                rank += 1
                break
            x ^= basis[pos]
    return rank


def adjacency(d, S):
    N = 1 << d
    return [sum(1 << (i ^ s) for s in S) for i in range(N)]


def product_square(x, rows, m):
    N = len(rows)
    y = [0] * N
    for i in range(N):
        v = gf_mul(x[i], x[i], m)
        bitmask = rows[i]
        while bitmask:
            one = bitmask & -bitmask
            j = one.bit_length() - 1
            y[j] ^= v
            bitmask -= one
    return tuple(y)


def check(d, S, m, exhaustive=True):
    N = 1 << d
    rows = adjacency(d, S)
    q = 1 << m
    degree = len(S)
    for i in range(N):
        for j in range(N):
            count = (rows[i] & rows[j]).bit_count() & 1
            assert count == ((degree & 1) if i == j else 0), (d, S, i, j)
    if degree % 2 == 0:
        expected = 1
        for i in range(N):
            x = [0] * N
            x[i] = 1
            assert product_square(product_square(x, rows, m), rows, m) == (0,) * N
    else:
        nil_rows = [r ^ (1 << i) for i, r in enumerate(rows)]
        rank = rank2(nil_rows, N)
        expected = (1 << (N - rank)) if m % 2 else (1 << N)
        # Explicit F4 idempotents via u + omega*(A+I)u, omega^2+omega+1=0.
        if m == 2:
            seen = set()
            for u_bits in range(1 << N):
                v_bits = 0
                for i, r in enumerate(nil_rows):
                    if (r & u_bits).bit_count() & 1:
                        v_bits |= 1 << i
                x = tuple(((u_bits >> i) & 1) ^ (2 * ((v_bits >> i) & 1))
                          for i in range(N))
                assert product_square(x, rows, m) == x
                seen.add(x)
            assert len(seen) == 1 << N
    if exhaustive:
        actual = 0
        for x in product(range(q), repeat=N):
            actual += product_square(x, rows, m) == x
        assert actual == expected, (d, S, m, actual, expected)
        return (d, len(S), m, N, expected, 'exhaustive')
    return (d, len(S), m, N, expected, 'parametrization and adjacency identity')


def main():
    checks = []
    for m in (1, 2, 3):
        checks.append(check(1, (1,), m))
        for S in ((1, 2), (1, 2, 3)):
            checks.append(check(2, S, m))
    for m in (1, 2):
        for S in ((1, 2, 4), (1, 2, 4, 3), (1, 2, 4, 3, 5),
                  (1, 2, 3, 4, 5, 6, 7)):
            checks.append(check(3, S, m))
    # Independent group-ring rank check for the hypercube nilpotent part.
    for d in range(1, 8, 2):
        N = 1 << d
        S = tuple(1 << j for j in range(d))
        rows = adjacency(d, S)
        nil_rows = [r ^ (1 << i) for i, r in enumerate(rows)]
        assert rank2(nil_rows, N) == N // 2
        checks.append((d, len(S), 2, N, 1 << N, 'rank/parameter formula'))
    for line in checks:
        print('CHECK', *line)
    print('VERIFY_OK', len(checks), 'cases')


if __name__ == '__main__':
    main()
