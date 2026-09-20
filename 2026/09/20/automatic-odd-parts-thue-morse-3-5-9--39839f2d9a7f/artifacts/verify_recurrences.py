#!/usr/bin/env python3
from math import comb


def coeffs(m, N):
    a = [0] * (N + 1)
    a[0] = 1
    for k in range(1, N + 1):
        n, bit = divmod(k, 2)
        if bit == 0:
            total = 0
            for j in range(m // 2 + 1):
                idx = n - j
                if idx >= 0:
                    total += comb(m, 2 * j) * a[idx]
        else:
            total = 0
            for j in range((m - 1) // 2 + 1):
                idx = n - j
                if idx >= 0:
                    total -= comb(m, 2 * j + 1) * a[idx]
        a[k] = total
    return a


def v2(x):
    if x == 0:
        return None
    x = abs(x)
    return (x & -x).bit_length() - 1


def odd(x):
    if x == 0:
        return 0
    return x >> v2(x)


def g5(r):
    return 4 * ((r + 1) // 2) - (r & 1)


def g9(r):
    return 5 * ((r + 1) // 2) - 2 * (r & 1)


N = 200000
a3 = coeffs(3, N)
a5 = coeffs(5, N)
a9 = coeffs(9, N)

# Cubic identities and oddness of the 4n,4n+1 classes.
for n in range(1, 25000):
    assert a3[4*n + 2] == 8 * a3[n - 1]
    assert a3[4*n + 3] == 8 * a3[n]
for n in range(25000):
    assert a3[4*n] & 1
    assert a3[4*n + 1] & 1

# Fifth-power valuation formula and normalized recurrence.
for q in range(20000):
    r = v2(q + 1)
    for j in range(4):
        assert v2(a5[4*q + j]) == g5(r)
for u in range(1, 64, 2):
    for j in range(4):
        Y = {}
        for r in range(0, 10):
            idx = (1 << (r + 2)) * u - 4 + j
            if idx <= N:
                Y[r] = a5[idx] >> g5(r)
        for r in range(4, 10):
            if r in Y and r-2 in Y and r-4 in Y:
                assert Y[r] == 5 * Y[r-2] - 4 * Y[r-4]

# Ninth-power valuation formula and normalized vector recurrence.
for q in range(12000):
    r = v2(q + 1)
    for j in range(8):
        assert v2(a9[8*q + j]) == g9(r)
for u in range(1, 32, 2):
    Y = {}
    for r in range(0, 11):
        base = (1 << (r + 3)) * u
        if base <= N + 8:
            Y[r] = tuple(a9[base - i] >> g9(r) for i in range(1, 9))
    for r in range(8, 11):
        if all(rr in Y for rr in (r, r-2, r-4, r-6, r-8)):
            rhs = tuple(
                205 * Y[r-2][i]
                - 8274 * Y[r-4][i]
                + 68224 * Y[r-6][i]
                - 65536 * Y[r-8][i]
                for i in range(8)
            )
            assert Y[r] == rhs

print("cubic identities: verified")
print("m=5 valuations and normalized recurrence: verified")
print("m=9 valuations and normalized vector recurrence: verified")
print("finite coefficient range: 0..200000")
