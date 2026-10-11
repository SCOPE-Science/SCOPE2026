#!/usr/bin/env python3
"""Exact finite verification of connected tight-edge potentials.

Only standard-library arithmetic is used. The grid is exhaustive for
vertices when the distances are half-integers: every vertex admits a
spanning tree of tight constraints, so its values relative to the basepoint
are multiples of one half. This check covers only the listed small spaces;
the theorem for arbitrary sizes follows from the analytical classification.
"""

from fractions import Fraction
from itertools import product


def predicted(sizes, t):
    n = sum(sizes)
    s = sum(2**a - 2 for a in sizes)
    if t == 1:
        return 2**n - 2
    if t == 2:
        return 2**n - 2 - s
    return 2**n - 2 + sum(
        (2**a - 2) * (2**(n - a) - 2) for a in sizes
    )


def enumerate_vertices(sizes, t):
    classes = [j for j, size in enumerate(sizes) for _ in range(size)]
    n = len(classes)
    distances = [(i, j, t if classes[i] == classes[j] else Fraction(1))
                 for i in range(n) for j in range(i + 1, n)]
    # All values lie within distance <=2 of the chosen basepoint.
    allowed = [Fraction(q, 2) for q in range(-4, 5)]
    vertices = 0
    for rest in product(allowed, repeat=n - 1):
        f = (Fraction(0),) + rest
        if any(abs(f[i] - f[j]) > distance
               for i, j, distance in distances):
            continue
        adj = [[] for _ in range(n)]
        for i, j, distance in distances:
            if abs(f[i] - f[j]) == distance:
                adj[i].append(j)
                adj[j].append(i)
        seen = {0}
        stack = [0]
        while stack:
            i = stack.pop()
            for j in adj[i]:
                if j not in seen:
                    seen.add(j)
                    stack.append(j)
        if len(seen) == n:
            vertices += 1
    return vertices


def main():
    # The dimensions and profiles include singleton and mixed blocks.
    cases = [(2, 1, 1), (2, 2, 1), (2, 2, 2), (3, 1, 1)]
    parameters = [Fraction(1), Fraction(3, 2), Fraction(2)]
    for sizes in cases:
        for t in parameters:
            found = enumerate_vertices(sizes, t)
            expected = predicted(sizes, t)
            assert found == expected, (sizes, t, found, expected)
            print(f"sizes={sizes}; t={t}; vertices={found}; expected={expected}; PASS")
    print("EXACT_SMALL_CASES_PASS: 12")


if __name__ == '__main__':
    main()
