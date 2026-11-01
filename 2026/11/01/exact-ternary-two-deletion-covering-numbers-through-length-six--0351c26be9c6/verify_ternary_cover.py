#!/usr/bin/env python3
"""Exact integer verification of three ternary two-deletion covering numbers."""
from itertools import combinations, product

ALPHABET = '012'
C4 = ['1201', '2020']
C5 = ['01010', '12012', '12101', '20202', '20212']
BASE6 = ['010010', '010121', '010202']
C6 = [ ''.join(str((int(s) + k) % 3) for s in b)
       for b in BASE6 for k in range(3) ]
NEAR5 = ['01001', '12101', '20202', '10212']
WEIGHTS = {'0000': 2, '0001': 2, '0010': 1, '0011': 1,
           '0012': 2, '0101': 0, '0102': 0, '0110': 1,
           '0112': 1, '0120': 1}


def all_words(n):
    return [''.join(z) for z in product(ALPHABET, repeat=n)]


def descendants(word, r=2):
    return {''.join(word[i] for i in pos)
            for pos in combinations(range(len(word)), len(word)-r)}


def covers(codebook, n):
    union = set().union(*(descendants(w) for w in codebook))
    expected = set(all_words(n-2))
    assert union <= expected
    return len(union), expected - union


def pattern(w):
    first = {}
    return ''.join(str(first.setdefault(c, len(first))) for c in w)


def weight(w):
    p = min(pattern(w), pattern(w[::-1]))
    return WEIGHTS[p]


def mask(w, index):
    ans = 0
    for y in descendants(w):
        ans |= 1 << index[y]
    return ans


def verify():
    assert len(set(C4)) == 2 and len(set(C5)) == 5 and len(set(C6)) == 9
    for n, c in [(4, C4), (5, C5), (6, C6)]:
        count, missing = covers(c, n)
        assert count == 3**(n-2) and not missing
        print('cover', n, len(c), count)

    # At length four, one center has at most six two-letter subsequences,
    # whereas there are nine distinct two-letter words.
    assert max(len(descendants(w)) for w in all_words(4)) <= 6
    print('n4_single_center_max', max(len(descendants(w)) for w in all_words(4)))

    # At length five, any source containing aaa as a descendant must
    # contain at least three occurrences of a. Such majority types are
    # disjoint, so any putative four-word cover has one from each type.
    words = all_words(5)
    index = {y:i for i,y in enumerate(all_words(3))}
    masks = {w: mask(w,index) for w in words}
    majorities = [[w for w in words if w.count(a)>=3] for a in ALPHABET]
    assert [len(t) for t in majorities] == [51, 51, 51]
    assert len(set().union(*[set(x) for x in majorities])) == 153
    full = (1 << 27) - 1

    # Downward closure of the 243 possible fourth-center shadows.
    # A missing mask can be covered by that fourth center iff its mask is
    # in this set. This checks every possible final center exactly.
    downsets = set()
    for s in masks.values():
        sub = s
        while True:
            downsets.add(sub)
            if sub == 0:
                break
            sub = (sub - 1) & s

    triples = 0
    smallest_missing = 27
    for a in majorities[0]:
        for b in majorities[1]:
            ab = masks[a] | masks[b]
            for c in majorities[2]:
                triples += 1
                uncovered = full ^ (ab | masks[c])
                smallest_missing = min(smallest_missing, uncovered.bit_count())
                assert uncovered not in downsets, (a,b,c)
    assert triples == 51**3 == 132651
    covered, remaining = covers(NEAR5, 5)
    assert covered == 26 and len(remaining) == 1
    print('n5_three_majority_triples', triples, 'downset_masks', len(downsets),
          'near_cover', covered, 'missing_word', next(iter(remaining)))

    # Exact integer fractional-cover dual certificate at length six.
    target_weights = {y: weight(y) for y in all_words(4)}
    total = sum(target_weights.values())
    assert total == 90
    source_totals = [sum(target_weights[y] for y in descendants(w))
                     for w in all_words(6)]
    assert len(source_totals) == 729 and max(source_totals) == 11
    assert all(v <= 11 for v in source_totals)
    print('n6_weight_total', total, 'n6_max_shadow_weight', max(source_totals),
          'n6_source_types', len(source_totals))

    # A cover of cardinality k must obey 90 <= 11*k, so k >= 9.
    assert (total + 10)//11 == 9
    print('verified_exact_profile', [2,5,9])


if __name__ == '__main__':
    verify()
