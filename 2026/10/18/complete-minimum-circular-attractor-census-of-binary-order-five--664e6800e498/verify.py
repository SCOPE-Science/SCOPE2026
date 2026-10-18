#!/usr/bin/env python3
"""Exact circular-attractor census for all binary order-five de Bruijn cycles.

Only Python's standard library is required. A row for each cycle is written to
census.csv; stdout records the independently checkable summary.
"""
from collections import Counter
from itertools import combinations
import csv
import hashlib

ORDER = 5
LENGTH = 1 << ORDER
ALL = (1 << LENGTH) - 1


def cycles():
    """Every length-32 Hamilton cycle of five-bit windows, anchored at 00000."""
    def walk(x, used, route):
        if len(route) == LENGTH:
            if 0 in (((x << 1) | 0) & 31, ((x << 1) | 1) & 31):
                yield ''.join(str(t >> 4) for t in route)
            return
        for bit in (0, 1):
            y = ((x << 1) | bit) & 31
            if not (used & (1 << y)):
                route.append(y)
                yield from walk(y, used | (1 << y), route)
                route.pop()
    yield from walk(0, 1, [0])


def mask_of(positions):
    ans = 0
    for p in positions:
        ans |= 1 << p
    return ans


def seven_position_candidates():
    """Exactly the 7-sets hitting all 32 cyclic windows of length five."""
    candidates = []
    for pp in combinations(range(LENGTH), 7):
        # The marked positions must have every clockwise cyclic gap <= 5.
        if max([b-a for a, b in zip(pp, pp[1:])] + [LENGTH + pp[0] - pp[-1]]) <= ORDER:
            candidates.append(mask_of(pp))
    return tuple(candidates)


def short_factor_coverage_masks(word):
    """For every short factor, union positions over *all* occurrences."""
    masks = []
    for size in range(1, ORDER):
        inc = {}
        for start in range(LENGTH):
            factor = ''.join(word[(start+j) % LENGTH] for j in range(size))
            posmask = mask_of(((start+j) % LENGTH for j in range(size)))
            inc[factor] = inc.get(factor, 0) | posmask
        assert len(inc) == (1 << size), (size, len(inc))
        masks.extend(inc.values())
    return tuple(masks)


def direct_all_length_check(word, mask):
    """Separate literal substring test for all 32 possible circular lengths."""
    for size in range(1, LENGTH+1):
        universe = set()
        hit = set()
        for start in range(LENGTH):
            s = ''.join(word[(start+j) % LENGTH] for j in range(size))
            universe.add(s)
            if any(mask & (1 << ((start+j) % LENGTH)) for j in range(size)):
                hit.add(s)
        if universe != hit:
            return False
    return True


def main():
    candidates = seven_position_candidates()
    assert len(candidates) == 384
    summary = Counter()
    rows = []
    for word in cycles():
        windows = [''.join(word[(s+j) % LENGTH] for j in range(ORDER))
                   for s in range(LENGTH)]
        assert len(set(windows)) == LENGTH
        assert windows.count('00000') == 1 and word[:5] == '00000'
        short = short_factor_coverage_masks(word)
        count = sum(all(C & M for M in short) for C in candidates)
        summary[count] += 1
        rows.append((word, count))
    assert len(rows) == len(set(w for w, count in rows)) == 2048
    assert sum(summary.values()) == 2048
    assert min(summary) == 216 and max(summary) == 368
    assert summary[216] == 4 and summary[368] == 2
    assert len(summary) == 120
    assert sum(size * multiplicity for size, multiplicity in summary.items()) == 589120
    # Fully independent direct circular-factor test on each extremal cycle.
    extremes = [word for word, count in rows if count in (216, 368)]
    assert len(extremes) == 6
    for word in extremes:
        short = short_factor_coverage_masks(word)
        for candidate in candidates:
            assert all(candidate & M for M in short) == direct_all_length_check(word, candidate)
    rows.sort()
    with open('census.csv', 'w', encoding='ascii', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(('canonical_word', 'number_of_size_seven_circular_attractors'))
        writer.writerows(rows)
    with open('census.csv', 'rb') as f:
        filehash = hashlib.sha256(f.read()).hexdigest()
    print('canonical cycles:', len(rows))
    print('valid size-seven candidate masks:', len(candidates))
    print('minimum attractor size for every cycle: 7')
    print('minimum optimal-set count:', min(summary), 'cycles:', summary[min(summary)])
    print('maximum optimal-set count:', max(summary), 'cycles:', summary[max(summary)])
    print('distinct optimal-set counts:', len(summary))
    print('aggregate optimal sets:', sum(k*v for k,v in summary.items()))
    print('minimum witnesses:', ','.join(w for w,c in rows if c == min(summary)))
    print('maximum witnesses:', ','.join(w for w,c in rows if c == max(summary)))
    print('full-factor independent cross-check: six extreme cycles x 384 candidate sets PASS')
    print('census.csv SHA-256:', filehash)
    print('ALL CHECKS PASS')

if __name__ == '__main__':
    main()
