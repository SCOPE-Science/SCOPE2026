#!/usr/bin/env python3
"""Finite checks for the cyclic-power DET:OLD theorem (Python 3.10+, stdlib only)."""
from collections import Counter, defaultdict
from itertools import combinations

D = (1, 2, 5, 6, 7)


def det_old(n, mask):
    """Definition, independently evaluating neighborhood difference predicates."""
    neighborhoods = [sum(1 << ((u + d) % n) for d in (-2, -1, 1, 2))
                     for u in range(n)]
    codes = [bits & mask for bits in neighborhoods]
    if min(code.bit_count() for code in codes) < 2:
        return False
    for u in range(n):
        for v in range(u + 1, n):
            if ((codes[u] & ~codes[v]).bit_count() < 2 and
                    (codes[v] & ~codes[u]).bit_count() < 2):
                return False
    return True


def complement_is_independent(n, deleted):
    """Every pair of deleted sites avoids the five forbidden cyclic differences."""
    sites = [u for u in range(n) if deleted & (1 << u)]
    return all((v - u) not in D and (n - v + u) not in D
               for u, v in combinations(sites, 2))


def transfer_independence_polynomial(n):
    """Trace of a 128-state length-n transfer matrix with integer-polynomial weights."""
    transitions = {}
    for state in range(128):
        edges = [((state << 1) & 127, 0)]
        if all(not (state & (1 << (d - 1))) for d in D):
            edges.append((((state << 1) | 1) & 127, 1))
        transitions[state] = edges

    poly = Counter()
    for initial in range(128):
        frontier = {(initial, 0): 1}
        for _ in range(n):
            following = defaultdict(int)
            for (state, cardinality), multiplicity in frontier.items():
                for target, chosen in transitions[state]:
                    following[(target, cardinality + chosen)] += multiplicity
            frontier = following
        for (state, cardinality), multiplicity in frontier.items():
            if state == initial:
                poly[cardinality] += multiplicity
    return poly


def predicted_number(n):
    if n < 8:
        return None
    if n <= 10:
        return n - 1
    if n == 11:
        return 9
    return n - (n // 4 if n % 4 == 0 else n // 4 - 1)


def predicted_minimum_count(n):
    if n < 8:
        return 0
    if n <= 11:
        return n
    if n in (13, 14, 15):
        return 2 * n
    if n % 4 == 0:
        return 4
    if n == 22:
        return 3 * n // 2
    if n == 23:
        return 3 * n
    if n % 4 == 3:
        return 2 * n
    return n


def main():
    # Exhaustive, direct test of the definition, with no reliance on transfer states.
    for n in range(3, 17):
        p = Counter()
        by_independence = Counter()
        for deleted in range(1 << n):
            selected = ((1 << n) - 1) ^ deleted
            if det_old(n, selected):
                p[selected.bit_count()] += 1
            if n >= 12 and complement_is_independent(n, deleted):
                by_independence[selected.bit_count()] += 1
            if n >= 12:
                assert det_old(n, selected) == complement_is_independent(n, deleted), (n, deleted)
        if n < 8:
            assert not p, (n, p)
        else:
            assert min(p) == predicted_number(n), (n, p)
            assert p[min(p)] == predicted_minimum_count(n), (n, p)
        if n >= 12:
            assert p == by_independence
        print('EXHAUSTIVE', n, 'valid', sum(p.values()), 'minimum', min(p) if p else 'none')

    # Independent transfer-matrix evaluation for every n in 12..40.
    for n in range(12, 41):
        polynomial = transfer_independence_polynomial(n)
        maximum_deleted = max(polynomial)
        assert n - maximum_deleted == predicted_number(n), n
        assert polynomial[maximum_deleted] == predicted_minimum_count(n), (n, polynomial[maximum_deleted])
        assert sum(polynomial.values()) > 0
        if n <= 16:
            count = sum(complement_is_independent(n, z) for z in range(1 << n))
            assert count == sum(polynomial.values())
        print('TRANSFER', n, 'maximum_deleted', maximum_deleted,
              'minimum_count', polynomial[maximum_deleted])
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
