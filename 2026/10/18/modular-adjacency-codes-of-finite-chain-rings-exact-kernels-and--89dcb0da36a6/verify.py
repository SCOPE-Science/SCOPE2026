#!/usr/bin/env python3
"""Finite independent tests for modular adjacency codes of chain-ring zero-divisor graphs.

Rows are generated from the graph adjacency predicate alone, without using the
claimed rank, kernel, or generator structure in the elimination routine.
"""
from itertools import product

CASES = [(2, 3, 2), (2, 4, 2), (2, 5, 2), (2, 6, 2),
         (2, 7, 2), (2, 8, 2), (3, 3, 3), (3, 4, 3),
         (3, 5, 3), (3, 6, 3), (4, 3, 2), (4, 4, 2),
         (4, 5, 2), (5, 3, 5), (5, 4, 5), (9, 3, 3)]


def row_reduction(rows, p):
    pivots = {}
    for source in rows:
        v = source.copy()
        for pivot in sorted(pivots):
            if v[pivot]:
                factor = v[pivot]
                base = pivots[pivot]
                v = [(a - factor * b) % p for a, b in zip(v, base)]
        if any(v):
            pivot = next(i for i, a in enumerate(v) if a)
            inv = pow(v[pivot], -1, p)
            pivots[pivot] = [(a * inv) % p for a in v]
    return pivots


def belongs(v, basis, p):
    w = v.copy()
    for pivot in sorted(basis):
        if w[pivot]:
            coef = w[pivot]
            w = [(a - coef * b) % p for a, b in zip(w, basis[pivot])]
    return not any(w)


def dot(a, b, p):
    return sum(x * y for x, y in zip(a, b)) % p


def run_case(q, m, p):
    assert q > 1 and q % p == 0 and all(p % k for k in range(2, p))
    levels = []
    for i in range(1, m):
        levels.extend([i] * ((q - 1) * q ** (m - i - 1)))
    N = len(levels)
    rows = [[int(a != b and levels[a] + levels[b] >= m)
             for b in range(N)] for a in range(N)]
    pivots = row_reduction(rows, p)
    t = (m + 1) // 2
    low = [j for j, val in enumerate(levels) if val < t]
    high = [j for j, val in enumerate(levels) if val >= t]
    assert len(low) == q ** (m - 1) - q ** (m // 2)
    assert len(pivots) == q ** (m // 2), (q, m, 'rank', len(pivots))

    # Check a complete spanning basis of the proposed kernel, starting from
    # coordinates e_x-e_anchor of the low-layer zero-sum hyperplane.
    anchor = low[0]
    ker_basis = []
    for k in low[1:]:
        v = [0] * N
        v[anchor] = p - 1
        v[k] = 1
        sums = {i: sum(v[j] for j, x in enumerate(levels) if x == i) % p
                for i in range(1, t)}
        for j in high:
            i = levels[j]
            if i <= m - 2:
                v[j] = sum(sums.get(a, 0) for a in range(m - i, t)) % p
        assert not any(dot(r, v, p) for r in rows), (q, m, 'kernel')
        ker_basis.append(v)
    assert len(ker_basis) == N - len(pivots), (q, m, 'nullity')

    # Standard-basis vectors supported on the socle must be in the rowspace.
    for j in range(N):
        if levels[j] == m - 1:
            e = [int(i == j) for i in range(N)]
            assert belongs(e, pivots, p), (q, m, 'distance 1')

    # Check claimed one-dimensional hull vector belongs to both rowspace
    # and kernel; use Gram rank of the full kernel basis for exclusivity.
    h = [int(a < t) for a in levels]
    assert belongs(h, pivots, p)
    assert not any(dot(r, h, p) for r in rows)
    gram = [[dot(u, v, p) for v in ker_basis] for u in ker_basis]
    assert len(row_reduction(gram, p)) == len(ker_basis) - 1, (q, m, 'hull')
    # dual weight 2 in an individual low block, and no weight one.
    assert levels[low[0]] == levels[low[1]]
    two = [0] * N
    two[low[0]] = 1
    two[low[1]] = p - 1
    assert not any(dot(r, two, p) for r in rows)
    for j in range(N):
        assert any(row[j] for row in rows), (q, m, 'zero column')
    return (q, m, p, N, len(pivots), len(ker_basis))


if __name__ == '__main__':
    values = [run_case(*case) for case in CASES]
    for entry in values:
        print('PASS q=%d m=%d p=%d N=%d rank=%d dual=%d' % entry)
    print('VERIFY_OK %d independent finite configurations' % len(values))
