#!/usr/bin/env python3
"""Exact independent enumeration of four-agent RSD outcome multiplicities.

Fixes the first strict ranking by a unique object relabeling; all other
rankings vary independently over the 24 permutations. Each canonical case
represents exactly 24 labeled strict-preference profiles.

Uses both a priority-list simulation and an independent recursive
choice-tree evaluation, comparing complete matching counters in every case.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import csv

ORDERS = tuple(permutations(range(4)))
EXPECTED_SUPPORT = {1: 31104, 2: 20736, 3: 20736, 4: 53856,
                    5: 48384, 6: 40032, 7: 45504, 8: 26568,
                    9: 12672, 10: 15120, 11: 6336, 12: 5880,
                    14: 4032, 16: 216, 18: 576, 24: 24}


def serial_outcome(profile, order):
    remaining = set(range(4))
    assigned = [None] * 4
    for agent in order:
        for item in profile[agent]:
            if item in remaining:
                assigned[agent] = item
                remaining.remove(item)
                break
    assert not remaining
    return tuple(assigned)


def recurse_counts(profile):
    counts = Counter()
    assigned = [-1] * 4
    def walk(remaining_agents, available):
        if not remaining_agents:
            counts[tuple(assigned)] += 1
            return
        for agent in remaining_agents:
            for item in profile[agent]:
                if available & (1 << item):
                    assigned[agent] = item
                    walk(tuple(a for a in remaining_agents if a != agent), available ^ (1 << item))
                    assigned[agent] = -1
                    break
    walk((0, 1, 2, 3), 15)
    return counts


def read_spectrum_csv(path):
    with path.open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 57
    results = {}
    for row in rows:
        shape = tuple(map(int, row['multiplicities'].split(';')))
        profiles = int(row['labeled_profiles'])
        assert sum(shape) == 24 and all(x > 0 for x in shape)
        assert tuple(sorted(shape, reverse=True)) == shape
        assert shape not in results
        results[shape] = profiles
    return results


def main():
    root = Path(__file__).resolve().parent
    shape_hist = Counter()
    support_hist = Counter()
    witness = {}
    for ranks in product(ORDERS, repeat=3):
        profile = (ORDERS[0],) + ranks
        one = Counter(serial_outcome(profile, order) for order in ORDERS)
        two = recurse_counts(profile)
        assert one == two, profile
        assert sum(one.values()) == 24
        shape = tuple(sorted(one.values(), reverse=True))
        shape_hist[shape] += 24  # exactly 24 object relabelings
        support_hist[len(shape)] += 24
        witness.setdefault(len(shape), tuple(ORDERS.index(r) for r in profile))

    assert len(shape_hist) == 57
    assert dict(sorted(support_hist.items())) == EXPECTED_SUPPORT
    assert sum(shape_hist.values()) == 24 ** 4
    csv_hist = read_spectrum_csv(root / 'spectrum.csv')
    assert dict(shape_hist) == csv_hist
    for shape, count in csv_hist.items():
        assert count % 24 == 0
    with (root / 'support_histogram.csv').open(newline='', encoding='utf-8') as f:
        data = list(csv.DictReader(f))
    assert {int(row['support_size']): int(row['labeled_profiles']) for row in data} == EXPECTED_SUPPORT
    with (root / 'support_witnesses.csv').open(newline='', encoding='utf-8') as f:
        data = list(csv.DictReader(f))
    assert len(data) == len(witness)
    for row in data:
        k = int(row['support_size'])
        pref_idx = tuple(int(x) for x in row['ranking_indices'].split(';'))
        assert pref_idx == witness[k]
        profile = tuple(ORDERS[j] for j in pref_idx)
        assert len(set(serial_outcome(profile, order) for order in ORDERS)) == k
    first = Fraction(sum(k*v for k, v in support_hist.items()), 24**4)
    second = Fraction(sum(k*k*v for k, v in support_hist.items()), 24**4)
    assert first == Fraction(1597, 288)
    assert second - first*first == Fraction(684839, 82944)
    assert support_hist[24] == 24 and support_hist[1] == 31104
    print('VERIFY_OK canonical_profiles=13824 labeled_profiles=331776 priority_orders=24')
    print('VERIFY_OK independent_exact_algorithms=2 probability_shapes=57 support_sizes=16')
    print('VERIFY_OK mean_support=1597/288 variance=684839/82944 complete_spectrum_csv=57')

if __name__ == '__main__':
    main()
