"""Exact arithmetic verification of rectangular fixed-cardinality assignment ellipsoids.

Run with standard Python 3: python verify.py.  This is finite corroboration,
not a replacement for the general determinant and symmetry proof.
"""
from fractions import Fraction as F


def solution(m, n, k):
    assert 2 <= m < n and 1 <= k < m
    a = F(m - 1, m * n)
    b = F(n - 1, m * n)
    c = F((m - 1) * (n - 1), m * n)
    t = F(k, m * n)
    u = F((m - k) ** 2, m * n * (m - 1))
    v = F((n - k) ** 2, m * n * (n - 1))
    q0 = t * t / (a + b + c)
    if q0 <= u:
        q = q0
    else:
        q1 = (t * t - a * u) / (b + c)
        if q1 <= v:
            q = q1
        else:
            q = (t * t - a * u - b * v) / c
    alpha, beta = min(q, u), min(q, v)
    assert alpha > 0 and beta > 0 and q > 0
    assert a * alpha + b * beta + c * q == t * t
    assert alpha <= u and beta <= v
    assert alpha == min(u, q) and beta == min(v, q)
    return alpha, beta, q, u, v, t


def projections(y):
    m, n = len(y), len(y[0])
    row = [sum(yi, F(0)) / n for yi in y]
    col = [sum(y[i][j] for i in range(m)) / m for j in range(n)]
    avg = sum((sum(yi, F(0)) for yi in y), F(0)) / (m * n)
    return (
        [[row[i] - avg for j in range(n)] for i in range(m)],
        [[col[j] - avg for j in range(n)] for i in range(m)],
        [[y[i][j] - row[i] - col[j] + avg for j in range(n)] for i in range(m)],
    )


def squared_norm(z):
    return sum((q * q for row in z for q in row), F(0))


def add(a, b):
    return [[u + v for u, v in zip(rowa, rowb)] for rowa, rowb in zip(a, b)]


def scale(a, c):
    return [[c * x for x in row] for row in a]


def dot(a, b):
    return sum((a[i][j] * b[i][j] for i in range(len(a)) for j in range(len(a[0]))), F(0))


def main():
    cases = 0
    regimes = set()
    facets = 0
    contact_points = 0
    for m in range(2, 35):
        for n in range(m + 1, min(m + 17, 45)):
            for k in range(1, m):
                alpha, beta, gamma, u, v, t = solution(m, n, k)
                regime = ('sphere' if gamma < u else
                          'threshold' if gamma == u or gamma == v else
                          'both' if gamma > v else 'row_only')
                regimes.add(regime)
                cases += 1
                # All equality regimes are covered by the min equation above.
                if m <= 7 and n <= 9:
                    c = [[t] * n for _ in range(m)]
                    normals = []
                    for i in range(m):
                        for j in range(n):
                            y = [[F(int((r, s) == (i, j))) - F(1, m * n)
                                  for s in range(n)] for r in range(m)]
                            normals.append((y, t, -1, True))
                    for i in range(m):
                        y = [[F(int(r == i)) - F(1, m)
                              for s in range(n)] for r in range(m)]
                        normals.append((y, F(m-k, m), +1, alpha == u))
                    for j in range(n):
                        y = [[F(int(s == j)) - F(1, n)
                              for s in range(n)] for r in range(m)]
                        normals.append((y, F(n-k, n), +1, beta == v))
                    for y, slack, sign, contact in normals:
                        row_p, col_p, int_p = projections(y)
                        assert sum((sum(row, F(0)) for row in y), F(0)) == 0
                        assert dot(row_p, col_p) == 0
                        assert dot(row_p, int_p) == 0
                        assert dot(col_p, int_p) == 0
                        variance = alpha * squared_norm(row_p) + beta * squared_norm(col_p) + gamma * squared_norm(int_p)
                        assert variance <= slack * slack
                        assert (variance == slack * slack) == contact
                        facets += 1
                        if contact:
                            sigmay = add(add(scale(row_p, alpha), scale(col_p, beta)), scale(int_p, gamma))
                            x = add(c, scale(sigmay, F(sign, 1) / slack))
                            assert sum((sum(row, F(0)) for row in x), F(0)) == k
                            assert min(z for row in x for z in row) >= 0
                            assert all(sum(row, F(0)) <= 1 for row in x)
                            assert all(sum(x[r][s] for r in range(m)) <= 1 for s in range(n))
                            assert dot(y, x) - dot(y, c) == sign * slack
                            contact_points += 1
    assert {'sphere', 'row_only', 'both'} <= regimes
    assert solution(4, 5, 3)[:3] == (F(1, 60), F(1, 40), F(1, 40))
    assert solution(7, 8, 6)[:3] == (F(1, 336), F(1, 98), F(31, 2352))
    print('PASS:', cases, 'exact water-filling instances;', facets,
          'independently projected facet inequalities;', contact_points,
          'exact contact points in the polytope;', sorted(regimes))


if __name__ == '__main__':
    main()
