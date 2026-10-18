#!/usr/bin/env python3
"""Finite exact checks for leader controllability on bouquets of unit cycles.

All controllability ranks are calculated in a prime finite field. A full
modular Kalman rank is an exact certificate of full rank over the rationals
for the tested integral matrices, not an infinite-family proof.
"""
from itertools import combinations, product

P = 1000000007


def bouquet(lengths):
    if not lengths or min(lengths) < 3:
        raise ValueError('cycle lengths must be >= 3')
    edges = set()
    groups = []
    next_vertex = 1
    for length in lengths:
        group = tuple(range(next_vertex, next_vertex + length - 1))
        next_vertex += length - 1
        groups.append(group)
        vertices = (0,) + group
        for a, b in zip(vertices, vertices[1:] + (0,)):
            edges.add(tuple(sorted((a, b))))
    n = next_vertex
    adjacency = [set() for _ in range(n)]
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    laplacian = []
    for i in range(n):
        laplacian.append([len(adjacency[i]) if i == j else (-1 if j in adjacency[i] else 0)
                          for j in range(n)])
    return adjacency, laplacian, groups


def rank_mod(A):
    if not A:
        return 0
    rows = [list(map(lambda a: a % P, row)) for row in A]
    ncols = len(rows[0]); pivot_row = 0
    for j in range(ncols):
        i = next((q for q in range(pivot_row, len(rows)) if rows[q][j]), None)
        if i is None:
            continue
        rows[pivot_row], rows[i] = rows[i], rows[pivot_row]
        inv = pow(rows[pivot_row][j], P - 2, P)
        pivot = [x * inv % P for x in rows[pivot_row]]
        for q in range(pivot_row + 1, len(rows)):
            factor = rows[q][j]
            if factor:
                rows[q] = [(x - factor * y) % P for x, y in zip(rows[q], pivot)]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def kalman_rank(L, leaders):
    n = len(L)
    columns = [[int(i == leader) for i in range(n)] for leader in leaders]
    all_columns = []
    for _ in range(n):
        all_columns.extend(columns)
        columns = [[sum(a * b for a, b in zip(row, col)) % P for row in L]
                   for col in columns]
    return rank_mod([[col[i] for col in all_columns] for i in range(n)])


def zero_forces(adjacency, initially_blue):
    blue = set(initially_blue)
    while True:
        new = set()
        for vertex in blue:
            white_neighbors = adjacency[vertex] - blue
            if len(white_neighbors) == 1:
                new.update(white_neighbors)
        if not new:
            break
        blue.update(new)
    return len(blue) == len(adjacency)


def run():
    checks = 0
    families = [(a, b) for a in range(3, 11) for b in range(a, 11)]
    families += [(a, b, c) for a in range(3, 6) for b in range(a, 6)
                 for c in range(b, 6)]
    families += [(3, 3, 3, 3), (3, 4, 5, 6), (3, 4, 5, 7), (3, 3, 4, 5, 6)]
    for lengths in families:
        adjacency, L, petals = bouquet(lengths)
        k = len(petals)
        assert kalman_rank(L, [group[0] for group in petals]) == len(L), lengths
        checks += 1
        assert zero_forces(adjacency, [0] + [group[0] for group in petals]), lengths
        checks += 1
        for chosen in combinations(range(len(L)), k - 1):
            assert not zero_forces(adjacency, chosen), (lengths, chosen)
            checks += 1
        # Explicit no-petal and no-hub obstructions for an arbitrary sensor set.
        for omitted in range(k):
            leaders = [0] + [petals[j][0] for j in range(k) if j != omitted]
            assert kalman_rank(L, leaders) < len(L), (lengths, omitted)
            checks += 1
    print('PASS: {} exact modular-rank/forcing checks across {} bouquets'.format(checks, len(families)))

if __name__ == '__main__':
    run()
