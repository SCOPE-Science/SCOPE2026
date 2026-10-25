#!/usr/bin/env python3
"""Verify exact labelled forced-four-colouring counts of finite wheel graphs.

Requires only Python's standard library. All numeric checks are integer-exact.
"""
from collections import Counter
from itertools import product
from math import comb


def cycle_chromatic(k, q):
    return (q - 1) ** k + (q - 1) * (-1) ** k


def independent_supports(n, h):
    if h == 0:
        return 1
    return n * comb(n - h, h) // (n - h)


def predicted_counts(n):
    """Counts by exact number of initially coloured vertices."""
    counts = Counter()
    for h in range(n // 2 + 1):
        k = n - h
        mult = 4 * independent_supports(n, h)
        counts[k + 1] += mult * cycle_chromatic(k, 3)
        counts[k] += mult * (cycle_chromatic(k, 3) - 3 * cycle_chromatic(k, 2))
    return +counts


def all_rim_patterns(n):
    """Independent enumeration: 0 denotes an uncoloured rim vertex."""
    counts = Counter()
    for word in product(range(4), repeat=n):
        for i in range(n):
            left, cur, right = word[(i - 1) % n], word[i], word[(i + 1) % n]
            if (cur != 0 and right != 0 and cur == right) or (cur == 0 and (left == 0 or right == 0 or left == right)):
                break
        else:
            k = sum(v != 0 for v in word)
            counts[k + 1] += 4
            if {1, 2, 3}.issubset(word):
                counts[k] += 4
    return +counts


def local_forcing_reaches_all(initial):
    """Direct simulation on the original graph, independent of compression."""
    n = len(initial) - 1
    neighbors = [tuple(range(1, n + 1))]
    neighbors.extend((0, 1 + (i - 1) % n, 1 + (i + 1) % n) for i in range(n))
    state = list(initial)
    for v, adj in enumerate(neighbors):
        if state[v] and any(state[v] == state[u] for u in adj):
            return False
    while True:
        if all(state):
            return True
        for v, adj in enumerate(neighbors):
            if state[v] == 0:
                seen = {state[u] for u in adj if state[u]}
                if len(seen) == 3:
                    state[v] = next(c for c in range(1, 5) if c not in seen)
                    break
        else:
            return False


def direct_counts(n):
    counts = Counter()
    for word in product(range(5), repeat=n + 1):
        if local_forcing_reaches_all(word):
            counts[sum(c != 0 for c in word)] += 1
    return +counts


def minimum_coefficient(n):
    k = (n + 1) // 2
    return 4 * independent_supports(n, n // 2) * (2 ** k - 3 - (-1) ** k)


def main():
    checks = 0
    for n in range(5, 13):
        for h in range(n // 2 + 1):
            mask_count = sum(
                1 for mask in range(1 << n)
                if mask.bit_count() == h and all(not (mask & (1 << i) and mask & (1 << ((i + 1) % n))) for i in range(n))
            )
            assert mask_count == independent_supports(n, h), (n, h)
            checks += 1
        formula = predicted_counts(n)
        assert min(formula) == (n + 1) // 2, n
        assert formula[min(formula)] == minimum_coefficient(n), n
        checks += 2
        if n <= 9:
            assert formula == all_rim_patterns(n), (n, 'rim')
            checks += 1
        if n <= 7:
            actual = direct_counts(n)
            assert formula == actual, (n, 'direct', formula, actual)
            checks += 1
        print(f'n={n} minimum={min(formula)} multiplicity={formula[min(formula)]} checks=ok')
    assert predicted_counts(5) == {3: 120, 4: 360, 5: 480, 6: 120}
    assert predicted_counts(6) == {3: 48, 4: 480, 5: 1368, 6: 960, 7: 264}
    print(f'VERIFY_OK ({checks} independently cross-checked identities)')


if __name__ == '__main__':
    main()
