#!/usr/bin/env python3
"""Exact rational checks for a return-time positivity theorem on finite Markov generators."""
from fractions import Fraction as F
from math import sqrt


def invert(a):
    n = len(a)
    z = [[F(a[i][j]) for j in range(n)] + [F(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot = next(k for k in range(j, n) if z[k][j])
        z[j], z[pivot] = z[pivot], z[j]
        v = z[j][j]
        z[j] = [w / v for w in z[j]]
        for k in range(n):
            if k != j:
                v = z[k][j]
                z[k] = [z[k][l] - v * z[j][l] for l in range(2 * n)]
    return [row[n:] for row in z]


def matvec(a, b):
    return [sum((v * x for v, x in zip(row, b)), F(0)) for row in a]


def generator(rates):
    n = len(rates)
    q = [[F(rates[i][j]) if i != j else F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        q[i][i] = -sum(q[i], F(0))
    return q


def resolvent(q, s):
    n = len(q)
    return invert([[F(i == j) - s * q[i][j] for j in range(n)] for i in range(n)])


def returning_transform(q, i, s):
    # Laplace transform of the first return *after departure* from i.
    n = len(q)
    sub = [j for j in range(n) if j != i]
    lam = F(1) / s
    hit = invert([[lam * F(j == k) - q[j][k] for k in sub] for j in sub])
    h = matvec(hit, [q[j][i] for j in sub])
    rate = -q[i][i]
    phi = sum((q[i][j] / rate * h[k] for k, j in enumerate(sub)), F(0))
    return F(1) / (1 + s * rate * (1 - phi))


def directed_cycle(n, rate=F(1)):
    a = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        a[i][(i + 1) % n] = rate
    return generator(a)


def check(q):
    n = len(q)
    previous = [F(1)] * n
    for s in [F(1, 30), F(1, 7), F(2, 3), F(1), F(5, 2), F(11)]:
        r = resolvent(q, s)
        assert all(sum(row, F(0)) == 1 for row in r)
        for i in range(n):
            assert r[i][i] == returning_transform(q, i, s)
            assert 0 < r[i][i] < previous[i]
            previous[i] = r[i][i]
        c = [[2 * r[i][j] - F(i == j) for j in range(n)] for i in range(n)]
        assert all(sum(row, F(0)) == 1 for row in c)
        assert all(c[i][j] >= 0 for i in range(n) for j in range(n) if i != j)
        assert all(all(c[i][j] >= 0 for j in range(n)) for i in range(n)) == all(2 * r[i][i] >= 1 for i in range(n))
    return 6 * n


def main():
    cases = [
        directed_cycle(3), directed_cycle(4), directed_cycle(5),
        directed_cycle(6), directed_cycle(7),
        generator([[0,1,0],[0,0,2],[3,0,0]]),
        generator([[0,2,0,1],[0,0,3,0],[1,0,0,2],[2,1,0,0]]),
        generator([[0,5],[2,0]]),
        generator([[0,1,2],[2,0,1],[4,3,0]])
    ]
    num = sum(check(q) for q in cases)
    for n in range(3, 16):
        # Cycle positivity boundary: 1 + r + ... + r^(n-1) = 2.
        lo, hi = F(1, 2), F(3, 4)
        for _ in range(80):
            mid = (lo + hi) / 2
            if sum((mid ** j for j in range(n)), F(0)) < 2:
                lo = mid
            else:
                hi = mid
        assert lo < hi
        assert sum((lo ** j for j in range(n)), F(0)) < 2 < sum((hi ** j for j in range(n)), F(0))
        assert lo >= F(1,2)
        if n == 3:
            exact = (sqrt(5) - 1) / 2
            assert float(lo) < exact < float(hi) or abs(float(lo)-exact)<1e-14
    print('VERIFY_OK: exact_first_return_checks=%d; directed_generators=%d; cycle_boundaries=%d' % (num, len(cases), 13))

if __name__ == '__main__':
    main()
