"""Exact certificate for the edgewise sensitivity of metric-nearness projection.
Requires only Python's standard library. All matrix arithmetic uses fractions.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict


def row_basis(rows, width):
    a = [list(map(F, row)) for row in rows]
    pivot_row = 0
    for col in range(width):
        pivot = next((i for i in range(pivot_row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        c = a[pivot_row][col]
        a[pivot_row] = [z / c for z in a[pivot_row]]
        for i in range(len(a)):
            if i != pivot_row and a[i][col]:
                fac = a[i][col]
                a[i] = [u - fac * v for u, v in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return tuple(tuple(row) for row in a[:pivot_row])


def inverse(a):
    n = len(a)
    t = [list(row) + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if t[i][col]), None)
        assert pivot is not None
        t[pivot], t[col] = t[col], t[pivot]
        c = t[col][col]
        t[col] = [v / c for v in t[col]]
        for i in range(n):
            if i == col:
                continue
            c = t[i][col]
            if c:
                t[i] = [u - c * v for u, v in zip(t[i], t[col])]
    return [row[n:] for row in t]


def projection(b, width):
    rank = len(b)
    if not rank:
        return tuple(tuple(F(i == j) for j in range(width)) for i in range(width))
    gram = [[sum(b[i][k] * b[j][k] for k in range(width))
             for j in range(rank)] for i in range(rank)]
    gi = inverse(gram)
    return tuple(tuple(F(i == j) - sum(
        b[s][i] * gi[s][t] * b[t][j]
        for s in range(rank) for t in range(rank))
        for j in range(width)) for i in range(width))


def triangle_normals(n):
    edges = tuple(combinations(range(n), 2))
    index = {edge: i for i, edge in enumerate(edges)}
    normals = []
    for x, y, z in combinations(range(n), 3):
        for middle, u, v in ((x, y, z), (y, x, z), (z, x, y)):
            a = [0] * len(edges)
            a[index[tuple(sorted((u, middle)))]] += 1
            a[index[tuple(sorted((v, middle)))]] += 1
            a[index[tuple(sorted((u, v)))]] -= 1
            normals.append(tuple(a))
    return edges, tuple(normals)


def verify_all(n):
    edges, normals = triangle_normals(n)
    width, constraints = len(edges), len(normals)
    cache = {}
    rank_subsets = defaultdict(int)
    rank_span_counts = defaultdict(int)
    rank_maximum = defaultdict(F)
    for subset in range(1 << constraints):
        b = row_basis([normal for i, normal in enumerate(normals)
                       if (subset >> i) & 1], width)
        rank = len(b)
        rank_subsets[rank] += 1
        if b not in cache:
            rank_span_counts[rank] += 1
            q = projection(b, width)
            for i in range(width):
                for j in range(width):
                    assert q[i][j] == q[j][i]
                    assert sum(q[i][k] * q[k][j] for k in range(width)) == q[i][j]
            assert all(sum(normal[i] * q[i][j] for i in range(width)) == 0
                       for normal in b for j in range(width))
            value = max(sum(abs(v) for v in row) for row in q)
            cache[b] = value
            rank_maximum[rank] = max(rank_maximum[rank], value)
        assert cache[b] <= (F(4, 3) if n == 3 else F(8, 5))
    summary = tuple((r, rank_subsets[r], rank_span_counts[r], str(rank_maximum[r]))
                    for r in sorted(rank_subsets))
    bound = max(cache.values())
    print("computed rank profile",n,summary,flush=True)
    if n == 3:
        assert summary == ((0, 1, 1, '1'), (1, 3, 3, '4/3'),
                           (2, 3, 3, '1'), (3, 1, 1, '0'))
        assert bound == F(4, 3)
    if n == 4:
        assert summary == ((0, 1, 1, '1'), (1, 12, 12, '4/3'),
                           (2, 66, 66, '3/2'), (3, 238, 166, '8/5'),
                           (4, 639, 171, '3/2'), (5, 1345, 49, '10/7'),
                           (6, 1795, 1, '0'))
        assert bound == F(8, 5)
    print(f'{n} vertices: {1 << constraints} complete subsets; '
          f'{len(cache)} distinct spans; max {bound}.')
    print('rank, subsets, spans, max-row-sum:', summary)
    return edges, normals


def witness(normals):
    b = tuple(tuple(map(F, normals[i])) for i in (0, 3, 6))
    q = projection(b, 6)
    x = tuple(map(F, ('1/2', '1/2', '1/2', '1', '1', '1')))
    v = tuple(map(F, (1, 1, -1, 1, 1, 1)))
    h = F(1, 1000)
    lam = F(1, 10)
    y = tuple(x[j] - lam * sum(b[i][j] for i in range(3)) for j in range(6))
    qv = tuple(sum(q[i][j] * v[j] for j in range(6)) for i in range(6))
    z = tuple(x[i] + h * qv[i] for i in range(6))
    y2 = tuple(y[i] + h * v[i] for i in range(6))
    assert qv == (F(4, 5), F(4, 5), F(-1, 5), F(8, 5), F(3, 5), F(3, 5))
    assert all(u > 0 for u in y + y2)
    assert all(sum(row[j] * x[j] for j in range(6)) >= 0 for row in normals)
    assert all(sum(row[j] * z[j] for j in range(6)) >= 0 for row in normals)
    assert all(sum(row[j] * x[j] for j in range(6)) == 0 for row in b)
    assert all(sum(row[j] * z[j] for j in range(6)) == 0 for row in b)
    # KKT multipliers of the second projection, in the active normal basis.
    bg = [[sum(b[i][j] * b[k][j] for j in range(6)) for k in range(3)]
          for i in range(3)]
    bg_inv = inverse(bg)
    bv = [sum(b[i][j] * v[j] for j in range(6)) for i in range(3)]
    lam2 = [lam - h * sum(bg_inv[i][k] * bv[k] for k in range(3)) for i in range(3)]
    assert lam2 == [F(497, 5000), F(251, 2500), F(251, 2500)]
    assert all(t > 0 for t in lam2)
    assert all(y2[j] - z[j] == -sum(lam2[i] * b[i][j] for i in range(3))
               for j in range(6))
    assert all(y[j] - x[j] == -sum(lam * b[i][j] for i in range(3))
               for j in range(6))
    assert max(abs(z[j] - x[j]) for j in range(6)) == h * F(8, 5)
    assert max(abs(y2[j] - y[j]) for j in range(6)) == h
    print('Two strictly positive inputs y,y+hv:', y, y2)
    print('Exact fitted outputs x,z:', x, z)
    print('Sharp quotient:', F(8, 5))

if __name__ == '__main__':
    verify_all(3)
    e, a = verify_all(4)
    assert e == ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
    witness(a)
    print('ALL EXACT CHECKS PASSED')
