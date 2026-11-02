#!/usr/bin/env python3
"""Independent finite spectral checks for the theta-family metric theorem.
Requires only Python 3 standard library. This is supplementary numerical evidence.
"""
from collections import deque
from math import sqrt, log2, isclose


def graph(m):
    n = m + 4
    adj = [[0] * n for _ in range(n)]
    def edge(i, j):
        adj[i][j] = adj[j][i] = 1
    for j in range(m):
        edge(0, 2 + j)
        edge(1, 2 + j)
    a, b = m + 2, m + 3
    edge(0, a)
    edge(a, b)
    edge(b, 1)
    return adj


def distances(adj):
    n = len(adj)
    out = []
    for s in range(n):
        ds = [-1] * n
        ds[s] = 0
        queue = deque([s])
        while queue:
            i = queue.popleft()
            for j, e in enumerate(adj[i]):
                if e and ds[j] == -1:
                    ds[j] = ds[i] + 1
                    queue.append(j)
        assert min(ds) == 0
        out.append(ds)
    return out


def jacobi_eigenvalues(matrix):
    n = len(matrix)
    a = [row[:] for row in matrix]
    for _ in range(90 * n * n):
        p, q, big = 0, 1, 0.0
        for i in range(n):
            for j in range(i + 1, n):
                x = abs(a[i][j])
                if x > big:
                    p, q, big = i, j, x
        if big < 2e-12:
            break
        apq = a[p][q]
        tau = (a[q][q] - a[p][p]) / (2 * apq)
        t = (1.0 if tau >= 0 else -1.0) / (abs(tau) + sqrt(1 + tau * tau))
        c = 1 / sqrt(1 + t * t)
        s = t * c
        app, aqq = a[p][p], a[q][q]
        a[p][p] = app - t * apq
        a[q][q] = aqq + t * apq
        a[p][q] = a[q][p] = 0.0
        for k in range(n):
            if k not in (p, q):
                akp, akq = a[k][p], a[k][q]
                a[k][p] = a[p][k] = c * akp - s * akq
                a[k][q] = a[q][k] = s * akp + c * akq
    else:
        raise RuntimeError('Jacobi nonconvergence')
    return sorted(a[i][i] for i in range(n))


def center(a):
    n = len(a)
    avgrow = [sum(row) / n for row in a]
    overall = sum(avgrow) / n
    return [[a[i][j] - avgrow[i] - avgrow[j] + overall for j in range(n)] for i in range(n)]


def critical_t(m):
    return ((3 * m + 2) + sqrt(29 * m * m + 92 * m + 4)) / (2 * (m + 4))


def check(m):
    g = graph(m)
    ds = distances(g)
    n = m + 4
    assert all(ds[i][j] == (0 if i == j else 1 if g[i][j] else 2)
               for i in range(n) for j in range(n))
    t = critical_t(m)
    p = log2(t / (t - 1))
    assert abs((m + 4) * t * t - (3 * m + 2) * t - 5 * m) < 1e-8
    eig = jacobi_eigenvalues(center(g))
    assert abs(eig[0] + t) < 3e-8, (m, eig[0], t)
    n_c = 2 if m == 1 else 1
    assert sum(abs(e + t) < 3e-8 for e in eig) == n_c, (m, eig[:5])
    for pp, expected in [(p / 3, 'strict'), (p, 'critical'), (p + .15, 'fail')]:
        dp = [[float(ds[i][j]) ** pp if i != j else 0. for j in range(n)] for i in range(n)]
        ev = jacobi_eigenvalues(center(dp))
        if expected == 'strict':
            # One zero eigenvalue comes from the constant vector.
            assert abs(ev[-1]) < 5e-8 and ev[-2] < -1e-6, (m, pp, ev[-3:])
        if expected == 'critical':
            assert sum(abs(v) < 5e-8 for v in ev) == n_c + 1, (m, pp, ev[-5:])
        if expected == 'fail':
            assert ev[-1] > 1e-6, (m, pp, ev[-3:])
    return p


if __name__ == '__main__':
    last = float('inf')
    for m in list(range(1, 19)) + [22, 29, 40]:
        p = check(m)
        assert p < last
        last = p
        print('m=%d  threshold=%.12f  checked' % (m, p))
    limit = log2((3 + sqrt(29)) / (1 + sqrt(29)))
    coefficient = (4 * ((3 + sqrt(29))/2) - 2) / (sqrt(29) * __import__('math').log(2) * (((3 + sqrt(29))/2) - 1))
    for m in [100, 1000, 10000]:
        p = log2(critical_t(m) / (critical_t(m) - 1))
        print('asymptotic m=%d: m*(p-limit)=%.12f' % (m, m * (p - limit)))
    print('limit %.12f ; coefficient %.12f' % (limit, coefficient))
    print('CHECK_OK')
