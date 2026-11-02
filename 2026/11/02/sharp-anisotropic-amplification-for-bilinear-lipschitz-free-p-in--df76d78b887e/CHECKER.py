"""Finite spanning-tree checks for weighted rectangular four-point p-free interpolation.
This is a diagnostic, not a replacement for the general analytic argument.
Run: python3 CHECKER.py
"""
from itertools import combinations

VERTICES = ((0, 0), (0, 1), (1, 0), (1, 1))
EDGES = tuple(combinations(range(4), 2))


def connected(edge_indices):
    reach = {0}
    for _ in range(4):
        for e in edge_indices:
            i, j = EDGES[e]
            if i in reach or j in reach:
                reach.update((i, j))
    return len(reach) == 4


TREES = tuple(t for t in combinations(range(6), 3) if connected(t))
assert len(TREES) == 16


def flow_on_edge(tree, edge_idx, masses):
    i, j = EDGES[edge_idx]
    component = {i}
    for _ in range(4):
        for e in tree:
            if e == edge_idx:
                continue
            u, v = EDGES[e]
            if u in component or v in component:
                component.update((u, v))
    assert j not in component
    return sum(masses[k] for k in component)


def tree_norm(masses, a, b, p):
    assert abs(sum(masses)) < 1e-12
    costs = []
    for t in TREES:
        costs.append(sum((abs(flow_on_edge(t, e, masses)) *
                          (a * abs(VERTICES[EDGES[e][0]][0] - VERTICES[EDGES[e][1]][0])
                           + b * abs(VERTICES[EDGES[e][0]][1] - VERTICES[EDGES[e][1]][1]))) ** p
                         for e in t))
    return min(costs) ** (1 / p)


def tangent_mass(B):
    return (-1 / 3 - 1 / (6 * B), -1 / 3 + 1 / (6 * B),
             1 / 3 - 1 / (6 * B),  1 / 3 + 1 / (6 * B))


if __name__ == '__main__':
    for p in (0.5, 0.75, 1.0):
        bound = 3 ** (1 / p - 1)
        print('p =', p, 'universal bound =', round(bound, 9))
        for B in (1, 2, 4, 8, 32, 128, 512):
            value = tree_norm(tangent_mass(B), 1, B, p)
            assert value <= bound + 1e-9
            print('  B =', B, 'tangent norm =', round(value, 9))
        assert abs(tree_norm(tangent_mass(16384), 1, 16384, p) - bound) < 0.01
    print('All 16-tree diagnostic checks passed.')
