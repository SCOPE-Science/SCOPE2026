#!/usr/bin/env python3
"""Exhaustive exact finite certificate for targeted single-node vaccination in trees.
Only standard Python 3 library is required. Run `python3 tree_vaccine_verifier.py`.
"""
from collections import deque
from itertools import product
from heapq import heapify, heappop, heappush


def prufer_tree(n, sequence):
    degree = [1] * n
    for x in sequence:
        degree[x] += 1
    leaves = [i for i, d in enumerate(degree) if d == 1]
    heapify(leaves)
    edges = []
    for x in sequence:
        y = heappop(leaves)
        edges.append((x, y))
        degree[x] -= 1
        degree[y] -= 1
        if degree[x] == 1:
            heappush(leaves, x)
    a = heappop(leaves)
    b = heappop(leaves)
    edges.append((a, b))
    return edges


def pair_coefficients(n, edges, vaccinated):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        if a != vaccinated and b != vaccinated:
            graph[a].append(b)
            graph[b].append(a)
    coeffs = [0] * (n - 1)
    for seed in range(n):
        if seed == vaccinated:
            continue
        distance = [-1] * n
        distance[seed] = 0
        todo = deque([seed])
        while todo:
            a = todo.popleft()
            for b in graph[a]:
                if distance[b] == -1:
                    distance[b] = distance[a] + 1
                    todo.append(b)
        for b in range(seed + 1, n):
            if b != vaccinated and distance[b] > 0:
                coeffs[distance[b] - 1] += 1
    return tuple(coeffs)


def prefix_leq(lhs, rhs):
    """Sufficient exact certificate: F_lhs(p) <= F_rhs(p) for all p in [0,1]."""
    total = 0
    for a, b in zip(lhs, rhs):
        total += b - a
        if total < 0:
            return False
    return True


def certificate_vertex(polynomials):
    return next((i for i, a in enumerate(polynomials)
                 if all(prefix_leq(a, b) for b in polynomials)), None)


def check_lower_bound():
    counts = {}
    for n in range(2, 8):
        checked = 0
        for sequence in product(range(n), repeat=n-2):
            edges = prufer_tree(n, sequence)
            polynomials = [pair_coefficients(n, edges, i) for i in range(n)]
            assert certificate_vertex(polynomials) is not None, (n, sequence, edges)
            checked += 1
        assert checked == n ** (n - 2)
        counts[n] = checked
    assert sum(counts.values()) == 18248
    return counts


def check_eight_vertex_witness():
    edges = [(0, 5), (0, 1), (1, 2), (2, 3), (2, 4), (5, 6), (6, 7)]
    poly = [pair_coefficients(8, edges, v) for v in range(8)]
    assert poly[1] == (5, 3, 1, 0, 0, 0, 0), poly[1]
    assert poly[2] == (4, 3, 2, 1, 0, 0, 0), poly[2]
    for v in range(8):
        if v not in (1, 2):
            assert prefix_leq(poly[1], poly[v]), (v, poly[v])
    # F_2 - F_1 = -p + p^3 + p^4 = p (p^2 + p^3 - 1).
    assert tuple(b-a for a,b in zip(poly[1], poly[2])) == (-1, 0, 1, 1, 0, 0, 0)
    # Rational evaluations straddle the unique positive root.
    from fractions import Fraction
    def evaluate(coefficients, p):
        return sum(Fraction(c) * p**(i+1) for i,c in enumerate(coefficients))
    assert evaluate(poly[2], Fraction(1,2)) < evaluate(poly[1], Fraction(1,2))
    assert evaluate(poly[1], Fraction(9,10)) < evaluate(poly[2], Fraction(9,10))
    assert evaluate(poly[2], Fraction(1,2)) == Fraction(49,16)
    assert evaluate(poly[1], Fraction(1,2)) == Fraction(27,8)
    return poly


if __name__ == '__main__':
    counts = check_lower_bound()
    poly = check_eight_vertex_witness()
    print('PASS all labeled trees, n=2..7:', counts, 'total', sum(counts.values()))
    print('PASS eight-vertex witness pair vectors:', poly[1], poly[2])
    print('PASS global witness comparison certificates and exact rational samples')
