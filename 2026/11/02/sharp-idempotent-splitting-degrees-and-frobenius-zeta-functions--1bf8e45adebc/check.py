#!/usr/bin/env python3
"""Direct finite-field checks of idempotent counts for binary evolution algebras."""
import itertools
import random

IRRED = {1: 0x3, 2: 0x7, 3: 0xb, 4: 0x13, 5: 0x25, 6: 0x43, 7: 0x89}


def mul(a, b, s):
    mod = IRRED[s]
    res = 0
    while b:
        if b & 1:
            res ^= a
        b >>= 1
        a <<= 1
        if a & (1 << s):
            a ^= mod
    return res


def square_table(s):
    q = 1 << s
    sq = [mul(a, a, s) for a in range(q)]
    assert set(sq) == set(range(q)), (s, 'not a field')
    return sq


def multiply_rows(A, B, n):
    return tuple(_xor_selected(B, mask) for mask in A)


def _xor_selected(rows, mask):
    v = 0
    j = 0
    while mask:
        if mask & 1:
            v ^= rows[j]
        j += 1
        mask >>= 1
    return v


def mat_power(A, k, n):
    out = tuple(1 << i for i in range(n))
    while k:
        if k & 1:
            out = multiply_rows(out, A, n)
        A = multiply_rows(A, A, n)
        k >>= 1
    return out


def rank_binary(rows, n):
    pivots = {}
    for row in rows:
        x = row
        while x:
            p = x.bit_length() - 1
            if p not in pivots:
                pivots[p] = x
                break
            x ^= pivots[p]
    return len(pivots)


def predicted(A, n, s):
    P = mat_power(A, s, n)
    R = tuple(P[i] ^ (1 << i) for i in range(n))
    return 1 << (n - rank_binary(R, n))


def actual(A, n, s):
    sq = square_table(s)
    q = 1 << s
    mask = q - 1
    cnt = 0
    for z in range(q ** n):
        v = tuple((z >> (s*i)) & mask for i in range(n))
        vsq = tuple(sq[a] for a in v)
        good = True
        for i in range(n):
            a = 0
            row = A[i]
            for j in range(n):
                if (row >> j) & 1:
                    a ^= vsq[j]
            if a != v[i]:
                good = False
                break
        if good:
            cnt += 1
    return cnt


def check(A, n, s):
    a = actual(A, n, s)
    b = predicted(A, n, s)
    assert a == b, (n, s, A, a, b)
    return a


def main():
    ncases = 0
    for n, maxs in [(1, 5), (2, 4), (3, 4)]:
        for seq in itertools.product(range(1 << n), repeat=n):
            for s in range(1, maxs + 1):
                check(seq, n, s)
                ncases += 1
        print(f'EXHAUSTIVE_BINARY_STRUCTURE_MATRICES n={n} s=1..{maxs} PASS')
    A3 = (0b100, 0b101, 0b010)  # companion of t^3+t+1, order seven
    for s in range(1, 8):
        count = check(A3, 3, s)
        assert count == (8 if s == 7 else 1), (s, count)
        ncases += 1
    print('PRIMITIVE_CUBIC_DEGREE_SEVEN_DELAY PASS')
    A2 = (0b10, 0b11)  # irreducible quadratic, order three
    T2 = (0b11, 0b10)  # unipotent block, order two
    mixed = tuple(A2) + tuple(x << 2 for x in T2)
    for s in range(1, 5):
        count = check(mixed, 4, s)
        expected = 1 << ((2 if s % 3 == 0 else 0) + (2 if s % 2 == 0 else 1))
        assert count == expected, (s, count, expected)
        ncases += 1
    print('NONSEMISIMPLE_MIXED_ORDER_SIX_BLOCK PASS')
    rng = random.Random(1729)
    for n, s, samples in [(4, 2, 25), (4, 3, 25), (5, 2, 25)]:
        for _ in range(samples):
            A = tuple(rng.randrange(1 << n) for _ in range(n))
            check(A, n, s)
            ncases += 1
    print('RANDOM_HIGHER_DIMENSION_AND_SINGULAR_CHECKS PASS')
    print(f'IDEMPOTENT_EXTENSION_CENSUS_OK {ncases}_EXHAUSTIVE_FIELD_MATRIX_CASES')

if __name__ == '__main__':
    main()
