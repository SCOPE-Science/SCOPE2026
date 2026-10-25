#!/usr/bin/env python3
"""Reproducible numerical checks of projected-simplex edge identities.

Only standard Python libraries are required. All universal statements in the
accompanying proof are analytical; this script is a finite consistency check.
"""
import math
import random


def inverse(a):
    n = len(a)
    t = [[float(a[i][j]) for j in range(n)] + [float(i == j) for j in range(n)] for i in range(n)]
    for p in range(n):
        pivot = max(range(p, n), key=lambda i: abs(t[i][p]))
        t[p], t[pivot] = t[pivot], t[p]
        assert abs(t[p][p]) > 1e-12
        v = t[p][p]
        t[p] = [x / v for x in t[p]]
        for i in range(n):
            if i != p:
                v = t[i][p]
                t[i] = [t[i][j] - v * t[p][j] for j in range(2 * n)]
    return [row[n:] for row in t]


def check_finite_geometry(m, k, seed):
    rng = random.Random(seed)
    z = [[rng.gauss(0.0, 1.0) for j in range(k)] for i in range(m)]
    mu = [sum(z[i][j] for i in range(m)) / m for j in range(k)]
    a = [[z[i][j] - mu[j] for j in range(k)] for i in range(m)]
    s = [[sum(a[i][r] * a[i][t] for i in range(m)) for t in range(k)] for r in range(k)]
    inv = inverse(s)

    # Build an independent orthonormal basis for the same discarded subspace.
    q = []
    for j in range(k):
        u = [a[i][j] for i in range(m)]
        for b in q:
            d = sum(u[i] * b[i] for i in range(m))
            u = [u[i] - d * b[i] for i in range(m)]
        norm = math.sqrt(sum(t * t for t in u))
        q.append([t / norm for t in u])
    assert max(abs(sum(b) / m) for b in q) < 1e-11
    assert max(abs(sum(q[i][p] * q[j][p] for p in range(m)) - float(i == j))
               for i in range(k) for j in range(k)) < 1e-11

    minimum_loss = math.inf
    maximum_projected_sq = -math.inf
    comparisons = 0
    for i in range(m):
        for j in range(i):
            d = [z[i][r] - z[j][r] for r in range(k)]
            loss_matrix = sum(d[r] * inv[r][t] * d[t] for r in range(k) for t in range(k))
            loss_basis = sum((q[r][i] - q[r][j]) ** 2 for r in range(k))
            assert abs(loss_matrix - loss_basis) < 2e-9, (m, k, i, j)
            minimum_loss = min(minimum_loss, loss_matrix)
            maximum_projected_sq = max(maximum_projected_sq, 2 - loss_basis)
            comparisons += 1
    assert abs((2 - minimum_loss) - maximum_projected_sq) < 2e-9
    return comparisons


def rate(s):
    return (s - 1 - math.log(s)) / 2


def s_root(c):
    lo, hi = 1e-15, 1.0
    assert rate(lo) >= 2 / c
    for _ in range(90):
        mid = (lo + hi) / 2
        if rate(mid) > 2 / c:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def check_chernoff():
    tests = 0
    for t in range(1, 10000):
        s = t / 10000.0
        theta = (1 - s) / (4 * s)
        j = (math.log1p(6 * theta) + math.log1p(2 * theta)) / 2 - 4 * s * theta
        h = 2 * math.log((3 - s) * (1 + s) / 4) - math.log(s) + s - 1
        hp = -((1 - s) ** 2 * (s + 3)) / (s * (3 - s) * (1 + s))
        assert abs((j - 1.5 * rate(s)) - h / 4) < 2e-11
        assert h > 0 and hp < 0
        tests += 1
    for c in (0.5, 1, 2, 4, 10, 100):
        s = s_root(c)
        assert abs(rate(s) - 2 / c) < 1e-12
        tests += 1
    return tests


def main():
    count = 0
    for m, k in ((8, 1), (9, 2), (11, 3), (14, 4), (16, 5)):
        for seed in (23, 41, 79):
            count += check_finite_geometry(m, k, seed + 1000 * m)
    rate_checks = check_chernoff()
    print("PASS: %d edge-identity comparisons; %d rate/Chernoff checks." % (count, rate_checks))
    print("No limiting probability or full theorem is certified by finite checks.")

if __name__ == '__main__':
    main()
