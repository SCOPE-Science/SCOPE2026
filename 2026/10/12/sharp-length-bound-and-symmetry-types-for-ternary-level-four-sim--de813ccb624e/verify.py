#!/usr/bin/env python3
"""Exact finite quotient census for Simon's congruence, three symbols, level four.

Requires only Python 3 standard library. The state of a word is the set of
all its nonempty scattered subsequences of lengths at most four, encoded
as a 120-bit integer. Transition completeness is mathematical: appending
any of the three symbols is handled for every reached state.
"""
from collections import Counter, deque
from itertools import combinations, permutations, product

ALPHABET = '012'
K = 4
HISTOGRAM = (
    1, 3, 9, 27, 81, 240, 702, 2004, 5433, 13848,
    32031, 60942, 82918, 74160, 42615, 15435, 3357, 378, 18
)
ORBIT_SEEDS = (
    '001110022220011100',
    '001110022221100011',
    '001110222000211122',
)


def make_machine():
    words = [''.join(t) for n in range(1, K + 1)
             for t in product(ALPHABET, repeat=n)]
    number = {w: i for i, w in enumerate(words)}
    # For a final letter a, the new nonempty subsequences are {a} and
    # all ua where u was a nonempty old subsequence of length at most K-1.
    transitions = {}
    for a in ALPHABET:
        singleton = 1 << number[a]
        pairs = tuple((1 << number[w[:-1]], 1 << number[w])
                      for w in words if len(w) > 1 and w[-1] == a)
        transitions[a] = (singleton, pairs)
    assert len(words) == sum(3**j for j in range(1, K + 1)) == 120
    return number, transitions


def step(state, letter, transitions):
    singleton, pairs = transitions[letter]
    out = state | singleton
    for parent, added in pairs:
        if state & parent:
            out |= added
    return out


def signature(word, transitions):
    state = 0
    for a in word:
        state = step(state, a, transitions)
    return state


def independent_subsequence_signature(word, number):
    # Independent, position-combination definition, not the step recurrence.
    mask = 0
    for k in range(1, min(K, len(word)) + 1):
        for positions in combinations(range(len(word)), k):
            term = ''.join(word[i] for i in positions)
            mask |= 1 << number[term]
    return mask


def ranker_lengths(word):
    # Published forward-ranker recurrence, applied also from the right.
    counters = {a: 1 for a in ALPHABET}
    result = []
    for char in word:
        result.append(counters[char])
        counters[char] += 1
        bound = counters[char]
        for a in ALPHABET:
            counters[a] = min(counters[a], bound)
    return result


def run():
    number, transitions = make_machine()
    # Check transition semantics against definition on *every* word of
    # length at most seven, not just on farthest representatives.
    for n in range(0, 8):
        for tup in product(ALPHABET, repeat=n):
            w = ''.join(tup)
            assert signature(w, transitions) == independent_subsequence_signature(w, number)

    # Breadth first search of the entire finite quotient transition graph;
    # first visit is shortest, and alphabetic edge order selects shortlex.
    representative = {0: ''}
    todo = deque([0])
    levels = Counter({0: 1})
    edges = 0
    while todo:
        state = todo.popleft()
        w = representative[state]
        for a in ALPHABET:
            successor = step(state, a, transitions)
            edges += 1
            if successor not in representative:
                nw = w + a
                representative[successor] = nw
                levels[len(nw)] += 1
                todo.append(successor)

    observed = tuple(levels[i] for i in range(max(levels) + 1))
    assert observed == HISTOGRAM, (observed, HISTOGRAM)
    assert len(representative) == 334202 == sum(HISTOGRAM)
    assert edges == 3 * len(representative) == 1002606
    assert max(levels) == 18
    farthest = sorted(w for w in representative.values() if len(w) == 18)
    assert len(farthest) == 18

    # Independent subsequence enumeration confirms the masks of all
    # extremal representatives. The ranker criterion of Fleischer and
    # Kufleitner independently confirms their length-minimality.
    for w in farthest:
        assert signature(w, transitions) == independent_subsequence_signature(w, number)
        left = ranker_lengths(w)
        right = ranker_lengths(w[::-1])[::-1]
        assert all(x+y <= K+1 for x, y in zip(left, right))
        assert all(x+y == K+1 for x, y in zip(left, right))

    # Symmetry means simultaneous alphabet permutation or word reversal;
    # normal forms after permutation/reversal are recovered from the
    # quotient signature, since shortlex is not itself symmetry invariant.
    covered = set()
    orbits = []
    for seed in ORBIT_SEEDS:
        orbit = set()
        for p in permutations(ALPHABET):
            translated = ''.join(p[int(c)] for c in seed)
            for w in (translated, translated[::-1]):
                orbit.add(representative[signature(w, transitions)])
        assert len(orbit) == 6, (seed, orbit)
        assert all(len(w) == 18 for w in orbit)
        assert not covered.intersection(orbit)
        orbits.append(orbit)
        covered.update(orbit)
    assert covered == set(farthest)
    print('VERIFY_OK alphabet=3 level=4 classes=334202 max_minimal_length=18 extremal_classes=18 symmetry_orbits=3')
    print('HISTOGRAM', ','.join(map(str, observed)))
    print('SYMMETRY', ','.join(str(len(orbit)) for orbit in orbits))
    print('TRANSITIONS', edges, 'DIRECT_ORACLE', len(farthest), 'RANKER_CERTIFICATES', len(farthest), 'EXHAUSTIVE_SHORT_ORACLE', 3280)
    print('EXTREMAL_SHORTLEX', ' '.join(farthest))


if __name__ == '__main__':
    run()
