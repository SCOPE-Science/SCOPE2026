"""Finite verification of the length-eight binary three-request recovery classification.
Requires Python 3.10+ standard library only. Run beside witnesses.json.
"""
import itertools
import collections
import json
from pathlib import Path

UNITS = (1, 2, 4)


def minimal_sets(columns):
    """Enumerate all inclusion-minimal recovery sets for the three named requests."""
    n = len(columns)
    xors = [0] * (1 << n)
    found = []
    for mask in range(1, 1 << n):
        low = mask & -mask
        xors[mask] = xors[mask ^ low] ^ columns[low.bit_length() - 1]
        if mask.bit_count() > 3 or xors[mask] not in UNITS:
            continue
        proper = (mask - 1) & mask
        while proper and xors[proper] != xors[mask]:
            proper = (proper - 1) & mask
        if not proper:
            found.append((mask, UNITS.index(xors[mask])))
    return found


def maximal_exchange_core(recoveries):
    """Greatest fixed point of the exchange-closed complete-history operator."""
    complete = set()
    for a, b, c in itertools.combinations(range(len(recoveries)), 3):
        am, bm, cm = (recoveries[j][0] for j in (a, b, c))
        if (am & bm) == (am & cm) == (bm & cm) == 0:
            complete.add((a, b, c))
    while complete:
        extensions = collections.defaultdict(set)
        for triple in complete:
            for j in range(3):
                pair = tuple(triple[l] for l in range(3) if l != j)
                extensions[pair].add(recoveries[triple[j]][1])
        keep = {
            triple for triple in complete
            if all(len(extensions[tuple(triple[l] for l in range(3) if l != j)]) == 3
                   for j in range(3))
        }
        if keep == complete:
            break
        complete = keep
    return complete


def check_strong_witness(columns, chosen):
    all_sets = set(minimal_sets(columns))
    by_mask = {mask: color for mask, color in all_sets}
    assert len(chosen) == len(set(chosen))
    assert all(mask in by_mask for mask in chosen)
    assert set(by_mask[mask] for mask in chosen) == {0, 1, 2}
    # Check every chosen set or disjoint chosen pair can be extended
    # to a disjoint chosen set for any of the three request symbols.
    for size in (0, 1, 2):
        for history in itertools.combinations(chosen, size):
            if any(a & b for a, b in itertools.combinations(history, 2)):
                continue
            occupied = 0
            for mask in history:
                occupied |= mask
            for color in (0, 1, 2):
                assert any(by_mask[mask] == color and (mask & occupied) == 0
                           for mask in chosen), (columns, history, color)


def main():
    data = json.loads(Path(__file__).with_name('witnesses.json').read_text(encoding='utf-8'))
    assert len(data) == 79
    table = {tuple(row['columns']): row['chosen_masks'] for row in data}
    assert len(table) == 79
    encountered = []
    stats = collections.Counter()
    for n in (7, 8):
        good = []
        for columns in itertools.combinations_with_replacement(range(1, 8), n):
            recoveries = minimal_sets(columns)
            if maximal_exchange_core(recoveries):
                good.append(columns)
                if n == 8:
                    assert columns in table
                    check_strong_witness(columns, table[columns])
                    counts = tuple(sorted(collections.Counter(columns).values()))
                    stats[counts] += 1
        if n == 7:
            assert len(good) == 0, good
        else:
            assert len(good) == 79, len(good)
            assert set(good) == set(table)
            encountered = good
    # Permuting the three named information coordinates (S_3) and
    # the stored-coordinate positions gives the natural equivalence relation.
    def relabel(value, permutation):
        return sum(1 << permutation[j] for j in range(3) if value & (1 << j))

    unseen = set(encountered)
    orbit_sizes = []
    while unseen:
        representative = min(unseen)
        orbit = {tuple(sorted(relabel(x, p) for x in representative))
                 for p in itertools.permutations(range(3))}
        assert orbit.issubset(set(encountered))
        unseen.difference_update(orbit)
        orbit_sizes.append(len(orbit))
    assert collections.Counter(orbit_sizes) == {6: 10, 3: 6, 1: 1}
    assert stats == {
        (1, 1, 1, 1, 2, 2): 48,
        (1, 1, 2, 2, 2): 24,
        (1, 1, 1, 1, 1, 1, 2): 7,
    }, stats
    print('VERIFY_OK: n=7 none; n=8 exactly 79 in 17 message-permutation classes; all 79 strong witnesses; profiles 48+24+7')


if __name__ == '__main__':
    main()
