#!/usr/bin/env python3
"""Exact integer checks of the Laplacian polynomial and spanning-tree formula.

Requires Python 3 standard library only. The proofs for all dimensions are
mathematical; checks below cover finitely many small parameters.
"""

def graph_laplacian(m):
    names = [('o',)] + [('a', i) for i in range(m)] + [
        ('b', i, j) for i in range(m) for j in range(m) if i != j]
    idx = {v: i for i, v in enumerate(names)}
    n = len(names)
    a = [[0] * n for _ in range(n)]
    edges = []
    for i in range(m):
        edges.append((('o',), ('a', i)))
        for j in range(m):
            if i != j:
                edges.append((('a', i), ('b', i, j)))
                if i < j:
                    edges.append((('b', i, j), ('b', j, i)))
        for j in range(m):
            for k in range(j + 1, m):
                if i not in (j, k):
                    edges.append((('b', i, j), ('b', i, k)))
    for u, v in edges:
        i, j = idx[u], idx[v]
        assert i != j and a[i][j] == 0
        a[i][i] += 1; a[j][j] += 1
        a[i][j] = -1; a[j][i] = -1
    assert len(names) == m * m + 1
    assert all(a[i][i] == m for i in range(n))
    return a


def det_bareiss(matrix):
    n = len(matrix)
    a = [row[:] for row in matrix]
    last = 1
    sign = 1
    for k in range(n - 1):
        p = next((r for r in range(k, n) if a[r][k]), None)
        if p is None:
            return 0
        if p != k:
            a[k], a[p] = a[p], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % last == 0
                a[i][j] = numerator // last
            a[i][k] = 0
        last = pivot
    return sign * a[n-1][n-1]


def predicted_characteristic(m, t):
    q = t*t - (2*m + 1)*t + m*m + 1
    c = t**3 - (2*m + 3)*t*t + (m*m + 4*m + 3)*t - (m*m + 2*m + 2)
    return t * q * c**(m-1) * (t-m)**(m*(m-3)//2) * (t-m-2)**((m-1)*(m-2)//2)


def predicted_trees(m):
    assert m >= 3
    return m**(m*(m-3)//2) * (m+2)**((m-1)*(m-2)//2) * (m*m + 2*m + 2)**(m-1)


def run():
    assert det_bareiss([[0]]) == 0
    assert det_bareiss([[3]]) == 3
    assert det_bareiss([[2, 1], [1, 2]]) == 3
    for m in range(3, 7):
        L = graph_laplacian(m)
        trees = det_bareiss([row[:-1] for row in L[:-1]])
        assert trees == predicted_trees(m), (m, trees, predicted_trees(m))
        print('TREE_OK', m, len(L), trees)
    for m in (3, 4):
        L = graph_laplacian(m)
        n = len(L)
        for t in range(n + 1):
            M = [[(t if i == j else 0) - L[i][j] for j in range(n)] for i in range(n)]
            assert det_bareiss(M) == predicted_characteristic(m, t), (m, t)
        print('CHARPOLY_OK', m, 'checked_at', n+1, 'distinct_integers')
    # A degree-n monic polynomial is determined by n+1 values.
    print('ALL_EXACT_CHECKS_OK')

if __name__ == '__main__':
    run()
