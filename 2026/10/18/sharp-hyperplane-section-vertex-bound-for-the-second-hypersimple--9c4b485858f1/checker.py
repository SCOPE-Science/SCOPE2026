#!/usr/bin/env python3
"""Exact finite checks for the maximal-section theorem of second hypersimplices.

Uses only Python's standard library. Finite checks corroborate, rather than
replace, the all-dimensional mathematical proof in RESULT.md.
"""
from itertools import combinations
from math import comb
from random import Random


def bound(n):
    return 2 * sum((k * k) // 4 for k in range(2, n))


def mixed_triangle_count(word):
    # Word position j (zero-based) is creation bit for vertex j+1.
    n = len(word) + 1
    m = 0
    for i, j, k in combinations(range(n), 3):
        if word[j - 1] != word[k - 1]:
            m += 1
    return m


def suffix_balance(word):
    n = len(word) + 1
    for length in range(2, n):
        suffix = word[-length:]
        if abs(sum(suffix) - (length - sum(suffix))) > 1:
            return False
    return True


def crossing_edges_from_weights(weights):
    n = len(weights)
    labels = {(i, j): (weights[i] + weights[j] > 0)
              for i, j in combinations(range(n), 2)}
    assert all(weights[i] + weights[j] != 0 for i, j in labels)
    crossings = 0
    mixed = 0
    for i, j, k in combinations(range(n), 3):
        signs = (labels[(i, j)], labels[(i, k)], labels[(j, k)])
        if len(set(signs)) == 2:
            mixed += 1
        crossings += sum(signs[a] != signs[b]
                         for a, b in ((0, 1), (0, 2), (1, 2)))
    assert crossings == 2 * mixed
    return crossings


def centered_generic_weights(n, random):
    # An exact-integral perturbation of centered arithmetic normal coordinates.
    # The large factor preserves signs of all previously nonzero pair sums.
    for _ in range(10000):
        jit = [random.randint(-10_000, 10_000) for _ in range(n)]
        total = sum(jit)
        weights = [10**9 * (2*i - (n-1)) + n*jit[i] - total
                   for i in range(n)]
        assert sum(weights) == 0
        if all(weights[i] + weights[j] != 0
               for i, j in combinations(range(n), 2)):
            return weights
    raise AssertionError('Failed to find a generic perturbation')


def check():
    words = 0
    for n in range(3, 16):
        found = 0
        winners = 0
        for mask in range(1 << (n-1)):
            word = [(mask >> i) & 1 for i in range(n-1)]
            count = 2*mixed_triangle_count(word)
            equal = count == bound(n)
            assert count <= bound(n)
            assert equal == suffix_balance(word)
            if equal:
                winners += 1
            found = max(found, count)
            words += 1
        assert found == bound(n) == comb(n, 3) + (n-1)**2 // 4
        assert winners > 0
    print('EXHAUSTIVE_THRESHOLD_WORDS_OK', words)

    rng = Random(20261016)
    sections = 0
    for n in range(3, 36):
        for repetition in range(9):
            weights = centered_generic_weights(n, rng)
            assert crossing_edges_from_weights(weights) == bound(n)
            sections += 1
        # General integer normals, when generic, cannot exceed the maximum.
        for repetition in range(9):
            for attempt in range(10000):
                arr = [rng.randint(-100_000, 100_000) for _ in range(n)]
                weights = [n*z - sum(arr) for z in arr]
                if all(weights[i] + weights[j] != 0
                       for i, j in combinations(range(n), 2)):
                    break
            else:
                raise AssertionError('Generic sampling failed')
            assert crossing_edges_from_weights(weights) <= bound(n)
            sections += 1
    print('EXACT_CENTERED_AND_GENERAL_NORMALS_OK', sections)
    print('HYPERSIMPLEX_MAX_SECTION_OK')


if __name__ == '__main__':
    check()
