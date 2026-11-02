#!/usr/bin/env python3
"""Exact finite checks for two-subset Kneser metric L1 distortion.

The all-n argument is in RESULT.md. These checks are independent finite
reconstructions of graph distances, incidence identities, orbit cut counts,
and the test vectors at and above the critical spectral threshold.
"""
from fractions import Fraction
from itertools import combinations, permutations
from collections import deque
from math import comb

checks = 0

def test(statement, message):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(message)


def graph_data(n):
    vertices = list(combinations(range(n), 2))
    edges = {v: [w for w in vertices if not set(v) & set(w)] for v in vertices}
    return vertices, edges


def quadratic(n, vertices, x, q):
    z = Fraction(0)
    for i, a in enumerate(vertices):
        for j, b in enumerate(vertices):
            if i == j:
                continue
            value = q if set(a) & set(b) else Fraction(1)
            z += x[i] * x[j] * value
    return z


def run_one(n):
    vertices, adj = graph_data(n)
    N = comb(n, 2)
    vindex = {v: i for i, v in enumerate(vertices)}
    test(len(vertices) == N, f'pair number {n}')
    for v in vertices:
        distances = {v: 0}
        queue = deque([v])
        while queue:
            x = queue.popleft()
            for y in adj[x]:
                if y not in distances:
                    distances[y] = distances[x] + 1
                    queue.append(y)
        for w in vertices:
            expected = 0 if v == w else (2 if set(v) & set(w) else 1)
            test(distances.get(w) == expected, f'graph distance {n}: {v}, {w}')

    # Complete n-by-N incidence matrix: BB^T = (n-2)I + J.
    inc = [[int(i in edge) for edge in vertices] for i in range(n)]
    for i in range(n):
        for j in range(n):
            value = sum(inc[i][k] * inc[j][k] for k in range(N))
            test(value == 1 + (n-2)*int(i == j), f'incidence identity {n}, {i},{j}')

    # Independent spectral witness x_{ij}=u_i+u_j, u=e_0-e_1.
    x = [(int(0 in edge) - int(1 in edge)) for edge in vertices]
    test(sum(x) == 0 and any(x), f'nonzero zero-sum witness {n}')
    R = Fraction(n-3, n-4)
    test(quadratic(n, vertices, x, R) == 0, f'endpoint form {n}')
    test(quadratic(n, vertices, x, R + Fraction(1, n)) > 0, f'failure above endpoint {n}')
    test(quadratic(n, vertices, x, Fraction(1)) < 0, f'below-endpoint form {n}')

    # Counts for the cut of pair-vertices indexed by edges of a fixed n-cycle.
    selected = {tuple(sorted((i, (i+1) % n))) for i in range(n)}
    intersection_cross = disjoint_cross = 0
    all_intersection = all_disjoint = 0
    for a, b in combinations(vertices, 2):
        hit = bool(set(a) & set(b))
        separated = (a in selected) != (b in selected)
        if hit:
            all_intersection += 1
            intersection_cross += int(separated)
        else:
            all_disjoint += 1
            disjoint_cross += int(separated)
    test(all_intersection == n*comb(n-1, 2), f'intersection orbit {n}')
    test(all_disjoint == 3*comb(n, 4), f'disjoint orbit {n}')
    test(intersection_cross == 2*n*(n-3), f'intersection crossing {n}')
    test(disjoint_cross == n*(n-3)*(n-4)//2, f'disjoint crossing {n}')
    pi = Fraction(intersection_cross, all_intersection)
    pd = Fraction(disjoint_cross, all_disjoint)
    test(pi == Fraction(4*(n-3), (n-1)*(n-2)), f'prob intersect {n}')
    test(pd == Fraction(4*(n-4), (n-1)*(n-2)), f'prob disjoint {n}')
    weight = Fraction(2, 1)/pi
    test(weight*pi == 2 and weight*pd == Fraction(2*(n-4), n-3), f'optimal cut scale {n}')

    # For small n, independently enumerate every relabeling of the cycle.
    if n <= 7:
        reference_pairs = [((0,1),(0,2)), ((0,1),(2,3))]
        for a,b in reference_pairs:
            count = 0
            total = 0
            for perm in permutations(range(n)):
                S = {tuple(sorted((perm[i], perm[(i+1) % n]))) for i in range(n)}
                count += (a in S) != (b in S)
                total += 1
            expected = pi if set(a) & set(b) else pd
            test(Fraction(count, total) == expected, f'full orbit count {n}: {a}, {b}')

for n in range(5, 12):
    run_one(n)
print(f'CHECK_OK {checks} exact finite assertions; n=5..11; permutation orbit n=5..7')
