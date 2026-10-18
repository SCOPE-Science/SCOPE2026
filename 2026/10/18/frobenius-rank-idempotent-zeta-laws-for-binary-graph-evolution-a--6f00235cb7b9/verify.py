#!/usr/bin/env python3
"""Finite verification of binary evolution-algebra idempotent point counts.
All operations use Python integers and exact finite-field arithmetic.
"""
from itertools import product, combinations

def mul_gf(a, b, f, polynomial):
    result = 0
    for _ in range(f):
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & (1 << f):
            a ^= polynomial
    return result

def matmul(a, b, n):
    columns = [sum(((b[i] >> j) & 1) << i for i in range(n)) for j in range(n)]
    return [sum((((a[i] & columns[j]).bit_count() & 1) << j) for j in range(n)) for i in range(n)]

def nullity(rows, n):
    rows = list(rows)
    rank = 0
    for bit in range(n):
        pivot = next((i for i in range(rank, n) if (rows[i] >> bit) & 1), None)
        if pivot is None:
            continue
        rows[pivot], rows[rank] = rows[rank], rows[pivot]
        for i in range(n):
            if i != rank and (rows[i] >> bit) & 1:
                rows[i] ^= rows[rank]
        rank += 1
    return n-rank

def field_expected(a, n, f):
    power = [1 << i for i in range(n)]
    for _ in range(f):
        power = matmul(power, a, n)
    return 1 << nullity([power[i] ^ (1 << i) for i in range(n)], n)

def count_direct(a, n, f, poly):
    q = 1 << f
    squares = [mul_gf(t, t, f, poly) for t in range(q)]
    total = 0
    for x in product(range(q), repeat=n):
        sq = [squares[t] for t in x]
        for i, row in enumerate(a):
            value = 0
            for j in range(n):
                if row >> j & 1:
                    value ^= sq[j]
            if value != x[i]:
                break
        else:
            total += 1
    return total

def cycle(n):
    return [(1 << ((i-1)%n)) | (1 << ((i+1)%n)) for i in range(n)]

def petersen():
    vertices = list(combinations(range(5), 2))
    return [sum(1 << j for j, w in enumerate(vertices) if not set(v).intersection(w)) for v in vertices]

# Complete checks of all 2^(n^2) binary structure matrices for n <= 3.
for n in (1, 2, 3):
    for flat in range(1 << (n*n)):
        a = [sum(((flat >> (i*n+j)) & 1) << j for j in range(n)) for i in range(n)]
        for f, pol in ((1, 0b11), (2, 0b111), (3, 0b1011)):
            actual = count_direct(a, n, f, pol)
            expected = field_expected(a, n, f)
            assert actual == expected, (n, flat, f, actual, expected)
print('EXHAUSTIVE_BINARY_MATRICES_OK: all 530 matrices in dimensions 1 through 3, degrees 1 through 3')

# Larger graphs not present in the preceding small-matrix verification.
for n, a, f, pol, expected in (
    (5, cycle(5), 1, 0b11, 1),
    (5, cycle(5), 2, 0b111, 1),
    (5, cycle(5), 3, 0b1011, 16),
    (10, petersen(), 1, 0b11, 32),
    (10, petersen(), 2, 0b111, 64),
):
    algebraic = field_expected(a, n, f)
    direct = count_direct(a, n, f, pol)
    assert algebraic == direct == expected, (n, f, algebraic, direct, expected)
    print('GRAPH_CHECK_OK', 'vertices=',n,'field_degree=',f,'count=',expected)

# Minimal splitting-degree and eventual-core checks over F_2.
for name,a,n,L,r in (
    ('C5',cycle(5),5,3,4),
    ('Petersen',petersen(),10,2,6),
):
    identity = [1 << i for i in range(n)]
    power = identity
    for i in range(1, L+1):
        power = matmul(power, a, n)
        assert field_expected(a,n,i) < (1 << r) or i == L
    assert nullity(power,n) == n-r, (name, 'stable rank')
    assert field_expected(a,n,L) == 1 << r
print('VERIFY_OK: direct finite fields, exact binary ranks, and splitting degrees')
