#!/usr/bin/env python3
"""Definition-based verification for minimum zero-forcing sets of cycle powers.

No third-party libraries. All vertex subsets of the alleged optimal cardinality
are tested for the selected small parameters; the infinite assertion is proved
separately in RESULT.md.
"""
from itertools import combinations
from collections import deque


def neighbors(n, k):
    return [sum(1 << j for j in range(n)
                if j != i and min((j - i) % n, (i - j) % n) <= k)
            for i in range(n)]


def forces_all(nb, initial):
    n = len(nb)
    full = (1 << n) - 1
    colored = initial
    while colored != full:
        nxt = colored
        for i in range(n):
            if colored & (1 << i):
                white = nb[i] & (full ^ colored)
                if white and not (white & (white - 1)):
                    nxt |= white
        if nxt == colored:
            return False
        colored = nxt
    return True


def family(n, k, nb):
    if n <= 2 * k + 1:
        return {(1 << n) - 1 ^ (1 << a) for a in range(n)}, n - 1, n
    if n == 2 * k + 2:
        forms = {(1 << n) - 1 ^ (1 << a) ^ (1 << b)
                 for a, b in combinations(range(n), 2)
                 if nb[a] & (1 << b)}
        return forms, n - 2, n * k
    forms = {(nb[v] | (1 << v)) & ~(1 << w)
             for v in range(n)
             for w in range(n) if nb[v] & (1 << w)}
    return forms, 2 * k, n * (2 * k - 1)


def connected_by_swaps(forms):
    if len(forms) <= 1:
        return True
    remaining = set(forms)
    root = remaining.pop()
    queue = deque([root])
    while queue:
        a = queue.popleft()
        for b in tuple(remaining):
            if (a ^ b).bit_count() == 2:
                remaining.remove(b)
                queue.append(b)
    return not remaining


def main():
    tests = 0
    subsets = 0
    for n in range(3, 16):
        for k in range(1, n):
            nb = neighbors(n, k)
            predicted, optimum, predicted_count = family(n, k, nb)
            assert len(predicted) == predicted_count, (n, k, 'count')
            observed = set()
            for inds in combinations(range(n), optimum):
                s = sum(1 << i for i in inds)
                subsets += 1
                if forces_all(nb, s):
                    observed.add(s)
            assert predicted == observed, (n, k, 'classification')
            if optimum > 1:
                # Certificate of the lower bound: no smaller set can make
                # the first force if its size is below minimum degree.
                assert min(m.bit_count() for m in nb) == optimum, (n, k, 'lower bound')
            assert connected_by_swaps(predicted), (n, k, 'reconfiguration')
            tests += 1
    # Independent high-parameter, non-exhaustive structural checks.
    larger = 0
    for k in (3, 6, 11, 17, 31):
        for n in (2*k+1, 2*k+2, 2*k+3, 3*k+7, 4*k+12):
            nb = neighbors(n, k)
            predicted, optimum, predicted_count = family(n, k, nb)
            assert len(predicted) == predicted_count
            assert all(forces_all(nb, s) for s in predicted)
            assert connected_by_swaps(predicted)
            larger += 1
    print('VERIFICATION_OK exhaustive_parameter_pairs=%d candidate_subsets=%d enlarged_cases=%d' % (tests, subsets, larger))


if __name__ == '__main__':
    main()
