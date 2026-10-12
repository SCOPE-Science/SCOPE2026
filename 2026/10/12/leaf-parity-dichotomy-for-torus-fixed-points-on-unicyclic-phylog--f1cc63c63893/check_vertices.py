#!/usr/bin/env python3
"""Independent bounded vertex enumeration for tripod-fibre phylogenetic polytopes.

Requires numpy and sympy. Integer inequalities and exact rational reconstruction
are checked independently of the numerical solution of candidate active systems.
This is regression evidence for three finite graphs, not a proof for all graphs.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations

import numpy as np
from sympy import Matrix


def facet_system(tripods, num_edges):
    rows, bounds = [], []
    for tripod in tripods:
        for coefficients in ((-1, -1, 1), (-1, 1, -1),
                             (1, -1, -1), (1, 1, 1)):
            row = [0] * num_edges
            for edge, coeff in zip(tripod, coefficients):
                row[edge] += coeff
            rows.append(row)
            bounds.append(2 if coefficients == (1, 1, 1) else 0)
    return rows, bounds


def enumerate_vertices(tripods, num_edges):
    rows, bounds = facet_system(tripods, num_edges)
    aa = np.array(rows, dtype=float)
    bb = np.array(bounds, dtype=float)
    found = set()
    for indices in combinations(range(len(rows)), num_edges):
        mat = aa[list(indices), :]
        if abs(np.linalg.det(mat)) < 1.e-8:
            continue
        x = np.linalg.solve(mat, bb[list(indices)])
        if np.any(aa @ x > bb + 1.e-8):
            continue
        rational = tuple(Fraction(float(z)).limit_denominator(100) for z in x)
        # Check all inequalities exactly, not relying on tolerance.
        if not all(sum(c * v for c, v in zip(row, rational)) <= b
                   for row, b in zip(rows, bounds)):
            continue
        active = [row for row, b in zip(rows, bounds)
                  if sum(c * v for c, v in zip(row, rational)) == b]
        assert Matrix(active).rank() == num_edges
        found.add(rational)
    return found


def run_case(name, tripods, num_edges, cycle_edges, leaf_edges):
    n = len(leaf_edges)
    assert num_edges == 2 * n == 2 * len(tripods)
    found = enumerate_vertices(tripods, num_edges)
    integral = {x for x in found if all(t.denominator == 1 for t in x)}
    fractional = found - integral
    assert len(integral) == 2**n
    assert len(fractional) == 2**(n - 1)
    assert all(all(t in (0, 1) for t in x) for x in integral)
    for x in fractional:
        assert all(x[e] == Fraction(1, 2) for e in cycle_edges)
        assert all(x[e] in (0, 1) for e in range(num_edges) if e not in cycle_edges)
        assert sum(int(x[e]) for e in leaf_edges) % 2 == 1
    for x in integral:
        assert sum(int(x[e]) for e in leaf_edges) % 2 == 0
    print(f'{name}: n={n}, total={len(found)}, integral={len(integral)}, '
          f'half-cycle={len(fractional)}: PASS')


if __name__ == '__main__':
    run_case('three-cycle', [(0, 2, 3), (0, 1, 4), (1, 2, 5)],
             6, (0, 1, 2), (3, 4, 5))
    run_case('four-cycle', [(0, 3, 4), (0, 1, 5), (1, 2, 6), (2, 3, 7)],
             8, (0, 1, 2, 3), (4, 5, 6, 7))
    run_case('three-cycle-with-branch',
             [(0, 2, 3), (0, 1, 4), (1, 2, 5), (3, 6, 7)],
             8, (0, 1, 2), (4, 5, 6, 7))
