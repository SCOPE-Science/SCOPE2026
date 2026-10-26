#!/usr/bin/env python3
"""Independent finite checks for distance-two mutual visibility in binary cubes."""
from itertools import combinations
from collections import Counter
from math import comb


def visible_two(S, d):
    """Check the original shortest-path requirement, using all length-two paths."""
    chosen = set(S)
    for a, b in combinations(S, 2):
        distance = (a ^ b).bit_count()
        if distance > 2:
            return False
        if distance == 2:
            mids = [a ^ (1 << i) for i in range(d) if (a ^ b) & (1 << i)]
            if not any(mid not in chosen for mid in mids):
                return False
    return True


def allowed_by_classification(S, d):
    s = set(S)
    for c in range(1 << d):
        ball = {c} | {c ^ (1 << i) for i in range(d)}
        if s <= ball:
            return True
    if len(s) != 4:
        return False
    # Enumerate all affine even-parity tetrahedra in three-coordinate faces.
    for ijk in combinations(range(d), 3):
        directions = [1 << i for i in ijk]
        for origin in range(1 << d):
            tet = {origin,
                   origin ^ directions[0] ^ directions[1],
                   origin ^ directions[0] ^ directions[2],
                   origin ^ directions[1] ^ directions[2]}
            if s == tet:
                return True
    return False


def coefficient(d, k):
    if k == 0:
        return 1
    if k == 1:
        return 1 << d
    if k == 2:
        return (1 << (d - 1)) * (d + comb(d, 2))
    term = (1 << d) * comb(d + 1, k) if k <= d + 1 else 0
    if k == 4:
        term += (1 << (d - 2)) * comb(d, 3)
    return term


def test_dimension(d, exhaustive):
    v = 1 << d
    samples = ( (tuple(i for i in range(v) if mask & (1 << i))
                  for mask in range(1 << v)) if exhaustive else
                (tuple(ss) for k in range(d + 2)
                 for ss in combinations(range(v), k)) )
    counts = Counter()
    tested = 0
    feasible = [] if d <= 4 else None
    for S in samples:
        actual = visible_two(S, d)
        classification = allowed_by_classification(S, d) if actual or len(S) <= 5 else False
        if actual != classification:
            raise AssertionError(('structural mismatch', d, S, actual, classification))
        if actual:
            counts[len(S)] += 1
            if feasible is not None:
                feasible.append(S)
        tested += 1
    for k in range(d + 2):
        assert counts[k] == coefficient(d, k), (d, k, counts[k], coefficient(d, k))
    if d <= 4:
        facets = Counter()
        for S in feasible:
            if not any(visible_two(S + (x,), d) for x in range(v) if x not in S):
                facets[len(S)] += 1
        assert facets == ({4: 10} if d == 3 else {4: 16, 5: 16}), facets
        print('DIMENSION_OK', d, 'subsets', tested, 'feasible', sum(counts.values()),
              'counts', [counts[k] for k in range(d+2)], 'facets', dict(facets))
    else:
        print('DIMENSION_OK', d, 'subsets', tested, 'feasible', sum(counts.values()),
              'counts', [counts[k] for k in range(d+2)])
    return tested

if __name__ == '__main__':
    total = test_dimension(3, True) + test_dimension(4, True) + test_dimension(5, False)
    print('VERIFICATION_OK subsets_checked=' + str(total))
