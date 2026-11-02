#!/usr/bin/env python3
"""Finite reproducibility checks for long-arm spider-power zero forcing.

The universal argument is algebraic and appears in RESULT.md; numerical tests
here test small instances and do not certify an infinite family.
Uses only the Python 3 standard library.
"""
from collections import deque
from math import cos, pi, sin, ceil


def tree(m, ell):
    n = 1 + m * ell
    near = [set() for _ in range(n)]
    for arm in range(m):
        for depth in range(1, ell + 1):
            u = 1 + arm * ell + depth - 1
            v = 0 if depth == 1 else u - 1
            near[u].add(v)
            near[v].add(u)
    return near


def distances(near):
    n = len(near)
    d = []
    for source in range(n):
        row = [-1] * n
        row[source] = 0
        todo = deque([source])
        while todo:
            u = todo.popleft()
            for v in near[u]:
                if row[v] == -1:
                    row[v] = row[u] + 1
                    todo.append(v)
        d.append(row)
    return d


def polynomial_coefficients(ell, k):
    # Eigenvalues of the adjacency of the ell-vertex path, ordered increasing.
    roots = [-2 * cos(j * pi / (ell + 1)) for j in range(1, k + 1)]
    p = [1.0]
    for root in roots:
        new = [0.0] * (len(p) + 1)
        for j, coeff in enumerate(p):
            new[j] -= root * coeff
            new[j+1] += coeff
        p = new
    return p, roots


def adjacency_times(near, v):
    w = [0.0] * len(near)
    for u, nbrs in enumerate(near):
        w[u] = sum(v[t] for t in nbrs)
    return w


def polynomial_times(near, p, v):
    value = [0.0] * len(near)
    curr = v[:]
    for coeff in p:
        for u, x in enumerate(curr):
            value[u] += coeff * x
        curr = adjacency_times(near, curr)
    return value


def check_spider(m, ell, k):
    assert m >= 3 and k >= 3 and ell >= max(k + 1, ceil(1.5*k - 1))
    near = tree(m, ell)
    d = distances(near)
    p, roots = polynomial_coefficients(ell, k)
    positive = [x for x in roots if x > 1e-7]
    assert all(x <= 1 + 1e-8 for x in positive), (ell, k, positive)
    assert all(any(abs(y + x) < 1e-7 for y in roots) for x in positive)
    assert len([x for x in roots if x < -1e-7]) > len(positive)
    n = len(near)
    for source in range(n):
        e = [0.0] * n
        e[source] = 1.0
        v = polynomial_times(near, p, e)
        for u in range(n):
            if u == source:
                continue
            if d[source][u] <= k:
                assert v[u] > 1e-8, (m, ell, k, source, u, v[u])
            else:
                assert abs(v[u]) < 1e-8, (m, ell, k, source, u, v[u])
    # Each distinct root supplies m-1 independent antisymmetric arm modes.
    for j in range(1, k + 1):
        for arm in range(1, m):
            v = [0.0] * n
            for depth in range(1, ell + 1):
                basis = (-1)**depth * sin(j * depth * pi / (ell + 1))
                v[1 + (arm-1)*ell + depth - 1] = basis
                v[1 + arm*ell + depth - 1] = -basis
            residual = polynomial_times(near, p, v)
            assert max(abs(x) for x in residual) < 1e-6, (m, ell, k, j, arm)
    power_neighbors = [{v for v in range(n) if v != u and d[u][v] <= k}
                       for u in range(n)]
    # Run an independent greedy forcing closure from the outermost k sites
    # of m-1 arms. Its cardinality is (m-1)k.
    blue = {1 + arm*ell + depth - 1
            for arm in range(m - 1)
            for depth in range(ell-k+1, ell+1)}
    assert len(blue) == (m-1)*k
    while True:
        forced = set()
        for u in blue:
            white = power_neighbors[u] - blue
            if len(white) == 1:
                forced.update(white)
        if not forced:
            break
        blue.update(forced)
    assert len(blue) == n, (m, ell, k, n-len(blue))
    return n


def main():
    tested = 0
    for m in (3, 4, 5):
        for k in range(3, 10):
            lo = max(k+1, ceil(1.5*k-1))
            for ell in (lo, lo+1, lo+3):
                check_spider(m, ell, k)
                tested += 1
    print('FINITE_POLYNOMIAL_SUPPORT_AND_KERNEL_MODES_OK', tested)
    print('INDEPENDENT_GREEDY_FORCING_OK', tested)
    print('ALL_SPECTRAL_PAIRING_AND_BOUNDARY_CHECKS_OK')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
