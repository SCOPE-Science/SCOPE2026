#!/usr/bin/env python3
"""Independent finite checks for the height-two poset extension identity.

Run: python3 verify.py
The tests are finite consistency checks, not a general proof.
"""
from itertools import product
from random import Random


def indset_count(a, b, edges):
    """Count independent sets of a bipartite graph by subset masks."""
    rows = [0] * a
    for x, y in edges:
        rows[x] |= 1 << y
    answer = 0
    for ma in range(1 << a):
        forbidden = 0
        for x in range(a):
            if (ma >> x) & 1:
                forbidden |= rows[x]
        answer += 1 << (b - forbidden.bit_count())
    return answer


def poset_type_count_by_ternary(a, b, edges):
    """Enumerate all ternary adjacency patterns and check all poset conditions."""
    n = a + b
    edges = set(edges)
    strict_pairs = {(x, a + y) for x, y in edges}
    answer = 0
    for word in product(range(3), repeat=n):
        lower = {i for i, w in enumerate(word) if w == 1}
        upper = {i for i, w in enumerate(word) if w == 2}
        if any(v in lower and u not in lower for u, v in strict_pairs):
            continue
        if any(u in upper and v not in upper for u, v in strict_pairs):
            continue
        if any((u, v) not in strict_pairs for u in lower for v in upper):
            continue
        answer += 1
    return answer


def formula(a, b, edges):
    complete = {(x, y) for x in range(a) for y in range(b)}
    i = indset_count(a, b, edges)
    ic = indset_count(a, b, complete.difference(edges))
    return 2 * i + ic - (1 << a) - (1 << b)


def isolated_padding_count(a, b, edges, k):
    # Uses the independently enumerable pair of bipartite graph invariants.
    complete = {(x, y) for x in range(a) for y in range(b)}
    return (1 << (k + 1)) * indset_count(a, b, edges) + \
           indset_count(a, b, complete.difference(edges)) - (1 << a) - (1 << b)


def check(a, b, edges, brute=True):
    fc = formula(a, b, edges)
    if brute:
        assert poset_type_count_by_ternary(a, b, edges) == fc, (a, b, edges)
    k = a + b
    padded_formula = isolated_padding_count(a, b, edges, k)
    assert padded_formula == formula(a + k, b, edges), (a, b, edges, k)
    recovered = (padded_formula + 1) // (1 << (k + 1))
    assert recovered == indset_count(a, b, edges), (a, b, edges, recovered)
    return 1


def main():
    exhaustive = 0
    for a in range(1, 4):
        for b in range(1, 4):
            if a + b > 6:
                continue
            for mask in range(1 << (a * b)):
                edges = {(x, y) for x in range(a) for y in range(b)
                         if (mask >> (x * b + y)) & 1}
                exhaustive += check(a, b, edges)

    rng = Random(20261018)
    sampled = 0
    for a, b in [(3, 4), (4, 4), (4, 5), (5, 5)]:
        for _ in range(60):
            edges = {(x, y) for x in range(a) for y in range(b)
                     if rng.randrange(4) <= 1}
            sampled += check(a, b, edges, brute=False)

    # Ensure exact-height-two rather than merely at-most-two hardness:
    # adjoining a disjoint edge multiplies the independent-set count by three.
    edge_factor = 0
    for a, b in [(1, 1), (2, 3), (3, 3)]:
        for mask in range(min(1 << (a * b), 64)):
            edges = {(x, y) for x in range(a) for y in range(b)
                     if (mask >> (x * b + y)) & 1}
            enlarged = set(edges) | {(a, b)}
            assert indset_count(a + 1, b + 1, enlarged) == \
                   3 * indset_count(a, b, edges)
            edge_factor += 1

    print(f'EXHAUSTIVE_GRAPHS={exhaustive}')
    print(f'LARGER_GRAPH_SAMPLES={sampled}')
    print(f'DISJOINT_EDGE_CHECKS={edge_factor}')
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    main()
