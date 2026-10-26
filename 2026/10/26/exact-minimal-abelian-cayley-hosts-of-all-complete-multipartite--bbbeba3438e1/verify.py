#!/usr/bin/env python3
"""Finite exact checks supplementing the elementary induced-Cayley proof."""
from itertools import combinations, combinations_with_replacement, permutations, product
from math import prod


def check_cyclic_construction(parts):
    t = len(parts)
    m = max(parts)
    n = t*m
    blocks = [[j + t*i for i in range(size)] for j, size in enumerate(parts)]
    vertices = [(j, v) for j, block in enumerate(blocks) for v in block]
    assert len({v for _, v in vertices}) == sum(parts)
    edges = {d for d in range(n) if d % t != 0}
    for (j, x), (k, y) in combinations(vertices, 2):
        assert (((x-y) % n) in edges) == (j != k)
    j0 = parts.index(m)
    a = set(blocks[j0])
    xsets = [{(u-v) % n for u in a for v in a}]
    xsets.extend({(blocks[j][0]-v) % n for v in a} for j in range(t) if j != j0)
    assert all(len(s) == m for s in xsets)
    assert all(not (xsets[i] & xsets[j]) for i in range(t) for j in range(i))
    assert set().union(*xsets) == set(range(n))
    return len(vertices)*(len(vertices)-1)//2


def group_elements(factors):
    return list(product(*(range(a) for a in factors)))


def add(a, b, factors):
    return tuple((x+y) % d for x, y, d in zip(a, b, factors))


def neg(a, factors):
    return tuple((-x) % d for x, d in zip(a, factors))


def sub(a, b, factors):
    return add(a, neg(b, factors), factors)


def lower_search(parts, factors):
    """Full label enumeration for the large-part-plus-singletons test families."""
    assert parts.count(1) == len(parts)-1
    size = max(parts)
    universe = group_elements(factors)
    zero = tuple(0 for _ in factors)
    tested = 0
    for tail in combinations([v for v in universe if v != zero], size-1):
        a = (zero,) + tail
        aa = {sub(u, v, factors) for u in a for v in a}
        available = [v for v in universe if v not in a]
        if len(aa) < size:
            raise AssertionError("Impossible difference-set size")
        for representatives in permutations(available, len(parts)-1):
            tested += 1
            sets = [aa]
            sets.extend({sub(z, u, factors) for u in a} for z in representatives)
            if all(not sets[i].intersection(sets[j]) for i in range(len(sets)) for j in range(i)):
                raise AssertionError(f"Unexpected smaller host: {parts}, {factors}, {a}, {representatives}")
    return tested


def main():
    construction_cases = 0
    pairs_checked = 0
    for t in range(2, 7):
        for parts in combinations_with_replacement(range(1, 6), t):
            pairs_checked += check_cyclic_construction(parts)
            construction_cases += 1
    # All finite abelian types of host orders from 5 through 11.
    group_types = {
        5: [(5,)], 6: [(6,)], 7: [(7,)],
        8: [(8,), (4, 2), (2, 2, 2)],
        9: [(9,), (3, 3)], 10: [(10,)], 11: [(11,)]
    }
    tested = 0
    groups = 0
    family_tests = 0
    for parts in ((1, 1, 1, 2), (1, 1, 1, 3), (1, 1, 1, 1, 2)):
        threshold = len(parts)*max(parts)
        for n in range(sum(parts), threshold):
            for factors in group_types.get(n, []):
                assert prod(factors) == n
                tested += lower_search(parts, factors)
                groups += 1
        family_tests += 1
    print(f"ALL CHECKS PASSED; cyclic_construction_cases={construction_cases}; induced_pair_checks={pairs_checked}; abelian_small_host_types={groups}; normalized_candidate_embeddings={tested}; finite_families={family_tests}")


if __name__ == '__main__':
    main()
