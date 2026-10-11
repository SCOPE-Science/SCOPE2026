#!/usr/bin/env python3
"""Exact finite checks of the equivariant graph Morse-complex character theorem.

Only Python standard-library modules are used. The general proof is symbolic;
finite enumeration here checks independent instances, not all graph orders.
"""
from fractions import Fraction
from itertools import combinations, permutations, product


def vertex_orbits(g):
    seen, out = set(), []
    for a in range(len(g)):
        if a in seen:
            continue
        O, v = [], a
        while v not in seen:
            seen.add(v)
            O.append(v)
            v = g[v]
        assert v == a
        out.append(O)
    return out


def det_integer(matrix):
    n = len(matrix)
    M = [[Fraction(x) for x in row] for row in matrix]
    value = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if M[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            M[j], M[pivot] = M[pivot], M[j]
            value *= -1
        factor = M[j][j]
        value *= factor
        for i in range(j + 1, n):
            multiplier = M[i][j] / factor
            for k in range(j + 1, n):
                M[i][k] -= multiplier * M[j][k]
            M[i][j] = 0
    assert value.denominator == 1
    return value.numerator


def coefficient_trace(n, edges, g):
    neighbours = [[] for _ in range(n)]
    for u, v in edges:
        neighbours[u].append(v)
        neighbours[v].append(u)
    coefficients = [0] * (n + 1)
    for choice in product(*[[-1] + ns for ns in neighbours]):
        arrows = {(u, v) for u, v in enumerate(choice) if v >= 0}
        if {(g[u], g[v]) for u, v in arrows} != arrows:
            continue
        cycle = False
        for origin in range(n):
            seen, v = set(), origin
            while v >= 0 and v not in seen:
                seen.add(v)
                v = choice[v]
            if v >= 0:
                cycle = True
                break
        if cycle:
            continue
        remaining, sign = set(arrows), 1
        while remaining:
            first = next(iter(remaining))
            v = first
            length = 0
            while v in remaining:
                remaining.remove(v)
                length += 1
                v = (g[v[0]], g[v[1]])
            assert v == first
            if length % 2 == 0:
                sign = -sign
        coefficients[len(arrows)] += sign
    return coefficients


def orbit_laplacian(n, edges, g):
    orbits = vertex_orbits(g)
    edge_set = {frozenset(e) for e in edges}
    m = len(orbits)
    weight = [[0] * m for _ in range(m)]
    for i, A in enumerate(orbits):
        for j, B in enumerate(orbits):
            if i == j or len(A) % len(B):
                continue
            weight[i][j] = sum(frozenset((A[0], v)) in edge_set for v in B)
    lap = [[sum(weight[i]) if i == j else -weight[i][j]
            for j in range(m)] for i in range(m)]
    return orbits, lap


def evaluate_determinant(orbits, lap, t):
    size = len(orbits)
    D = [(-1) ** (len(O) - 1) * t ** len(O) for O in orbits]
    return det_integer([[(1 if i == j else 0) + D[i] * lap[i][j]
                         for j in range(size)] for i in range(size)])


def check(n, edges, g):
    E = {frozenset(e) for e in edges}
    assert {frozenset((g[u], g[v])) for u, v in edges} == E
    coefficients = coefficient_trace(n, edges, g)
    orbits, lap = orbit_laplacian(n, edges, g)
    # Both sides have degree <= n, so equality at n+1 distinct arguments
    # verifies the complete finite-instance polynomial identity exactly.
    for t in range(n + 1):
        lhs = sum(c * (t ** i) for i, c in enumerate(coefficients))
        rhs = evaluate_determinant(orbits, lap, t)
        assert lhs == rhs, (n, edges, g, t, coefficients, lhs, rhs)
    lefschetz = -sum(c * (-1) ** i for i, c in enumerate(coefficients))
    lhs = -evaluate_determinant(orbits, lap, -1)
    assert lefschetz == lhs


def complete_cycle_product(n, g):
    counts = {}
    for O in vertex_orbits(g):
        counts[len(O)] = counts.get(len(O), 0) + 1
    ans = 1
    for d, r in counts.items():
        s = sum(e * r_e for e, r_e in counts.items() if e < d and d % e == 0)
        ans *= (1 - s) * (1 - s - d * r) ** (r - 1)
    return -ans


def main():
    total = 0
    for n in range(1, 5):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = [e for k, e in enumerate(possible) if mask & (1 << k)]
            E = {frozenset(e) for e in edges}
            for g in permutations(range(n)):
                if {frozenset((g[u], g[v])) for u, v in edges} != E:
                    continue
                check(n, edges, g)
                total += 1
    assert total == 293
    for n in range(2, 7):
        edges = list(combinations(range(n), 2))
        for g in permutations(range(n)):
            orbits, lap = orbit_laplacian(n, edges, g)
            assert -evaluate_determinant(orbits, lap, -1) == complete_cycle_product(n, g)
    examples = [
        (6, [(i, j) for i in range(3) for j in range(3, 6)],
         (3, 4, 5, 0, 1, 2)),
        (6, [(i, j) for i in range(3) for j in range(3, 6)],
         (1, 2, 0, 4, 5, 3)),
        (6, [(i, (i + 1) % 6) for i in range(6)],
         (3, 4, 5, 0, 1, 2)),
    ]
    for n, edges, g in examples:
        check(n, edges, g)
    print('VERIFY_OK: 293 exhaustive graph-automorphism cases through four')
    print('VERIFY_OK: complete-graph cycle product, every permutation on 2..6')
    print('VERIFY_OK: three six-vertex nontrivial actions with graded traces')

if __name__ == '__main__':
    main()
