#!/usr/bin/env python3
"""Independent finite-field checks for square-zero derivations of a four-dimensional algebra.
Run: python3 check.py. Uses only the Python standard library.
"""
from collections import Counter
from itertools import product

MODULI = {2: 0b11, 4: 0b111, 8: 0b1011, 16: 0b10011}


def field(q):
    modulus = MODULI[q]
    mul = [[0] * q for _ in range(q)]
    for a in range(q):
        for b in range(q):
            x, y, value = a, b, 0
            while y:
                if y & 1:
                    value ^= x
                y >>= 1
                x <<= 1
                if x & q:
                    x ^= modulus
            mul[a][b] = value
    inv = [0] * q
    for a in range(1, q):
        inv[a] = next(b for b in range(1, q) if mul[a][b] == 1)
    return mul, inv


def matrix_rank(vectors, mul, inv):
    vectors = list(vectors)
    rows = [[vectors[col][row] for col in range(len(vectors))]
            for row in range(4)]
    rank = 0
    for col in range(len(vectors)):
        pivot = next((r for r in range(rank, 4) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        factor = inv[rows[rank][col]]
        rows[rank] = [mul[factor][v] for v in rows[rank]]
        for r in range(rank + 1, 4):
            scale = rows[r][col]
            if scale:
                for j in range(col, len(vectors)):
                    rows[r][j] ^= mul[scale][rows[rank][j]]
        rank += 1
    return rank


def derivation_coeffs(matrix):
    m = matrix
    return (m[1][0], m[2][2], m[1][2], m[0][2],
            m[2][0], m[2][1], m[1][1], m[0][1])


def square_zero_derivation(coeffs, mul):
    a0, a1, a2, a3, b0, b1, b2, b3 = coeffs
    return not any((
        mul[a0][a1] ^ mul[b0][a2],
        mul[a1][a1] ^ mul[a2][b1] ^ mul[a3][b0],
        mul[a1][a2] ^ mul[a3][a0] ^ mul[a2][b2],
        mul[a2][b3] ^ mul[a3][b2],
        mul[b1][a0] ^ mul[b2][b0],
        mul[b1][a1] ^ mul[b2][b1] ^ mul[b3][b0],
        mul[b1][a2] ^ mul[b3][a0] ^ mul[b2][b2],
        mul[b1][a3] ^ mul[b3][a1],
    ))


def derivation_rank(coeffs, mul, inv):
    a0, a1, a2, a3, b0, b1, b2, b3 = coeffs
    # Columns of the derivation on the basis (1,x,y,xy); D(1)=0.
    return matrix_rank(((a0, a1, a2, a3), (b0, b1, b2, b3),
                        (0, b0, a0, a1 ^ b2)), mul, inv)


def verify_exhaustive(q):
    mul, inv = field(q)
    counts = Counter()
    for c in product(range(q), repeat=8):
        if square_zero_derivation(c, mul):
            counts[derivation_rank(c, mul, inv)] += 1
    expect = {0: 1, 1: (q + 1) * (q * q - 1), 2: q * q * (q * q - 1)}
    assert dict(counts) == expect, (q, counts, expect)
    print('exhaustive', q, dict(counts), 'OK')


def verify_rank_one_model(q):
    mul, inv = field(q)
    normalized_covectors = []
    for v in product(range(q), repeat=3):
        if not any(v):
            continue
        first = next(x for x in v if x)
        if first != 1:
            continue
        normalized_covectors.append(v)
    assert len(normalized_covectors) == q*q + q + 1
    counts = Counter()
    for v in normalized_covectors:
        for u in product(range(q), repeat=3):
            if not any(u) or (mul[u[0]][v[0]] ^ mul[u[1]][v[1]] ^ mul[u[2]][v[2]]):
                continue
            m = [[mul[u[i]][v[j]] for j in range(3)] for i in range(3)]
            c = derivation_coeffs(m)
            assert square_zero_derivation(c, mul)
            dr = derivation_rank(c, mul, inv)
            assert dr == (1 if v[0] == 0 else 2)
            counts[dr] += 1
    expect = {1: (q + 1) * (q * q - 1), 2: q * q * (q * q - 1)}
    assert dict(counts) == expect, (q, counts, expect)
    print('matrix_parameterization', q, dict(counts), 'OK')


if __name__ == '__main__':
    for q in (2, 4):
        verify_exhaustive(q)
    for q in (2, 4, 8, 16):
        verify_rank_one_model(q)
    print('SQUARE_ZERO_DERIVATION_RANK_OK')
