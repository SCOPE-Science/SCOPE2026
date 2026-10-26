#!/usr/bin/env python3
"""Reproduce the exhaustive five-item, three-partition classification.

Uses only Python's standard library and exact integer operations.
"""
from itertools import product, permutations
from collections import Counter


def set_partitions_three(n):
    out = []
    for words in product(range(3), repeat=n):
        if set(words) != {0, 1, 2}:
            continue
        blocks = tuple(sum((1 << j for j, label in enumerate(words) if label == i), 0)
                       for i in range(3))
        if blocks[0] < blocks[1] < blocks[2]:
            out.append(blocks)
    assert len(out) == len(set(out))
    return out


def disjoint_transversal(partitions):
    return any(not ((a & b) or (a & c) or (b & c))
               for a, b, c in product(*partitions))


def canonical_exception(partitions, n=5):
    if n != 5:
        return False
    singleton = []
    matchings = []
    for p in partitions:
        singles = [b for b in p if b.bit_count() == 1]
        if len(singles) != 1:
            return False
        singleton.append(singles[0])
        pairs = frozenset(b for b in p if b.bit_count() == 2)
        if len(pairs) != 2:
            return False
        matchings.append(pairs)
    return len(set(singleton)) == 1 and len(set(matchings)) == 3


def main():
    for n, expected in [(3, 1), (4, 6), (5, 25)]:
        p = set_partitions_three(n)
        assert len(p) == expected, (n, len(p))
        print(f"partitions n={n}: {len(p)}")
        if n == 3 or n == 4:
            assert all(disjoint_transversal(t) for t in product(p, repeat=3))
    p = set_partitions_three(5)
    bad = [triple for triple in product(p, repeat=3)
           if not disjoint_transversal(triple)]
    modeled = [triple for triple in product(p, repeat=3)
               if canonical_exception(triple)]
    assert len(bad) == len(modeled) == 30
    assert set(bad) == set(modeled)
    print("three five-item partitions: total=15625, no-transversal=30")

    # Independently verify that all 30 failures form a single orbit
    # under permutations of goods and of the three agents.
    def permute_mask(mask, goods_permutation):
        return sum(1 << goods_permutation[j] for j in range(5)
                   if mask & (1 << j))

    representative = bad[0]
    orbit = set()
    for pi in permutations(range(5)):
        transformed = tuple(tuple(sorted(permute_mask(block, pi)
                                          for block in partition))
                            for partition in representative)
        for sigma in permutations(range(3)):
            orbit.add(tuple(transformed[sigma[i]] for i in range(3)))
    assert orbit == set(bad), (len(orbit), len(bad))
    print("one good/agent relabeling orbit, size=30")

    # Canonical monotone, normalized, binary-valued agents.
    e = 1 << 4
    matchings = [frozenset((0b0011, 0b1100)),
                 frozenset((0b0101, 0b1010)),
                 frozenset((0b1001, 0b0110))]
    assert len(set(matchings)) == 3

    def value(i, bundle):
        return int(bool(bundle & e) or any((bundle & edge) == edge
                                            for edge in matchings[i]))

    # Each partition consisting of e and the two matching edges
    # guarantees maximin share >= 1; binary range forces equality.
    for i in range(3):
        assert value(i, e) == 1
        assert all(value(i, edge) == 1 for edge in matchings[i])
        assert all(value(i, 0) == 0 and value(i, (1 << 5)-1) == 1
                   for i in range(3))

    # Exhaustively test all labeled allocations of five indivisible goods.
    satisfying_allocations = 0
    for assignment in product(range(3), repeat=5):
        bundles = [0, 0, 0]
        for j, owner in enumerate(assignment):
            bundles[owner] |= (1 << j)
        if all(value(i, bundles[i]) >= 1 for i in range(3)):
            satisfying_allocations += 1
    assert satisfying_allocations == 0
    print("canonical non-MMS instance: 243 allocations examined, 0 fair")
    print("PASS: analytic classification and computational census agree")


if __name__ == '__main__':
    main()
