#!/usr/bin/env python3
"""Independent finite checks of a clique-bouquet defensive-alliance theorem.

Run with Python 3.9+. A clique bouquet has a common center and pairwise
nonadjacent peripheral cliques of orders given by the input tuple.
"""
from collections import Counter
from itertools import combinations, product
from math import comb


def adjacency(blades):
    assert len(blades) >= 2 and min(blades) >= 2
    total = 1 + sum(blades)
    edges = [set() for _ in range(total)]
    offset = 1
    for size in blades:
        block = list(range(offset, offset + size))
        for v in block:
            edges[0].add(v)
            edges[v].add(0)
            for w in block:
                if w != v:
                    edges[v].add(w)
        offset += size
    return edges


def brute_minimal_sets(blades):
    adj = adjacency(blades)
    n = len(adj)
    min_sets = []
    valid_count = 0
    # Any proper subset has a strictly smaller integer-encoded bitmask.
    for mask in range(1, 1 << n):
        if any((mask & prior) == prior for prior in min_sets):
            continue
        valid = True
        for v in range(n):
            if not (mask & (1 << v)):
                continue
            inside = sum((mask >> u) & 1 for u in adj[v])
            if 2 * inside + 1 < len(adj[v]):
                valid = False
                break
        if valid:
            min_sets.append(mask)
    return set(min_sets)


def predicted_sets(blades):
    block_lists = []
    offset = 1
    local = set()
    for size in blades:
        block = list(range(offset, offset + size))
        block_lists.append(block)
        for chosen in combinations(block, size // 2 + 1):
            local.add(sum(1 << vertex for vertex in chosen))
        offset += size
    if sum(x % 2 for x in blades) <= 1:
        for groups in product(*[combinations(block, len(block) // 2)
                                for block in block_lists]):
            local.add(1 | sum(1 << vertex for group in groups for vertex in group))
    return local


def coefficients(sets):
    return dict(sorted(Counter(mask.bit_count() for mask in sets).items()))


def expected_coefficients(blades):
    result = Counter()
    for r in blades:
        result[r // 2 + 1] += comb(r, r // 2 + 1)
    if sum(r % 2 for r in blades) <= 1:
        prod = 1
        for r in blades:
            prod *= comb(r, r // 2)
        result[1 + sum(r // 2 for r in blades)] += prod
    return dict(sorted(result.items()))


def run():
    trials = [
        (2, 2), (2, 3), (3, 3), (2, 4), (3, 4), (4, 4),
        (2, 2, 2), (2, 2, 3), (2, 3, 4), (3, 3, 3),
        (2, 2, 4), (2, 4, 4), (3, 2, 2, 2), (3, 3, 4),
        (2, 2, 2, 2), (4, 5), (4, 6), (3, 5, 2), (2, 2, 5),
        (2, 3, 3, 2), (2, 3, 2, 2),
    ]
    examined = 0
    for sizes in trials:
        x = brute_minimal_sets(sizes)
        y = predicted_sets(sizes)
        assert x == y, (sizes, x ^ y)
        assert coefficients(x) == expected_coefficients(sizes)
        count = (1 << (1 + sum(sizes))) - 1
        examined += count
        print(f'{sizes}: vertices={1+sum(sizes)}, subsets={count}, '
              f'minimal={len(x)}, coefficients={coefficients(x)}, OK')
    print(f'PASS: {len(trials)} cases, {examined} nonempty input subsets tested; '
          'direct inequality and inclusion-minimality agree with the classification.')


if __name__ == '__main__':
    run()
