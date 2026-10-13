#!/usr/bin/env python3
"""Finite-field consistency checks for the null-filiform Leibniz derivation-rank census.

Only Python's standard library is required. Exhaustive checks are finite
verification, not substitutes for the general proof.
"""
from collections import Counter
from itertools import product


class Field:
    def __init__(self, q):
        assert q in (2, 3, 4, 5)
        self.q = q
        self.p = 2 if q == 4 else q
        self.elements = range(q)

    def add(self, a, b):
        return a ^ b if self.q == 4 else (a + b) % self.p

    def neg(self, a):
        return a if self.q == 4 else (-a) % self.p

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if self.q != 4:
            return (a * b) % self.p
        c = 0
        while b:
            if b & 1:
                c ^= a
            b >>= 1
            a <<= 1
            if a & 4:
                a ^= 7  # x^2+x+1
        return c

    def pow(self, a, n):
        result = 1
        while n:
            if n & 1:
                result = self.mul(result, a)
            a = self.mul(a, a)
            n >>= 1
        return result

    def inv(self, a):
        assert a
        return self.pow(a, self.q - 2)

    def scale(self, a, n):
        return self.mul(a, n % self.p)


def derivation_matrix(F, a):
    n = len(a)
    mat = [[0] * n for _ in range(n)]
    for col in range(n):
        for row in range(col, n):
            mat[row][col] = F.scale(a[0], col + 1) if row == col else a[row - col]
    return mat


def rank(F, mat):
    a = [row[:] for row in mat]
    rows = len(a)
    cols = len(a[0])
    r = 0
    for col in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = F.inv(a[r][col])
        a[r] = [F.mul(x, inv) for x in a[r]]
        for i in range(rows):
            if i == r or not a[i][col]:
                continue
            z = a[i][col]
            a[i] = [F.sub(x, F.mul(z, y)) for x, y in zip(a[i], a[r])]
        r += 1
    return r


def gauge_witness(F, coeffs):
    """Return full normalized gauge (b_0,...,b_{m-1}) and unit coefficients."""
    n = len(coeffs)
    p = F.p
    m = n // p
    if not coeffs[0] or m == 0:
        return []
    truncation = p * m
    u = [0] * truncation
    u[0] = 1
    b = [0] * m
    a = coeffs[0]
    for k in range(1, truncation):
        acc = 0
        for j in range(1, k):
            zj = F.sub(b[j // p] if j % p == 0 else 0, coeffs[j])
            acc = F.add(acc, F.mul(zj, u[k - j]))
        if k % p == 0:
            b[k // p] = F.sub(coeffs[k], acc)
            u[k] = 0
        else:
            rhs = F.sub(acc, coeffs[k])
            u[k] = F.mul(rhs, F.inv(F.scale(a, k)))
    return b, u


def gauge_resonance(F, coeffs):
    return gauge_witness(F, coeffs)[0][1:]


def check_gauge_identity(F, coeffs):
    n = len(coeffs)
    a = coeffs[0]
    m = n // F.p
    if not a or not m:
        return
    b, u = gauge_witness(F, coeffs)
    limit = F.p * m
    # a*t*u' = (b(t^p)-h(t))*u(t), modulo t^(p*m).
    for k in range(1, limit):
        lhs = F.scale(F.mul(a, u[k]), k)
        rhs = 0
        for j in range(1, k + 1):
            coefficient = F.sub(b[j // F.p] if j % F.p == 0 else 0, coeffs[j])
            rhs = F.add(rhs, F.mul(coefficient, u[k - j]))
        assert lhs == rhs, (F.q, n, coeffs, k, lhs, rhs)


def predicted_nullity(F, coeffs):
    n = len(coeffs)
    if not coeffs[0]:
        return next((i for i in range(1, n) if coeffs[i]), n)
    m = n // F.p
    if not m:
        return 0
    b = gauge_resonance(F, coeffs)
    return next((i for i, x in enumerate(b, 1) if x), m)


def predicted_counts(q, p, n):
    out = Counter({n: 1})
    for k in range(1, n):
        out[k] += (q - 1) * q ** (n - k - 1)
    m = n // p
    if m == 0:
        out[0] += (q - 1) * q ** (n - 1)
    else:
        for k in range(1, m):
            out[k] += (q - 1) ** 2 * q ** (n - k - 1)
        out[m] += (q - 1) * q ** (n - m)
    return out


def exhaustive(q, n):
    F = Field(q)
    observed = Counter()
    for coeffs in product(F.elements, repeat=n):
        matrix = derivation_matrix(F, coeffs)
        actual = n - rank(F, matrix)
        gauge = predicted_nullity(F, coeffs)
        check_gauge_identity(F, coeffs)
        assert actual == gauge, (q, n, coeffs, actual, gauge)
        observed[actual] += 1
    expected = predicted_counts(q, F.p, n)
    assert observed == expected, (q, n, observed, expected)
    assert sum(observed.values()) == q ** n
    print(f"PASS q={q} n={n}: " + str(sorted(observed.items())))


if __name__ == '__main__':
    for q, largest in ((2, 8), (3, 6), (4, 5), (5, 5)):
        for n in range(1, largest + 1):
            exhaustive(q, n)
    print('VERIFY_OK')
