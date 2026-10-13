#!/usr/bin/env python3
"""Finite, independent checks for rank spectra of square-zero derivations.

Usage: python3 verify_square_zero.py
The exhaustive ranges below are finite and are not an infinite proof.
"""
from collections import Counter
from itertools import product


def field_mul(a, b, q):
    if q == 2:
        return a & b
    assert q == 4
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7    # GF(4) = F_2[z]/(z^2+z+1)
    return result


def field_inv(a, q):
    assert a
    if q == 2:
        return 1
    return (0, 1, 3, 2)[a]


def matrix_rank(matrix, q):
    a = [row[:] for row in matrix]
    n = len(a)
    m = len(a[0]) if n else 0
    r = 0
    for col in range(m):
        pivot = next((i for i in range(r, n) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = field_inv(a[r][col], q)
        for j in range(col, m):
            a[r][j] = field_mul(inv, a[r][j], q)
        for i in range(r + 1, n):
            factor = a[i][col]
            if factor:
                for j in range(col, m):
                    a[i][j] ^= field_mul(factor, a[r][j], q)
        r += 1
        if r == n:
            break
    return r


def derivation_matrix(f, n):
    a = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(1, n, 2):
        for k in range(n - j + 1):
            a[j - 1 + k][j] = f[k]
    return a


def squared_is_zero(a, q):
    n = len(a)
    for i in range(n):
        for j in range(n):
            total = 0
            for k in range(n):
                total ^= field_mul(a[i][k], a[k][j], q)
            if total:
                return False
    return True


def product_zero(a, b, length, q):
    for d in range(length):
        total = 0
        for i in range(d + 1):
            total ^= field_mul(a[i], b[d - i], q)
        if total:
            return False
    return True


def pair_condition(f, n, q):
    s = n // 2
    if n % 2 == 0:
        E = list(f[0::2])
        H = list(f[1::2])
    else:
        E = list(f[2::2])
        H = list(f[1::2])
    assert len(E) == len(H) == s
    return product_zero(E, H, s, q) and product_zero(H, H, s, q)


def expected(s, q):
    out = Counter({0: 1})
    for r in range(1, s + 1):
        out[r] = ((q*q - 1) * q**(2*r - 2)
                  if r <= s//2 else (q - 1) * q**(s - 1))
    return out


def exhaustive_case(n, q):
    s = n // 2
    actual = Counter()
    for f in product(range(q), repeat=n):
        if n % 2 and f[0] != 0:
            continue  # D(t^n)=0 is necessary and sufficient.
        matrix = derivation_matrix(f, n)
        zero = squared_is_zero(matrix, q)
        assert zero == pair_condition(f, n, q), (n, q, f)
        v = next((i for i, c in enumerate(f) if c), n)
        predicted_rank = (n - v + 1)//2 if v < n else 0
        assert matrix_rank(matrix, q) == predicted_rank, (n, q, f)
        if zero:
            actual[predicted_rank] += 1
    assert actual == expected(s, q), (n, q, actual, expected(s, q))
    total = sum(actual.values())
    assert total == q**s + (s//2)*(q - 1)*q**(s-1)
    return actual


def main():
    for q, biggest_n in ((2, 9), (4, 7)):
        for n in range(2, biggest_n):
            observed = exhaustive_case(n, q)
            print(f'n={n} q={q} histogram={dict(sorted(observed.items()))}')
        for s in range(1, biggest_n//2):
            assert exhaustive_case(2*s, q) == exhaustive_case(2*s+1, q)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
