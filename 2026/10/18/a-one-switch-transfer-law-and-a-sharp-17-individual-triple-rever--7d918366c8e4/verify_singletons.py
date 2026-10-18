#!/usr/bin/env python3
"""Exact finite checks for singleton-curve crossings under abundance majorization.

Scientific conventions: populations have positive integer species counts; all samples
are uniformly selected without replacement.  This program checks the entire finite
classification through census size 17; its output is not an infinite-case proof.
"""
from functools import lru_cache
from itertools import combinations
from math import comb


def choose(n, r):
    return comb(n, r) if 0 <= r <= n else 0


@lru_cache(None)
def partitions_below(total, cap):
    if total == 0:
        return ((),)
    result = []
    for leading in range(min(total, cap), 0, -1):
        for rest in partitions_below(total - leading, leading):
            result.append((leading,) + rest)
    return tuple(result)


def partitions(n):
    return partitions_below(n, n)


def majorizes(large, small):
    if len(large) != len(small) or sum(large) != sum(small):
        return False
    return large != small and all(
        sum(large[:j]) >= sum(small[:j])
        for j in range(1, len(large))
    )


def numerators(profile, total):
    return tuple(
        sum(a * choose(total - a, m - 1) for a in profile)
        for m in range(1, total + 1)
    )


def sign_transitions(values):
    s = [1 if x > 0 else -1 for x in values if x]
    return sum(x != y for x, y in zip(s, s[1:]))


def census(upper=17):
    stats = []
    violations = []
    for total in range(2, upper + 1):
        classified = {}
        for profile in partitions(total):
            classified.setdefault(len(profile), []).append((profile, numerators(profile, total)))
        compared = 0
        anomalous = 0
        for length, items in classified.items():
            for original, before in items:
                for balanced, after in items:
                    if not majorizes(original, balanced):
                        continue
                    compared += 1
                    differences = tuple(y - x for x, y in zip(before, after))
                    flips = sign_transitions(differences)
                    if flips >= 2:
                        anomalous += 1
                        violations.append((total, original, balanced, flips, differences))
        stats.append((total, len(partitions(total)), compared, anomalous))
    return stats, violations


def independent_subset_numerators(profile):
    """Count exact singleton totals directly among all 2^N labelled subsets."""
    labels = tuple(i for i, a in enumerate(profile) for _ in range(a))
    total = len(labels)
    acc = [0] * (total + 1)
    for mask in range(1 << total):
        occurrences = [0] * len(profile)
        size = 0
        for i in range(total):
            if mask & (1 << i):
                size += 1
                occurrences[labels[i]] += 1
        acc[size] += sum(x == 1 for x in occurrences)
    return tuple(acc[1:])


def transfer_delta(n, a, b):
    return tuple(
        (a - 1) * choose(n - a + 1, m - 1)
        + (b + 1) * choose(n - b - 1, m - 1)
        - a * choose(n - a, m - 1)
        - b * choose(n - b, m - 1)
        for m in range(1, n + 1)
    )


def check_local_polynomial():
    # Prove/check the generating polynomial coefficients against the closed formula.
    checked = 0
    for n in range(3, 28):
        for a in range(3, n):
            for b in range(1, a - 1):
                if a + b > n:
                    continue
                d = a - b - 1
                M = n - a
                # q(z) = (a-1)(1+z)-a + (b+1)(1+z)^d-b(1+z)^(d+1)
                q = [(a - 1) * choose(1, j) - (a if j == 0 else 0)
                     + (b + 1) * choose(d, j) - b * choose(d + 1, j)
                     for j in range(d + 2)]
                polynomial = tuple(sum(choose(M, k - j) * q[j]
                                       for j in range(len(q)))
                                   for k in range(n))
                actual = transfer_delta(n, a, b)
                assert actual == polynomial, (n, a, b)
                assert q[0] == 0 and q[1] == 2 * d and q[-1] == -b
                assert actual[1] > 0 and actual[n - b] < 0
                assert sign_transitions(actual) == 1, (n, a, b, actual)
                checked += 1
    return checked


def main():
    stats, examples = census(17)
    print('N, partitions, ordered strict-majorization pairs (same richness), pairs with >=2 strict sign reversals')
    for row in stats:
        print(*row, sep=',')
    assert sum(e[0] < 17 for e in examples) == 0
    assert len(examples) == 1
    assert examples[0][:4] == (17, (9, 4, 3, 1), (7, 6, 2, 2), 3)
    n, x, y, flips, diff = examples[0]
    assert diff == (0, 14, 108, 350, 597, 522, 129, -112, 9, 114, -70,
                    -306, -325, -186, -63, -12, -1)
    print('Unique minimal witness:', x, '=>', y)
    print('Exact numerator differences:', diff)
    before = independent_subset_numerators(x)
    after = independent_subset_numerators(y)
    assert tuple(b - a for a, b in zip(before, after)) == diff
    assert before == numerators(x, 17)
    assert after == numerators(y, 17)
    print('Independent direct enumeration:', 2 * 2**17, 'labelled subsets verified')
    count = check_local_polynomial()
    print('Exact local generating identity and one-switch examples:', count)
    print('ALL CHECKS PASS')


if __name__ == '__main__':
    main()
