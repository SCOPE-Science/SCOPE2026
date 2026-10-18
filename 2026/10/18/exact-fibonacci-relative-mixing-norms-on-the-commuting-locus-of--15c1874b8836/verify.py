#!/usr/bin/env python3
"""Finite exact consistency checks for a relative-mixing Fibonacci lattice norm."""

from itertools import product


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def matvec(a, v):
    return (a[0][0] * v[0] + a[0][1] * v[1], a[1][0] * v[0] + a[1][1] * v[1])


def l1(v):
    return abs(v[0]) + abs(v[1])


M = ((1, 1), (1, 0))
A = matmul(M, M)
assert A == ((2, 1), (1, 1))
unit = ((1, 0), (0, 1), (-1, 0), (0, -1))
F = [0, 1]
for _ in range(25):
    F.append(F[-1] + F[-2])

I = ((1, 0), (0, 1))
Apow = I
Mpow = I
Minv = ((0, 1), (1, -1))
Minvpow = I
checks = 1
for n in range(13):
    if n:
        assert Mpow == ((F[n + 1], F[n]), (F[n], F[n - 1]))
        assert Minvpow == tuple(tuple((-1) ** n * a for a in row) for row in ((F[n - 1], -F[n]), (-F[n], F[n + 1])))
        checks += 2
    assert Apow == matmul(Mpow, Mpow)
    checks += 1
    best = None
    winners = []
    for a, b in product(range(-12, 13), repeat=2):
        if a == b == 0:
            continue
        v = (a, b)
        cost = l1(matvec(Mpow, v)) + l1(matvec(Minvpow, v))
        if n:
            L = F[n + 1] + F[n - 1]
            assert cost >= L * l1(v)
            checks += 1
        if best is None or cost < best:
            best, winners = cost, [v]
        elif cost == best:
            winners.append(v)
    assert best == F[n + 3], (n, best, F[n + 3])
    assert set(winners) == set(unit), (n, winners)
    checks += 2
    for v in unit:
        k = matvec(Minvpow, v)
        ak = matvec(Apow, k)
        assert l1(k) + l1(ak) == F[n + 3], (n, v, k, ak)
        assert ak == matvec(Mpow, v)
        checks += 2
    Apow = matmul(Apow, A)
    Mpow = matmul(Mpow, M)
    Minvpow = matmul(Minvpow, Minv)
print(f'PASS: {checks} exact integer assertions across times 0..12')
