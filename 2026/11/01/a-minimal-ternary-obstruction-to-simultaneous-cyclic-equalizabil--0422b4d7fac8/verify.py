#!/usr/bin/env python3
"""Independent exhaustive checks for the cyclic distance-two symbol-pair lemma.
No bound here is used as a proof of the unrestricted assertion.
"""
from itertools import product


def rotate(word, shift):
    return word[shift:] + word[:shift]


def pair_at_distance_two(word, other):
    mismatch = [i for i, (x, y) in enumerate(zip(word, other)) if x != y]
    if len(mismatch) != 2:
        return None
    x, y = mismatch
    assert word[x] == other[y] and word[y] == other[x]
    assert word[x] != word[y]
    return frozenset((word[x], word[y]))


def check(q, n):
    nwords = 0
    nclose = 0
    for word in product(range(q), repeat=n):
        nwords += 1
        pair_types = set()
        for s in range(1, n):
            other = rotate(word, s)
            typ = pair_at_distance_two(word, other)
            if typ is not None:
                pair_types.add(typ)
                nclose += 1
        assert len(pair_types) <= 1, (q, n, word, pair_types)
    return nwords, nclose


def direct_counterexample():
    u, v, w = tuple(map(tuple, ('012', '021', '120')))
    assert set(u) == set(v) == set(w)
    pair_1 = pair_at_distance_two(u, v)
    pair_2 = pair_at_distance_two(v, w)
    assert pair_1 == frozenset(('1','2'))
    assert pair_2 == frozenset(('0','1'))
    assert pair_1 != pair_2
    for n in range(3, 40):
        # A common insertion of 0's at fixed positions preserves both
        # original disagreement symbol types and their cardinality.
        pad = '0' * (n-3)
        u1, v1, w1 = tuple(tuple(x+pad) for x in ('012', '021', '120'))
        assert pair_at_distance_two(u1,v1) == pair_1
        assert pair_at_distance_two(v1,w1) == pair_2
    return True

if __name__ == '__main__':
    assert direct_counterexample()
    print('COUNTEREXAMPLE_OK 012 021 120; padded length 3..39')
    for q, max_n in ((2, 12),(3, 10),(4, 8)):
        for n in range(2, max_n+1):
            words,close = check(q,n)
            print(f'ALPHABET={q} LENGTH={n} WORDS={words} DISTANCE_TWO_ROTATIONS={close} CHECK=PASS')
    print('ALL_FINITE_CHECKS_PASS')
