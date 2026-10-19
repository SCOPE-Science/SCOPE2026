"""Independent exact checks of binary weight-three length-three deck enumeration.

Public reproducibility checker; Python standard library only. This finite checker
supplements, but does not replace, the unrestricted combinatorial proof.
"""
from collections import defaultdict
from itertools import combinations, product
from math import comb
from random import Random


def word(g):
    a, b, c, d = g
    return '0' * a + '1' + '0' * b + '1' + '0' * c + '1' + '0' * d


def triple_deck_by_dp(w):
    pats = [''.join(p) for p in product('01', repeat=3)]
    one = {'0': 0, '1': 0}
    two = {p: 0 for p in map(''.join, product('01', repeat=2))}
    three = {p: 0 for p in pats}
    for letter in w:
        for p in pats:
            if p[-1] == letter:
                three[p] += two[p[:2]]
        for p in two:
            if p[-1] == letter:
                two[p] += one[p[0]]
        one[letter] += 1
    return tuple(three[p] for p in pats)


def triple_deck_brute(w):
    pats = [''.join(p) for p in product('01', repeat=3)]
    counts = {p: 0 for p in pats}
    for inds in combinations(range(len(w)), 3):
        counts[''.join(w[i] for i in inds)] += 1
    return tuple(counts[p] for p in pats)


def gap_vectors(N):
    for a in range(N + 1):
        for b in range(N - a + 1):
            for c in range(N - a - b + 1):
                yield a, b, c, N - a - b - c


def explicit_partner(g):
    a, b, c, d = g
    delta = b - c
    if delta % 3:
        return None
    t = delta // 3
    if not t:
        return None
    other = (a + t, c, b, d - t)
    return other if min(other) >= 0 else None


def pair_count(N):
    return sum(N - 4 * t - 2 * c + 1
               for t in range(1, N // 4 + 1)
               for c in range((N - 4 * t) // 2 + 1))


def run():
    cases = 0
    vectors = 0
    for N in range(26):
        classes = defaultdict(list)
        for g in gap_vectors(N):
            w = word(g)
            sig = triple_deck_by_dp(w)
            if N <= 7:
                assert sig == triple_deck_brute(w), (N, g)
            assert sum(sig) == comb(N + 3, 3)
            classes[sig].append(g)
            vectors += 1
        assert max(map(len, classes.values())) <= 2
        pairs = [v for v in classes.values() if len(v) == 2]
        for pair in pairs:
            assert explicit_partner(pair[0]) == pair[1]
            assert explicit_partner(pair[1]) == pair[0]
        for class_ in classes.values():
            if len(class_) == 1:
                assert explicit_partner(class_[0]) is None
        P = pair_count(N)
        assert len(pairs) == P, (N, len(pairs), P)
        assert len(classes) == comb(N + 3, 3) - P
        cases += 1
    rng = Random(0xDA7311)
    for _ in range(500):
        N = rng.randrange(0, 200)
        cuts = sorted([0, N] + [rng.randint(0, N) for _ in range(3)])
        g = tuple(cuts[i + 1] - cuts[i] for i in range(4))
        deck = triple_deck_by_dp(word(g))
        companion = explicit_partner(g)
        if companion is not None:
            assert triple_deck_by_dp(word(companion)) == deck
        else:
            # Independently sample a different point on the same two-deck line.
            for t in (-2, -1, 1, 2):
                shifted = (g[0] + t, g[1] - 3*t, g[2] + 3*t, g[3] - t)
                if min(shifted) >= 0:
                    assert triple_deck_by_dp(word(shifted)) != deck
    print(f'WEIGHT3_3DECK_ALL_CHECKS_PASSED totals=0..25 profiles={vectors} random=500')

if __name__ == '__main__':
    run()
