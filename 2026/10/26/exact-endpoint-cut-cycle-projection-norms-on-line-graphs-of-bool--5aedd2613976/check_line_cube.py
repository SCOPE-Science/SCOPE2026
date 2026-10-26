#!/usr/bin/env python3
"""Exact-rational checks for cut/cycle projection norms on cube line graphs.

Uses only the Python standard library. Run with Python 3.10+:
    python check_line_cube.py
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def predicted(n):
    assert n >= 3
    count_vertices = n * (1 << (n - 1))
    cut = (Q(n * n + 11 * n - 14, 4 * n)
           - Q(2, n * (n - 1)) * (1 - Q(n, 1 << (n - 1))))
    cycle = cut + 1 - Q(2, n - 1) * (1 - Q(1, count_vertices))
    return cut, cycle


def green_level(m, j):
    """Integral of p**j*(1-p)**(m-j), p from 0 to 1/2."""
    upper_tail = sum(comb(m + 1, r) for r in range(j + 1, m + 2))
    return Q(upper_tail, (m + 1) * comb(m, j) * (1 << (m + 1)))


def binomial_current_formula(n):
    m = n - 2
    h = [green_level(m, j) for j in range(m + 1)]
    assert all(h[j] > h[j + 1] for j in range(m))
    assert h[1] < 1
    sums = [Q(0)] * 4
    for j in range(m + 1):
        w = comb(m, j)
        hlow = h[j - 1] if j else Q(0)
        hhigh = h[j + 1] if j < m else Q(0)
        sums[0] += w * h[j]
        sums[1] += w * j * hlow
        sums[2] += w * (m-j) * hhigh
        sums[3] += w * j * (m-j) * (hlow - hhigh)
    assert sums == [Q(1,2), Q(3*m,8), Q(m,8), Q(m*(m-1),4)]
    assert h[1] == Q(1 - Q(n, 1 << (n - 1)), (n - 1)*(n - 2))
    base = 4 * (n-1) * sums[0] + 2 * (2*(sums[1]+sums[2]) + sums[3])
    specials = 2*(n-1) + 2*(1 + m*(1 - 2*h[1]))
    return (base + specials) / (2*n)


def cube_line_graph(n):
    e_cube = [(v, v ^ (1 << j)) for v in range(1 << n)
              for j in range(n) if not (v & (1 << j))]
    incident = [[] for _ in range(1 << n)]
    for i,(a,b) in enumerate(e_cube):
        incident[a].append(i)
        incident[b].append(i)
    e_line = []
    for around in incident:
        e_line.extend(combinations(around, 2))
    return e_cube, e_line


def grounded_potential(n_vertices, e_line, source):
    """Independent exact Gaussian solve of grounded line-graph Laplacian."""
    size = n_vertices - 1
    matrix = [[0] * size for _ in range(size)]
    for a,b in e_line:
        if a < size: matrix[a][a] += 1
        if b < size: matrix[b][b] += 1
        if a < size and b < size:
            matrix[a][b] -= 1
            matrix[b][a] -= 1
    rhs = [0] * size
    a,b = source
    if a < size: rhs[a] += 1
    if b < size: rhs[b] -= 1
    for i in range(size):
        pivot = matrix[i][i]
        assert pivot > 0
        for row in range(i + 1, size):
            off = matrix[row][i]
            if off:
                multiplier = Q(off, pivot)
                matrix[row][i] = 0
                for col in range(i + 1, size):
                    matrix[row][col] -= multiplier * matrix[i][col]
                rhs[row] -= multiplier * rhs[i]
    potential = [Q(0)] * size
    for i in range(size - 1, -1, -1):
        potential[i] = (rhs[i] - sum(matrix[i][j] * potential[j]
                                        for j in range(i+1, size))) / matrix[i][i]
    return potential + [Q(0)]


def direct_graph_check(n, columns):
    cube, line = cube_line_graph(n)
    vertices = len(cube)
    assert vertices == n * (1 << (n - 1))
    assert len(line) == vertices * (n - 1)
    predicted_cut, predicted_cycle = predicted(n)
    expected_diagonal = Q(vertices - 1, len(line))
    for edge in line[:columns]:
        potential = grounded_potential(vertices, line, edge)
        currents = [potential[a]-potential[b] for a,b in line]
        cut = sum(abs(j) for j in currents)
        direct_diagonal = potential[edge[0]]-potential[edge[1]]
        cycle = cut + 1 - 2*direct_diagonal
        assert cut == predicted_cut, (n,edge,cut,predicted_cut)
        assert cycle == predicted_cycle, (n,edge,cycle,predicted_cycle)
        assert direct_diagonal == expected_diagonal
    return len(line), columns


def main():
    for n in range(3, 41):
        assert binomial_current_formula(n) == predicted(n)[0]
    checked_graphs = 0
    checked_columns = 0
    total_line_edges = 0
    for n, columns in [(3, 24), (4, 96), (5, 3), (6, 1)]:
        m, count = direct_graph_check(n, columns)
        total_line_edges += m
        checked_columns += count
        checked_graphs += 1
    print('LINE_HYPERCUBE_HODGE_EXACT_OK'
          f' integral_dimensions=38 grounded_graphs={checked_graphs}'
          f' grounded_columns={checked_columns} line_edges={total_line_edges}')

if __name__ == '__main__':
    main()
