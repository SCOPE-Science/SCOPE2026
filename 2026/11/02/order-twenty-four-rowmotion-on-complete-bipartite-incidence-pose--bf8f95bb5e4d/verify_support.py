#!/usr/bin/env python3
"""Finite support certificate for classical rowmotion on incidence posets K_{2,n}."""
from collections import Counter
from itertools import combinations

EXPECTED = {
    2: {1: 2, 2: 1},
    3: {1: 3, 3: 1},
    4: {2: 4},
    6: {3: 3, 4: 5, 5: 1},
    8: {1: 8, 2: 12},
    24: {3: 8},
}

def allowed(left, x):
    r, ta, tb = x & 1, (x >> 1) & 1, (x >> 2) & 1
    return not ((ta and not (r and (left & 1))) or
                (tb and not (r and (left & 2))))

def direct_rowmotion(ideal, lowers, size):
    # All elements not in an ideal with no missing lower cover are minimal
    # in the complement. Build the ideal they generate.
    generators = [v for v in range(size)
                  if not ((ideal >> v) & 1)
                  and all((ideal >> w) & 1 for w in lowers[v])]
    output = 0
    for v in generators:
        output |= 1 << v
        for w in lowers[v]:
            output |= 1 << w
    return output

def representative_period(left, column_types):
    k = len(column_types)
    # Minimal elements: left vertices 0,1; right vertices 2..k+1.
    # Maximal elements: edge (a,j) at 2+k+2*j+a.
    count = 2 + 3*k
    lowers = [[] for _ in range(count)]
    for j in range(k):
        for a in range(2):
            lowers[2+k+2*j+a] = [a, 2+j]
    initial = left
    for j, x in enumerate(column_types):
        if x & 1:
            initial |= 1 << (2+j)
        for a in range(2):
            if (x >> (a+1)) & 1:
                initial |= 1 << (2+k+2*j+a)
    state = initial
    for period in range(1, 49):
        state = direct_rowmotion(state, lowers, count)
        if state == initial:
            return period
    raise AssertionError('period exceeded 48')

def main():
    census = Counter()
    for left in range(4):
        typ = [x for x in range(8) if allowed(left, x)]
        for k in range(1, len(typ)+1):
            for support in combinations(typ, k):
                d = representative_period(left, support)
                census[d, k] += 1
    by_period = {d: {k: census[d,k] for k in range(1,6) if census[d,k]}
                 for d in sorted(set(d for d,_ in census))}
    assert by_period == EXPECTED, (by_period, EXPECTED)
    assert sum(census.values()) == 48
    print('SUPPORT_PERIOD_CERTIFICATE_OK supports=48')
    print('period_by_support_size=',by_period)

if __name__ == '__main__':
    main()
