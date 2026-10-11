#!/usr/bin/env python3
"""Exact-rational verification of cube-section vertices and numerical-index-one criterion."""
from fractions import Fraction
from itertools import product


def vertices(weights):
    n = len(weights)
    out = set()
    for free in range(n):
        fixed = [j for j in range(n) if j != free]
        for signs in product((-1, 1), repeat=n-1):
            q = [-9] * n
            for j, s in zip(fixed, signs):
                q[j] = Fraction(s)
            q[free] = -sum(weights[j]*q[j] for j in fixed) / weights[free]
            if abs(q[free]) <= 1:
                out.add(tuple(q))
    return out


def score(weights):
    n = len(weights)
    total = sum(weights)
    active = [i for i in range(n) if 2*weights[i] < total]
    vs = vertices(weights)
    assert vs
    mcgregor = all(abs(v[i]) == 1 for i in active for v in vs)
    predicate = 2*max(weights) >= total or (n % 2 == 0 and len(set(weights)) == 1)
    assert mcgregor == predicate, (weights, predicate, mcgregor)
    if 2*max(weights) < total and not (n%2 == 0 and len(set(weights)) == 1):
        assert any(abs(v[i]) < 1 for i in active for v in vs)
    return len(vs)


def main():
    checks = 0
    total_vertices = 0
    for n in range(4, 7):
        for entry in product(range(1, 4), repeat=n):
            weights = tuple(Fraction(x) for x in entry)
            total_vertices += score(weights)
            checks += 1
    print(f"VERIFY_OK rational_weight_vectors={checks} cube_vertices={total_vertices} dimensions=4..6 weights=1..3")

if __name__ == '__main__':
    main()
