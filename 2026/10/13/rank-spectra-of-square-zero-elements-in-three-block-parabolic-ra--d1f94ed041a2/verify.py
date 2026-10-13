#!/usr/bin/env python3
"""Independent finite-field checks for the three-block square-zero rank formula.

Run using ``python verify.py``. Only the Python standard library is required.
The finite tests do not replace the proof for arbitrary parameters.
"""
from itertools import product
from functools import reduce
from math import prod
from collections import Counter


def field(q):
    if q == 4:
        # F_4 = F_2[t]/(t^2+t+1), encoded using coefficients as bits.
        def add(x, y):
            return x ^ y

        def mul(x, y):
            z = 0
            for bit in range(2):
                if (y >> bit) & 1:
                    z ^= x << bit
            if z & 4:
                z ^= 0b111
            return z

        return add, mul
    assert q in (2, 3, 5)
    return lambda x, y: (x + y) % q, lambda x, y: (x * y) % q


def matrix_rank(matrix, q, add, mul):
    rows = [row[:] for row in matrix]
    m, n = len(rows), len(rows[0])
    pivot_row = 0
    for col in range(n):
        pivot = next((i for i in range(pivot_row, m) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[pivot], rows[pivot_row] = rows[pivot_row], rows[pivot]
        inverse = next(x for x in range(1, q) if mul(x, rows[pivot_row][col]) == 1)
        rows[pivot_row] = [mul(inverse, x) for x in rows[pivot_row]]
        for i in range(pivot_row + 1, m):
            coefficient = rows[i][col]
            if not coefficient:
                continue
            if q == 4:
                rows[i] = [add(x, mul(coefficient, y)) for x, y in zip(rows[i], rows[pivot_row])]
            else:
                rows[i] = [(x - mul(coefficient, y)) % q for x, y in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == m:
            break
    return pivot_row


def rank_count(m, n, r, q):
    if not 0 <= r <= min(m, n):
        return 0
    numerator = prod((q**m - q**i) * (q**n - q**i) for i in range(r))
    denominator = prod(q**r - q**i for i in range(r))
    assert numerator % denominator == 0
    return numerator // denominator


def predicted(a, b, c, q):
    result = Counter()
    for i in range(min(a, b) + 1):
        count_a = rank_count(a, b, i, q)
        for j in range(min(b - i, c) + 1):
            count_b = rank_count(b - i, c, j, q)
            free = q ** (a * c - (a - i) * (c - j))
            for h in range(min(a - i, c - j) + 1):
                result[i + j + h] += count_a * count_b * free * rank_count(a - i, c - j, h, q)
    return +result


def direct(a, b, c, q):
    add, mul = field(q)
    n = a + b + c
    result = Counter()
    for entries in product(range(q), repeat=a*b + b*c + a*c):
        it = iter(entries)
        A = [[next(it) for _ in range(b)] for _ in range(a)]
        B = [[next(it) for _ in range(c)] for _ in range(b)]
        C = [[next(it) for _ in range(c)] for _ in range(a)]
        if any(
            reduce(
                add, (mul(A[i][t], B[t][j]) for t in range(b)), 0
            ) != 0
            for i in range(a) for j in range(c)
        ):
            continue
        X = [[0] * n for _ in range(n)]
        for i in range(a):
            X[i][a:a+b] = A[i]
            X[i][a+b:] = C[i]
        for i in range(b):
            X[a+i][a+b:] = B[i]
        result[matrix_rank(X, q, add, mul)] += 1
    return +result


def main():
    cases = []
    for q in (2, 3, 4, 5):
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    if q ** (a*b + b*c + a*c) <= 40000:
                        cases.append((a, b, c, q))
    for a, b, c, q in cases:
        formula = predicted(a, b, c, q)
        brute = direct(a, b, c, q)
        assert formula == brute, (a, b, c, q, formula, brute)
        maximum = min((a+b+c)//2, a+b, a+c, b+c)
        assert sorted(formula) == list(range(maximum + 1))
        ungraded = sum(rank_count(a, b, i, q) * q**(c*(b-i)+a*c)
                       for i in range(min(a, b) + 1))
        assert sum(formula.values()) == ungraded
    print('VERIFY_OK_PARABOLIC_SQUARE_ZERO', len(cases), 'exhaustive cases')
    for a,b,c,q in ((1,1,1,2),(1,2,1,2),(2,2,2,2),(2,2,2,3),(3,2,2,2)):
        print((a,b,c,q), sorted(predicted(a,b,c,q).items()))

if __name__ == '__main__':
    main()
