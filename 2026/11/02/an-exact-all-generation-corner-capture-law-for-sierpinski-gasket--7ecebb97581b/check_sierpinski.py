#!/usr/bin/env python3
"""Independent finite-graph checks for a Sierpinski-gasket quantum-capture theorem.

Standard-library only.  The all-generation result follows from the analytical
boundary-resolvent proof; modular experiments here are finite cross-checks.
"""
from fractions import Fraction


def gasket(level):
    scale = 1 << level
    edges = set()

    def triangle(a, b, c, depth):
        if depth == 0:
            edges.update(tuple(sorted((u, v))) for u, v in ((a, b), (b, c), (c, a)))
            return
        ab = tuple((a[k] + b[k]) // 2 for k in (0, 1))
        ac = tuple((a[k] + c[k]) // 2 for k in (0, 1))
        bc = tuple((b[k] + c[k]) // 2 for k in (0, 1))
        triangle(a, ab, ac, depth - 1)
        triangle(ab, b, bc, depth - 1)
        triangle(ac, bc, c, depth - 1)

    triangle((0, 0), (scale, 0), (0, scale), level)
    vertices = sorted({v for edge in edges for v in edge})
    position = {v: i for i, v in enumerate(vertices)}
    neighbors = [[] for _ in vertices]
    for u, v in edges:
        i, j = position[u], position[v]
        neighbors[i].append(j)
        neighbors[j].append(i)
    corners = [position[(0, 0)], position[(scale, 0)], position[(0, scale)]]
    return vertices, neighbors, corners


def block_krylov_rank(neighbors, sources, prime):
    dimension = len(neighbors)
    pivots = {}
    columns = []
    for i in sources:
        v = [0] * dimension
        v[i] = 1
        columns.append(v)
    for _ in range(dimension + 1):
        grew = False
        for column in columns:
            residual = column[:]
            while True:
                pivot = next((i for i, val in enumerate(residual) if val), None)
                if pivot is None:
                    break
                if pivot not in pivots:
                    inverse = pow(residual[pivot], -1, prime)
                    pivots[pivot] = [(value * inverse) % prime for value in residual]
                    grew = True
                    break
                factor = residual[pivot]
                base = pivots[pivot]
                residual = [(a - factor * b) % prime for a, b in zip(residual, base)]
        if not grew or len(pivots) == dimension:
            return len(pivots)
        columns = [[sum(column[j] for j in neighbors[i]) % prime
                    for i in range(dimension)] for column in columns]
    raise AssertionError('Cayley-Hamilton stopping condition violated')


def solve(matrix, right):
    # Exact rational Gauss-Jordan, used only for N<=15.
    n = len(matrix)
    mat = [[Fraction(value) for value in row] + [Fraction(right[i])]
           for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if mat[i][col])
        mat[pivot], mat[col] = mat[col], mat[pivot]
        factor = mat[col][col]
        mat[col] = [v / factor for v in mat[col]]
        for row in range(n):
            if row != col and mat[row][col]:
                factor = mat[row][col]
                mat[row] = [a - factor * b for a, b in zip(mat[row], mat[col])]
    return [mat[i][-1] for i in range(n)]


def sector_recurrence(level, energy):
    x = Fraction(energy)
    def k(sector, depth, z):
        if depth == 0:
            return z - 2 if sector == 's' else z + 1
        y = z * (z - 3)
        return ((z + 2) * k(sector, depth - 1, y) + 2*z) / ((z + 1)*(z - 2))
    return k('s', level, x), k('t', level, x)


def check_sector_resolvent(level):
    vertices, adj, corners = gasket(level)
    n = len(vertices)
    z = 10
    matrix = [[(z if i == j else 0) - int(j in adj[i])
               for j in range(n)] for i in range(n)]
    rhs = [int(i == corners[0]) for i in range(n)]
    solution = solve(matrix, rhs)
    g_diag = solution[corners[0]]
    g_offdiag = solution[corners[1]]
    s, t = sector_recurrence(level, z)
    expected_diag = (Fraction(1,s) + 2*Fraction(1,t))/3
    expected_offdiag = (Fraction(1,s) - Fraction(1,t))/3
    assert g_diag == expected_diag and g_offdiag == expected_offdiag, (level,g_diag,expected_diag)
    print('resolvent',level,'exact rational PASS')


def main():
    for level in range(6):
        vertices, adj, corners = gasket(level)
        n = len(vertices)
        expected_vertices = (3**(level+1)+3)//2
        expected_edges = 3**(level+1)
        expected_rank = 3 if level == 0 else 5*2**(level-1)+1
        assert n == expected_vertices
        assert sum(map(len, adj))//2 == expected_edges
        assert all(len(adj[c]) == 2 for c in corners)
        assert all(len(adj[v]) == 4 for v in range(n) if v not in corners)
        for prime in (1000033, 1000037):
            rank = block_krylov_rank(adj, corners, prime)
            assert rank == expected_rank, (level,prime,rank,expected_rank)
        print('gasket',level,'vertices',n,'corner-active-rank',expected_rank,'two modular checks PASS')
    for level in range(3):
        check_sector_resolvent(level)
    print('ALL FINITE CROSS-CHECKS PASS')

if __name__ == '__main__':
    main()
