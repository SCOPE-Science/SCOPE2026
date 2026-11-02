#!/usr/bin/env python3
"""Independent dynamic-state check: canonical greedy-subsequence counting."""
from itertools import product
from collections import Counter
from verify import exact_histogram


def count_via_greedy(w):
    n = len(w)
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            survivor = w[:i] + w[i + 1:j] + w[j + 1:]
            # Verify earliest greedy embedding retains precisely the complement
            # of the proposed deletion positions.
            k, kept = 0, []
            for pos, letter in enumerate(w):
                if k < len(survivor) and letter == survivor[k]:
                    kept.append(pos)
                    k += 1
            assert k == n - 2
            if set(range(n)) - set(kept) == {i, j}:
                count += 1
    return count


def run():
    for q, lim in [(2, 9), (3, 7), (4, 6), (5, 5)]:
        for n in range(2, lim + 1):
            hist = Counter(count_via_greedy(w)
                           for w in product(range(q), repeat=n))
            assert hist == exact_histogram(n, q), (n, q)
    print('CROSSCHECK_OK')


if __name__ == '__main__':
    run()
