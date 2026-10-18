#!/usr/bin/env python3
"""Exact small-order checks of a universal Newman-sum projector identity.

Only integer arithmetic and the Python standard library are used. These
checks illustrate, but do not replace, the root-of-unity proof.
"""
from math import comb


def multiply(a, b):
    n = len(a)
    # All matrices in this checker are n-square integer matrices.
    return [[sum(a[r][t] * b[t][s] for t in range(n))
             for s in range(n)] for r in range(n)]


def add_scaled(a, b, weight):
    n = len(a)
    return [[a[r][s] + weight * b[r][s] for s in range(n)]
            for r in range(n)]


def projector_check(n):
    # A digit d contributes sign (-1)^d, residue d-u modulo n.
    a = [(-1)**d for d in range(n - 1)] + [0]
    b = [[a[(r + s) % n] for s in range(n)] for r in range(n)]
    sq = multiply(b, b)
    p = [[n if r == s else 0 for s in range(n)] for r in range(n)]
    power = [[int(r == s) for s in range(n)] for r in range(n)]
    result = [[0] * n for _ in range(n)]
    for j in range((n + 1) // 2):
        result = add_scaled(result, power, (-1)**j * comb(n, 2*j + 1))
        if j < (n - 1) // 2:
            power = multiply(power, sq)
    assert result == [[1] * n for _ in range(n)], n
    return b


def signed_digits(value, base):
    parity = 0
    while value:
        parity ^= value % base & 1
        value //= base
    return -1 if parity else 1


def direct_vector(n, x):
    base = n - 1
    vector = [0] * n
    for value in range(x):
        vector[value % n] += signed_digits(value, base)
    return vector


def vec_mul(mat, vec):
    return [sum(row[j]*vec[j] for j in range(len(vec))) for row in mat]


def direct_check(n, x):
    base = n - 1
    b = projector_check(n)
    orig = direct_vector(n, x)
    assert direct_vector(n, base*x) == vec_mul(b, orig), (n, x)
    target = sum(orig)
    now = orig
    lhs = [0] * n
    for j in range((n + 1)//2):
        coeff = (-1)**j * comb(n, 2*j + 1)
        for i in range(n):
            lhs[i] += coeff * now[i]
        if j < (n-1)//2:
            now = vec_mul(b, vec_mul(b, now))
    assert lhs == [target]*n, (n, x)
    assert target == (0 if x % 2 == 0 else signed_digits(x-1, base)), (n, x)


if __name__ == '__main__':
    orders = list(range(3, 26, 2))
    for n in orders:
        projector_check(n)
    tested = 0
    for n, max_x in [(3, 55), (5, 40), (7, 30), (9, 15)]:
        for x in range(max_x + 1):
            direct_check(n, x)
            tested += 1
    # Independent direct checks of the full summation for small arguments.
    for n, limit in [(3, 100), (5, 30), (7, 4)]:
        base = n - 1
        for x in range(limit + 1):
            total = [0] * n
            for j in range((n+1)//2):
                direct = direct_vector(n, base**(2*j) * x)
                c = (-1)**j * comb(n, 2*j + 1)
                for i in range(n):
                    total[i] += c * direct[i]
            assert total == [sum(direct_vector(n, x))]*n, (n, x)
    print('VERIFY_OK; exact polynomial projector for', len(orders),
          'odd moduli 3..25; vector/digit checks:', tested)
