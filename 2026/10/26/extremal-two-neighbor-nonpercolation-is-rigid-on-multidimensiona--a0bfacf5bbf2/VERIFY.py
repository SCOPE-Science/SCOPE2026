"""Independent finite checks for extremal two-neighbor bootstrap configurations on Cartesian tori.

Run: python3 VERIFY.py
This checks small instances only; the theorem for arbitrary dimensions requires the accompanying proof.
"""
from itertools import combinations, product
from math import prod
from random import Random


def torus_neighbors(lengths):
    vertices = list(product(*(range(k) for k in lengths)))
    index = {v: i for i, v in enumerate(vertices)}
    masks = []
    for v in vertices:
        ns = 0
        for j, k in enumerate(lengths):
            for step in (-1, 1):
                w = list(v)
                w[j] = (w[j] + step) % k
                ns |= 1 << index[tuple(w)]
        masks.append(ns)
    return vertices, masks


def is_closed_complement(mask, neighbors, dimension):
    need = 2 * dimension - 1
    remaining = mask
    while remaining:
        low = remaining & -remaining
        i = low.bit_length() - 1
        if (neighbors[i] & mask).bit_count() < need:
            return False
        remaining ^= low
    return True


def slabs(lengths, vertices):
    max_k = max(lengths)
    ans = set()
    for j, k in enumerate(lengths):
        if k == max_k:
            for a in range(k):
                mask = sum(1 << i for i, v in enumerate(vertices)
                           if v[j] == a or v[j] == (a + 1) % k)
                ans.add(mask)
    assert len(ans) == sum(k for k in lengths if k == max_k)
    return ans


def exact_small(lengths):
    vertices, neighbors = torus_neighbors(lengths)
    n, dim = len(vertices), len(lengths)
    target = 2 * n // max(lengths)
    expected = slabs(lengths, vertices)
    feasible = set()
    checked = 0
    for k in range(1, target + 1):
        for inds in combinations(range(n), k):
            checked += 1
            mask = sum(1 << i for i in inds)
            if is_closed_complement(mask, neighbors, dim):
                assert k == target, (lengths, k, inds)
                feasible.add(mask)
    assert feasible == expected, (lengths, len(feasible), len(expected))
    print('EXACT', lengths, 'subsets_checked', checked,
          'minimum_surviving', target, 'extremizers', len(feasible))
    return checked


def constructive_and_random():
    rng = Random(20261024)
    total = 0
    for lengths in [(4, 4, 4), (4, 4, 5), (4, 5, 5), (4, 5, 6),
                    (5, 5, 5), (4, 4, 4, 4), (4, 4, 5, 6), (5, 6, 7, 8)]:
        vertices, neighbors = torus_neighbors(lengths)
        n = len(vertices)
        goal = 2 * n // max(lengths)
        for mask in slabs(lengths, vertices):
            assert mask.bit_count() == goal
            assert is_closed_complement(mask, neighbors, len(lengths))
            total += 1
        for _ in range(100):
            k = rng.randint(1, min(goal, 70))
            m = sum(1 << i for i in rng.sample(range(n), k))
            if is_closed_complement(m, neighbors, len(lengths)):
                assert k == goal and m in slabs(lengths, vertices)
            total += 1
    print('CONSTRUCTION_RANDOM', total, 'checks')


if __name__ == '__main__':
    count = sum(exact_small(x) for x in [(4, 4), (4, 5), (5, 5)])
    constructive_and_random()
    print('VERIFY_OK exhaustive_subsets', count)
