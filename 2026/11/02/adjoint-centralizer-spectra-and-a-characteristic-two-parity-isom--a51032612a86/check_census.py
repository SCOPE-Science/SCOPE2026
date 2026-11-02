#!/usr/bin/env python3
"""Independent finite-field enumeration for centralizers of truncated derivations.

Execute with Python 3: python3 check_census.py
Uses coefficient arithmetic and Gaussian elimination rather than the valuation reduction.
"""
from collections import Counter
from itertools import product


class FiniteField:
    def __init__(self, p, e=1):
        self.p, self.e, self.q = p, e, p ** e
        modulus = { (2, 2): (1, 1, 1), (3, 2): (1, 0, 1) }
        self.modulus = modulus.get((p, e)) if e > 1 else None
        assert e == 1 or self.modulus is not None
        self.vec = [tuple((a // (p ** k)) % p for k in range(e)) for a in range(self.q)]
        self.lookup = {v: i for i, v in enumerate(self.vec)}
        self.add = [[self.lookup[tuple((a + b) % p for a, b in zip(self.vec[x], self.vec[y]))]
                     for y in range(self.q)] for x in range(self.q)]
        self.neg = [self.lookup[tuple(-a % p for a in self.vec[x])] for x in range(self.q)]
        self.mul = [[self._multiply(x, y) for y in range(self.q)] for x in range(self.q)]
        self.inv = [None] * self.q
        for x in range(1, self.q):
            self.inv[x] = next(y for y in range(1, self.q) if self.mul[x][y] == 1)

    def _multiply(self, x, y):
        p, e = self.p, self.e
        z = [0] * (2 * e - 1)
        for i, a in enumerate(self.vec[x]):
            for j, b in enumerate(self.vec[y]):
                z[i + j] = (z[i + j] + a * b) % p
        if e > 1:
            for i in range(len(z) - 1, e - 1, -1):
                t = z[i]
                for j in range(e):
                    z[i - e + j] = (z[i - e + j] - t * self.modulus[j]) % p
        return self.lookup[tuple(z[:e])]

    def scalar(self, a):
        return a % self.p


def nullity(f, field, allowed):
    n, d = len(f), len(allowed)
    at = {v: i for i, v in enumerate(allowed)}
    A = [[0] * d for _ in range(d)]
    for col, j in enumerate(allowed):
        for i, coefficient in enumerate(f):
            row = at.get(i + j - 1)
            if row is not None:
                term = field.mul[coefficient][field.scalar(j - i)]
                A[row][col] = field.add[A[row][col]][term]
    rank = 0
    for col in range(d):
        pivot = next((r for r in range(rank, d) if A[r][col] != 0), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        inv = field.inv[A[rank][col]]
        for k in range(col, d):
            A[rank][k] = field.mul[inv][A[rank][k]]
        for r in range(rank + 1, d):
            t = A[r][col]
            if t:
                for k in range(col, d):
                    A[r][k] = field.add[A[r][k]][field.neg[field.mul[t][A[rank][k]]]]
        rank += 1
    return d - rank


def expected_nullity(N, p, v):
    low = 0 if N % p == 0 else 1
    if v == N:
        return N - low
    return sum((j + v - 1 >= N) or ((j - v) % p == 0)
               for j in range(low, N))


def theoretical_histogram(N, field):
    q, p = field.q, field.p
    low = 0 if N % p == 0 else 1
    out = Counter({N - low: 1})
    for v in range(low, N):
        out[expected_nullity(N, p, v)] += (q - 1) * q ** (N - v - 1)
    return out


def exact_multiples_count(N, field):
    p, q = field.p, field.q
    assert N % p == 0
    k = N // p
    # S_p(q) = 1 + [(p-1)/2]*(1/q+1/q^2) for odd p.
    if p == 2:
        return q ** (N + k) + q ** (N + k - 1) - q ** (N - 1)
    h = (p - 1) // 2
    return (q ** (N + k) + h * (q ** (N + k - 1) + q ** (N + k - 2))
            - h * (q ** (N - 1) + q ** (N - 2)))


def verify(p, e, n):
    F = FiniteField(p, e)
    low = 0 if n % p == 0 else 1
    admissible = tuple(range(low, n))
    observed = Counter()
    for coefficients in product(range(F.q), repeat=len(admissible)):
        f = (0,) * low + coefficients
        observed[nullity(f, F, admissible)] += 1
    expected = theoretical_histogram(n, F)
    assert observed == expected, (p, e, n, observed, expected)
    assert sum(observed.values()) == F.q ** len(admissible)
    cpairs = sum(count * F.q ** degree for degree, count in observed.items())
    if n % p == 0:
        assert cpairs == exact_multiples_count(n, F)
    return F.q ** len(admissible)


def main():
    settings = ([(2, 1, n) for n in range(2, 9)]
                + [(3, 1, n) for n in range(2, 7)]
                + [(5, 1, n) for n in range(2, 6)]
                + [(2, 2, n) for n in range(2, 7)]
                + [(3, 2, n) for n in range(2, 5)])
    checked = sum(verify(*config) for config in settings)
    print('TRUNCATED_DERIVATION_ADJOINT_CENSUS_OK', len(settings), checked)


if __name__ == '__main__':
    main()
