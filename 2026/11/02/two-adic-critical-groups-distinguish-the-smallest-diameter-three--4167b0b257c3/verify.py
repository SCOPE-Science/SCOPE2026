#!/usr/bin/env python3
"""Finite verification of the two 64-vertex critical-group decompositions.

Run with Python 3.9+; no nonstandard packages required.
"""
from collections import Counter

SH_STEPS = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}


def graph(kind):
    coords = [(a, b, c) for a in range(4) for b in range(4) for c in range(4)]
    N = len(coords)
    A = [[0] * N for _ in range(N)]
    for i, (a, b, c) in enumerate(coords):
        for j, (u, v, w) in enumerate(coords):
            adjacent_cube = (a == u and b == v and c != w)
            if kind == 'Doob':
                adjacent_base = c == w and ((u - a) % 4, (v - b) % 4) in SH_STEPS
            else:
                adjacent_base = c == w and ((a == u) != (b == v))
            A[i][j] = int(adjacent_cube or adjacent_base)
    assert all(A[i][i] == 0 and sum(A[i]) == 9 for i in range(N))
    assert all(A[i][j] == A[j][i] for i in range(N) for j in range(N))
    # Every 16-vertex factor has strongly regular parameters (16,6,2,2).
    base = [4 * i for i in range(16)]
    assert all(sum(A[base[i]][base[k]] * A[base[k]][base[j]] for k in range(16)) ==
               (6 if i == j else 2) for i in range(16) for j in range(16))
    return [[9 * (i == j) - A[i][j] for j in range(63)] for i in range(63)]


def valuations(B, prime, precision):
    modulus = prime ** precision
    A = [[entry % modulus for entry in row] for row in B]
    n = len(A)
    values = []

    def v(x):
        if not x:
            return precision
        h = 0
        while x % prime == 0:
            x //= prime
            h += 1
        return h

    for k in range(n):
        options = ((v(A[i][j]), i, j) for i in range(k, n) for j in range(k, n) if A[i][j])
        t, i, j = min(options, default=(precision, k, k))
        if t == precision:
            values.extend([precision] * (n - k))
            break
        A[k], A[i] = A[i], A[k]
        for row in A:
            row[k], row[j] = row[j], row[k]
        scale = prime ** t
        multiplier = pow(A[k][k] // scale, -1, modulus)
        A[k] = [(x * multiplier) % modulus for x in A[k]]
        assert A[k][k] == scale
        for i in range(k + 1, n):
            x = A[i][k]
            assert x % scale == 0
            factor = x // scale
            if factor:
                A[i] = [(a - factor * b) % modulus for a, b in zip(A[i], A[k])]
            assert A[i][k] == 0
        for j in range(k + 1, n):
            x = A[k][j]
            assert x % scale == 0
            factor = x // scale
            if factor:
                for i in range(k, n):
                    A[i][j] = (A[i][j] - factor * A[i][k]) % modulus
            assert A[k][j] == 0
        values.append(t)
    assert all(v < precision for v in values)
    assert all(A[i][j] == 0 for i in range(n) for j in range(n) if i != j)
    return dict(sorted(Counter(values).items()))


def main():
    expectations = {
        'Doob': {2: {0: 28, 1: 3, 2: 4, 3: 2, 4: 6, 5: 14, 6: 6},
                 3: {0: 36, 1: 27}},
        'Hamming': {2: {0: 28, 1: 1, 2: 8, 4: 6, 5: 14, 6: 6},
                    3: {0: 36, 1: 27}},
    }
    for kind in ('Doob', 'Hamming'):
        L = graph(kind)
        for p, precision in ((2, 9), (3, 5)):
            counts = valuations(L, p, precision)
            assert counts == expectations[kind][p], (kind, p, counts)
            assert sum(v * count for v, count in counts.items()) == (147 if p == 2 else 27)
            assert sum(counts.values()) == 63
            print(kind.upper(), 'PRIME', p, 'VALUATIONS', counts)
    # The nonzero eigenvalues are 4 (9 times), 8 (27 times), 12 (27 times).
    # Matrix-tree theorem: tau = 4^9 * 8^27 * 12^27 / 64 = 2^147 * 3^27.
    assert (4**9 * 8**27 * 12**27) // 64 == 2**147 * 3**27
    print('CRITICAL_GROUP_CERTIFICATE_OK')

if __name__ == '__main__':
    main()
