#!/usr/bin/env python3
"""Reproduce the shortest circular-rotation 3-deck ambiguity census.

Python 3, standard library only. Both independent signature routines use
exact integer counts of noncontiguous subsequences, never random sampling.
"""
from collections import Counter, defaultdict
from itertools import combinations, product

ALPHABET = '01'
K = 3
EXPECTED_NECKLACE_COUNTS = {1: 2, 2: 3, 3: 4, 4: 6, 5: 8, 6: 14, 7: 20, 8: 36}
EXPECTED_PROFILE_DISTRIBUTIONS = {
 1: {1: 2},
 2: {1: 2, 2: 1},
 3: {1: 2, 3: 2},
 4: {1: 2, 2: 1, 4: 3},
 5: {1: 2, 5: 6},
 6: {1: 2, 2: 1, 3: 2, 6: 9},
 7: {1: 2, 7: 18},
 8: {1: 2, 2: 1, 4: 3, 6: 2, 7: 1, 8: 27},
}
EXPECTED_BAD = {
 '00011011': [[(4, '10110001'), (6, '11000110')],
              [(5, '01100011'), (7, '10001101')]],
 '00100111': [[(1, '01001110'), (3, '00111001')],
              [(2, '10011100'), (4, '01110010')]],
 '00101101': [[(3, '01101001'), (7, '10010110')]],
}
EXPECTED_GLOBAL_DECK_COUNTS = {3: 8, 4: 16, 5: 32, 6: 64, 7: 126, 8: 247}


def all_words(n):
    return (''.join(t) for t in product(ALPHABET, repeat=n))


def patterns():
    return [''.join(p) for k in range(1, K + 1)
            for p in product(ALPHABET, repeat=k)]

PATTERNS = patterns()


def explicit_deck(word):
    """Direct definition: enumerate every increasing tuple of positions."""
    counts = Counter()
    for k in range(1, K + 1):
        for inds in combinations(range(len(word)), k):
            counts[''.join(word[i] for i in inds)] += 1
    return tuple(counts[p] for p in PATTERNS)


def recurrence_deck(word):
    """Independent left-to-right prefix-subsequence recurrence."""
    acc = {'': 1}
    for character in word:
        for pattern, multiplicity in tuple(acc.items()):
            if len(pattern) < K:
                longer = pattern + character
                acc[longer] = acc.get(longer, 0) + multiplicity
    return tuple(acc.get(p, 0) for p in PATTERNS)


def rotate(word, cut):
    return word[cut:] + word[:cut]


def necklace(word):
    return min(rotate(word, i) for i in range(len(word)))


def census():
    stats = {}
    for n in range(1, 9):
        representatives = sorted(set(necklace(w) for w in all_words(n)))
        assert len(representatives) == EXPECTED_NECKLACE_COUNTS[n]
        sizes = Counter()
        bad = {}
        for w in representatives:
            signature_buckets = defaultdict(list)
            for cut in range(n):
                v = rotate(w, cut)
                d1 = explicit_deck(v)
                d2 = recurrence_deck(v)
                assert d1 == d2, (w, cut, d1, d2)
                signature_buckets[d1].append((cut, v))
            sizes[len(signature_buckets)] += 1
            collisions = sorted(
                (sorted(bucket) for bucket in signature_buckets.values()
                 if len({v for _, v in bucket}) > 1),
                key=lambda bucket: bucket[0][0]
            )
            if collisions:
                bad[w] = collisions
        assert dict(sizes) == EXPECTED_PROFILE_DISTRIBUTIONS[n], (n, sizes)
        assert bad == (EXPECTED_BAD if n == 8 else {}), (n, bad)
        stats[n] = (len(representatives), len(bad), dict(sorted(sizes.items())))
    for n, expected in EXPECTED_GLOBAL_DECK_COUNTS.items():
        deck_types = {explicit_deck(w) for w in all_words(n)}
        assert len(deck_types) == expected, (n, len(deck_types), expected)
    return stats


if __name__ == '__main__':
    result = census()
    for n, (necklaces, bad, dist) in result.items():
        print('n=%d necklaces=%d ambiguous_necklaces=%d profile_distribution=%s'
              % (n, necklaces, bad, dist))
    print('CHECKED n=1..8, 510 binary words, all indexed rotations, two deck methods')
    print('VERIFY_OK')
