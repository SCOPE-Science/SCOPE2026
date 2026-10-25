#!/usr/bin/env python3
"""Direct finite verification for single-edge subdivisions of bicliques.

Uses the original color-change rule and the original fort definition.
Run: python3 verify_subdivision.py
"""
from collections import Counter
from itertools import combinations


def graph(p, q):
    n = p + q + 1
    nbr = [set() for _ in range(n)]
    for a in range(p):
        for b in range(q):
            if (a, b) == (0, 0):
                continue
            u, v = a, p + b
            nbr[u].add(v)
            nbr[v].add(u)
    for v in (0, p):
        nbr[v].add(n - 1)
        nbr[n - 1].add(v)
    return nbr


def forcing(nbr, initially_white):
    white = set(initially_white)
    while white:
        newly_blue = set()
        for v, adj in enumerate(nbr):
            if v not in white:
                candidates = adj.intersection(white)
                if len(candidates) == 1:
                    newly_blue.update(candidates)
        if not newly_blue:
            return False
        white.difference_update(newly_blue)
    return True


def is_fort(nbr, subset):
    if not subset:
        return False
    return all(len(adj.intersection(subset)) != 1
               for v, adj in enumerate(nbr) if v not in subset)


def proposed_minimal_forts(p, q):
    left = range(1, p)
    right = range(p + 1, p + q)
    s = p + q
    result = [frozenset(c) for c in combinations(left, 2)]
    result += [frozenset(c) for c in combinations(right, 2)]
    result += [frozenset((0, s, a)) for a in left]
    result += [frozenset((p, s, b)) for b in right]
    result += [frozenset((0, p, a, b)) for a in left for b in right]
    return set(result)


def actual_minimal_forts(nbr):
    n = len(nbr)
    forts = []
    for size in range(1, n + 1):
        for tup in combinations(range(n), size):
            subset = frozenset(tup)
            if any(s.issubset(subset) for s in forts):
                continue
            if is_fort(nbr, subset):
                forts.append(subset)
    return set(forts)


def expected_polynomial(p, q):
    n = p + q + 1
    return {n - 3: 3 * p * q - p - q,
            n - 2: p * q + 2 * p + 2 * q - 2,
            n - 1: n,
            n: 1}


def run():
    total = 0
    boards = [(3, 3), (3, 4), (4, 3), (4, 4),
              (3, 5), (5, 3), (4, 5), (5, 4), (5, 5), (5, 6), (6, 5), (6, 6)]
    checked_forts = 0
    for p, q in boards:
        nbr = graph(p, q)
        n = len(nbr)
        claimed_forts = proposed_minimal_forts(p, q)
        assert all(is_fort(nbr, f) for f in claimed_forts)
        counts = Counter()
        for mask in range(1 << n):
            white = {v for v in range(n) if (mask >> v) & 1}
            actual = forcing(nbr, white)
            by_forts = not any(f.issubset(white) for f in claimed_forts)
            assert actual == by_forts, (p, q, white, actual, by_forts)
            if actual:
                counts[n - len(white)] += 1
        assert dict(counts) == expected_polynomial(p, q), (p, q, counts)
        total += 1 << n
        if p <= 4 and q <= 4:
            assert actual_minimal_forts(nbr) == claimed_forts
            checked_forts += 1
        print(f'p={p} q={q} subsets={1 << n} ' +
              f'coefficients={sorted(counts.items())} PASS')
    print(f'VERIFY_OK boards={len(boards)} subsets={total} '
          f'exhaustive_minimal_fort_boards={checked_forts}')


if __name__ == '__main__':
    run()
