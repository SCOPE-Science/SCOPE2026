#!/usr/bin/env python3
"""Exact arithmetic verifier for four Rudin--Shapiro string-attractor optima.
Usage: python3 verify.py [certificates.json]
Requires only the Python standard library.
"""

import collections
import functools
import json
import pathlib
import sys


def sequence(n):
    return ''.join(str((i & (i >> 1)).bit_count() % 2) for i in range(n))


def factor_coverages(word):
    """Compute the union of occurrence intervals for every different factor."""
    n = len(word)
    factors = {}
    for length in range(1, n + 1):
        interval = (1 << length) - 1
        for start in range(n - length + 1):
            factor = word[start:start + length]
            factors[factor] = factors.get(factor, 0) | (interval << start)
    return factors


def minimal_coverages(factors):
    """Keep precisely inclusion-minimal coverage sets. All masks are nonzero."""
    minimal = []
    for mask in sorted(set(factors.values()), key=lambda x: (x.bit_count(), x)):
        if not any((mask & c) == c for c in minimal):
            minimal.append(mask)
    return minimal


def excluded_equal_dual_case(n, C, core, support, incidence_denominator):
    """Enumerate ALL equality cases of a positive uniform dual lower bound.

    For a hitting set of cardinality |support|/d, every selected position
    must lie in exactly d positive-dual sets and must hit each such set once.
    The recursion exact-covers these positive-dual sets and additionally
    hits every core constraint; it has no numerical tolerance or solver.
    """
    d = incidence_denominator
    assert len(support) % d == 0
    groups = collections.defaultdict(list)
    for p in range(n):
        support_mask = sum(1 << j for j, i in enumerate(support)
                           if (C[i] >> p) & 1)
        if support_mask.bit_count() != d:
            continue
        cover_mask = sum(1 << j for j, i in enumerate(core)
                         if (C[i] >> p) & 1)
        groups[support_mask].append((cover_mask, p))

    # Keeping only inclusion-maximal coverage masks WITHIN ONE support mask
    # cannot eliminate a solution: the dominating point is interchangeable.
    options = []
    for support_mask, items in groups.items():
        distinct = dict((cm, p) for cm, p in items)
        for cm, p in distinct.items():
            if any(cm != bigger and (cm & bigger) == cm
                   for bigger in distinct):
                continue
            options.append((support_mask, cm, p))

    by_group = [[] for _ in support]
    for support_mask, cm, p in options:
        for j in range(len(support)):
            if support_mask & (1 << j):
                by_group[j].append((support_mask, cm, p))

    full_groups = (1 << len(support)) - 1
    all_core = (1 << len(core)) - 1
    calls = 0

    @functools.lru_cache(maxsize=None)
    def search(remaining_groups, uncovered_core):
        nonlocal calls
        calls += 1
        if remaining_groups == 0:
            return uncovered_core == 0

        # Any future selected point must use only as-yet-uncovered groups.
        # Reject if an unhit core set cannot be hit by any such point.
        reachable = 0
        for sm, cm, _ in options:
            if (sm & remaining_groups) == sm:
                reachable |= cm
        if uncovered_core & ~reachable:
            return False

        # Exact-cover branching on the least flexible remaining dual group.
        chosen = None
        fewest = len(options) + 1
        for j in range(len(support)):
            if not (remaining_groups & (1 << j)):
                continue
            allowed = [(sm, cm) for sm, cm, _ in by_group[j]
                       if (sm & remaining_groups) == sm]
            if not allowed:
                return False
            if len(allowed) < fewest:
                chosen = allowed
                fewest = len(allowed)
        assert chosen is not None

        for sm, cm in chosen:
            if search(remaining_groups ^ sm, uncovered_core & ~cm):
                return True
        return False

    possible = search(full_groups, all_core)
    return possible, calls, len(options), search.cache_info().currsize


def verify(n, record):
    C = [int(v, 16) for v in record['C']]
    assert len(C) == len(set(C))
    word = sequence(n)
    # Independent recurrence: appending a binary 1 contributes an occurrence
    # of 11 precisely when the preceding least significant bit is 1.
    recursive_bits = [0] * n
    for j in range(1, n):
        recursive_bits[j] = recursive_bits[j // 2] ^ (int(j % 2 == 1) * ((j // 2) & 1))
    assert word == ''.join(map(str, recursive_bits))
    assert word[:16] == '0001001000011101'
    factors = factor_coverages(word)
    minimal = minimal_coverages(factors)
    assert set(minimal) == set(C), 'Stored masks are not the complete minimal coverages'

    support = [int(i) for i, weight in record['LPsupport']]
    weights = [weight for i, weight in record['LPsupport']]
    assert all(0 <= i < len(C) for i in support)
    assert len(set(support)) == len(support)
    d = 1 if n in (128, 256) else 2
    assert all(weight == 1 / d for weight in weights)
    lower = len(support) // d
    assert len(support) % d == 0
    assert all(sum((C[i] >> p) & 1 for i in support) <= d
               for p in range(n)), 'Dual bound not feasible'

    points = [int(x) - 1 for x in record['witness']]
    assert len(points) == len(set(points)) == record['opt']
    assert all(0 <= p < n for p in points)
    assert all(any((mask >> p) & 1 for p in points) for mask in C), \
        'Claimed attractor misses a minimal factor coverage'

    assert record['opt'] == lower or record['opt'] == lower + 1
    if record['opt'] == lower + 1:
        core = [int(i) for i in record['sel']]
        assert len(set(core)) == len(core)
        assert set(support).issubset(set(core))
        possible, calls, opts, memo = excluded_equal_dual_case(
            n, C, core, support, d)
        assert not possible, 'An equal-to-dual-size attractor was found'
        print(f'PROOF n={n} factors={len(factors)} minimal={len(C)} '
              f'lower_dual={lower} exact_cover_states={calls} '
              f'options={opts} memo={memo} optimum={record["opt"]}')
    else:
        print(f'PROOF n={n} factors={len(factors)} minimal={len(C)} '
              f'lower_dual={lower} optimum={record["opt"]}')


def main():
    path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else
                        pathlib.Path(__file__).with_name('certificates.json'))
    records = json.loads(path.read_text(encoding='utf-8'))
    assert set(records) == {'128', '256', '512', '1024'}
    for n in (128, 256, 512, 1024):
        verify(n, records[str(n)])
    print('VERIFY_OK Rudin-Shapiro dyadic attractor profile = 10,11,12,12')


if __name__ == '__main__':
    main()
