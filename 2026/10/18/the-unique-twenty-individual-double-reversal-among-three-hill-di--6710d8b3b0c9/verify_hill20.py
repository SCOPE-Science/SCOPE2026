"""Exact, independent finite-census check for three Hill-order rankings.

Standard library only; run with python3 verify_hill20.py.
No floating-point comparisons determine any conclusion.
"""
from collections import defaultdict
from math import prod

LIMIT = 20


def nonincreasing_partitions(total, ceiling=None):
    """Enumerate integer partitions once, with largest part first."""
    if ceiling is None:
        ceiling = total
    if total == 0:
        yield ()
    else:
        for first in range(min(ceiling, total), 0, -1):
            for tail in nonincreasing_partitions(total - first, first):
                yield (first,) + tail


def partition_counts_by_coins(limit):
    """Separate unbounded-coin DP for counts of integer partitions."""
    counts = [0] * (limit + 1)
    counts[0] = 1
    for coin in range(1, limit + 1):
        for amount in range(coin, limit + 1):
            counts[amount] += counts[amount - coin]
    return counts


def signatures(profile):
    return (sum(v * v for v in profile),
            prod(pow(v, v) for v in profile), profile[0])


def is_strict_reversal(a, b):
    sa, ea, ma = signatures(a)
    sb, eb, mb = signatures(b)
    # D1(a)<D1(b), D2(a)>D2(b), Dinf(a)<Dinf(b)
    return ea > eb and sa < sb and ma > mb


def check():
    predicted = partition_counts_by_coins(LIMIT)
    pair_checks = 0
    boundary = []
    for total in range(1, LIMIT + 1):
        parts = list(nonincreasing_partitions(total))
        assert len(parts) == predicted[total], (total, len(parts), predicted[total])
        assert len(set(parts)) == len(parts)
        assert all(sum(p) == total and all(v > 0 for v in p)
                   and tuple(sorted(p, reverse=True)) == p for p in parts)
        by_richness = defaultdict(list)
        for p in parts:
            by_richness[len(p)].append(p)
        witnesses = []
        for richness, profiles in by_richness.items():
            for idx, a in enumerate(profiles):
                for b in profiles[idx + 1:]:
                    pair_checks += 1
                    if is_strict_reversal(a, b):
                        witnesses.append((richness, a, b))
                    if is_strict_reversal(b, a):
                        witnesses.append((richness, b, a))
        if total < LIMIT:
            assert not witnesses, (total, witnesses)
        else:
            boundary = witnesses
            assert boundary == [(4, (9, 6, 4, 1), (8, 8, 2, 2))], boundary
    a = (9, 6, 4, 1)
    b = (8, 8, 2, 2)
    assert signatures(a) == (134, 4627325525704704, 9)
    assert signatures(b) == (136, 4503599627370496, 8)
    assert is_strict_reversal(a, b)
    print('PASS: integer partitions 1..20 independently counted via coin DP')
    print('PASS: distinct equal-richness unordered profile pairs checked:', pair_checks)
    print('PASS: no strict reversed triple at census <20')
    print('PASS: exactly one ordered witness at census 20:', boundary)
    print('PASS: exact entropy, Simpson, and dominance comparisons')


if __name__ == '__main__':
    check()
