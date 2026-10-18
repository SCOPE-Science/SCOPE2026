#!/usr/bin/env python3
"""Independent finite checks of the three-marker length-three scattered deck theorem.
No external packages or data dependencies. Python 3.10+.
"""
from collections import defaultdict
from itertools import combinations, product
from math import comb

PATS = [''.join(t) for k in (1, 2, 3) for t in product('01', repeat=k)]
PATS_DESC = sorted(PATS, key=lambda x: -len(x))

def measured_profile(n, places):
    # This is a scattered-subsequence dynamic program, not the proof's formulas.
    symbols = ['0'] * n
    for p in places:
        symbols[p] = '1'
    cnt = {'': 1}
    for bit in symbols:
        for pat in PATS_DESC:
            if pat[-1] == bit:
                cnt[pat] = cnt.get(pat, 0) + cnt.get(pat[:-1], 0)
    return tuple(cnt.get(pat, 0) for pat in PATS)

def coordinates_from_places(places):
    return tuple(p - i for i, p in enumerate(places))

def partner(n, places):
    a, b, c = coordinates_from_places(places)
    u, v = b - a, c - b
    if u == v or (u - v) % 3:
        return None
    shift = (u - v) // 3
    aa, bb, cc = a + shift, a + shift + v, a + shift + v + u
    if not (0 <= aa <= bb <= cc <= n - 3):
        return None
    return (aa, bb + 1, cc + 2)

def claimed_pairs(n):
    return sum(max(0, n - 2 - 2 * u - 4 * t)
               for t in range(1, n // 4 + 1)
               for u in range(n // 2 + 1))

def main():
    for n in range(3, 31):
        buckets = defaultdict(list)
        for places in combinations(range(n), 3):
            buckets[measured_profile(n, places)].append(places)
        assert all(len(c) <= 2 for c in buckets.values()), ('FIBER_GT_TWO', n)
        paired = [tuple(sorted(c)) for c in buckets.values() if len(c) == 2]
        assert len(paired) == claimed_pairs(n), ('PAIR_COUNT', n, len(paired), claimed_pairs(n))
        for cls in buckets.values():
            for places in cls:
                p = partner(n, places)
                assert p == (cls[0] if len(cls) == 2 and places == cls[1] else
                             cls[1] if len(cls) == 2 else None), ('PARTNER', n, places, cls, p)
        assert len(buckets) == comb(n, 3) - claimed_pairs(n), ('CLASS_COUNT', n)
        if n in (7, 8, 12, 20, 30):
            print('N', n, 'WORDS', comb(n, 3), 'DOUBLETONS', len(paired), 'CLASSES', len(buckets))
    for n in range(3, 1001):
        # Independently calculate the coefficient of x^n in x^7/[(1-x)^2(1-x^2)(1-x^4)]
        # via recurrence of accumulating convolution with 1/(1-x)^2.
        formula = claimed_pairs(n)
        gf_coeff = sum(n - (7 + 2 * u + 4 * v) + 1
                       for v in range(0, (n - 7) // 4 + 1)
                       for u in range(0, (n - 7 - 4 * v) // 2 + 1)) if n >= 7 else 0
        assert formula == gf_coeff, ('GF', n, formula, gf_coeff)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
