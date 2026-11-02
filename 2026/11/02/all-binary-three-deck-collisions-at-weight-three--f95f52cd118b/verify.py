#!/usr/bin/env python3
"""Independent exhaustive finite checks for the fixed-three-ones binary 3-deck theorem."""
from collections import defaultdict
from itertools import combinations, product
from math import comb


def deck(word):
    """Literal dynamic program for all length-three scattered subsequences."""
    counts = {'': 1}
    for symbol in word:
        nxt = counts.copy()
        for pat, multiplicity in counts.items():
            if len(pat) < 3:
                extended = pat + symbol
                nxt[extended] = nxt.get(extended, 0) + multiplicity
        counts = nxt
    return tuple(counts.get(''.join(t), 0) for t in product('01', repeat=3))


def gaps(word):
    parts = word.split('1')
    assert len(parts) == 4 and all(set(p) <= {'0'} for p in parts)
    return tuple(map(len, parts))


def partner(a, b, c, d):
    if b == c or (c - b) % 3:
        return None
    t = (c - b) // 3
    cand = (a - t, c, b, d + t)
    return cand if min(cand) >= 0 else None


def count_by_parameters(z):
    out = 0
    for t in range(1, z // 4 + 1):
        for b in range((z - 4*t) // 2 + 1):
            left = z - 4*t - 2*b
            # u+d=left with u,d nonnegative
            out += left + 1
    return out


def coefficients(zmax):
    # products x^4 (sum_u (u+1)x^u)(sum_t x^(2t))(sum_s x^(4s))
    return [count_by_parameters(z) for z in range(zmax + 1)]


def main():
    words_checked = 0
    classes_checked = 0
    pairs_checked = 0
    for z in range(16):
        n = z + 3
        groups = defaultdict(list)
        for ones in combinations(range(n), 3):
            symbols = ['0'] * n
            for i in ones:
                symbols[i] = '1'
            word = ''.join(symbols)
            groups[deck(word)].append(word)
            words_checked += 1
        classes_checked += len(groups)
        assert sum(map(len, groups.values())) == comb(n, 3)
        for members in groups.values():
            assert len(members) <= 2, (n, members)
            actual_gaps = {gaps(w) for w in members}
            for g in actual_gaps:
                pg = partner(*g)
                assert pg is None if len(members) == 1 else pg in actual_gaps, (n, members, g, pg)
            if len(members) == 2:
                pairs_checked += 1
        predicted = count_by_parameters(z)
        actual = sum(len(x) == 2 for x in groups.values())
        assert actual == predicted, (z, actual, predicted)
        assert len(groups) == comb(n, 3) - predicted, (n, len(groups), predicted)
    assert coefficients(12) == [0, 0, 0, 0, 1, 2, 4, 6, 10, 14, 20, 26, 35]
    print(f'VERIFY_OK zeros=0..15 words={words_checked} classes={classes_checked} doubletons={pairs_checked} signature_class_partner_and_gf=TRUE')

if __name__ == '__main__':
    main()
