#!/usr/bin/env python3
"""Deterministic exhaustive certificate for binary three-separated decks.

Run with Python 3: python verify.py
No third-party packages or probabilistic fingerprints are used.
"""
from collections import defaultdict
from itertools import combinations, product
from pathlib import Path
import csv

MIN_LENGTH = 7
MAX_LENGTH = 17
GAP = 3
MAX_SUBSEQ_LENGTH = 3


def initial_state():
    return [[1]] + [[0] * (1 << j) for j in range(1, MAX_SUBSEQ_LENGTH + 1)]


def extend(states, bit):
    """Return exact deck counts after appending one binary symbol.

    states[j] is the profile of the first j symbols. If the new position
    is i+1, its predecessor may be no later than i-2.
    """
    i = len(states) - 1
    output = [layer[:] for layer in states[i]]
    eligible = states[max(0, i - 2)]
    for length in range(1, MAX_SUBSEQ_LENGTH + 1):
        for prefix_value, count in enumerate(eligible[length - 1]):
            output[length][2 * prefix_value + bit] += count
    return output


def flatten(state):
    return tuple(value for layer in state[1:] for value in layer)


def direct_deck(word):
    """Independent literal index enumeration, not using the DP recurrence."""
    n = len(word)
    result = []
    for length in range(1, MAX_SUBSEQ_LENGTH + 1):
        counts = [0] * (1 << length)
        for inds in combinations(range(n), length):
            if any(inds[j] - inds[j - 1] < GAP for j in range(1, length)):
                continue
            pat = 0
            for i in inds:
                pat = 2 * pat + int(word[i])
            counts[pat] += 1
        result.extend(counts)
    return tuple(result)


def complement(word):
    return ''.join('1' if bit == '0' else '0' for bit in word)


def normalized_pair(pair):
    return tuple(sorted(pair))


def dihedral_orbit(pair):
    a, b = pair
    return {
        normalized_pair((a, b)),
        normalized_pair((a[::-1], b[::-1])),
        normalized_pair((complement(a), complement(b))),
        normalized_pair((complement(a[::-1]), complement(b[::-1]))),
    }


def full_census():
    first = {n: {} for n in range(MIN_LENGTH, MAX_LENGTH + 1)}
    collided = {n: set() for n in range(MIN_LENGTH, MAX_LENGTH + 1)}
    pairs = defaultdict(list)
    states = [initial_state()]

    def traverse(depth, word_index):
        if depth >= MIN_LENGTH:
            key = flatten(states[-1])
            prior = first[depth].get(key)
            if prior is None:
                first[depth][key] = word_index
            else:
                assert key not in collided[depth], 'fiber larger than two'
                collided[depth].add(key)
                pairs[depth].append((prior, word_index))
        if depth == MAX_LENGTH:
            return
        for bit in (0, 1):
            states.append(extend(states, bit))
            traverse(depth + 1, (word_index << 1) | bit)
            states.pop()

    traverse(0, 0)
    results = []
    for n in range(MIN_LENGTH, MAX_LENGTH + 1):
        class_count = len(first[n])
        duplicate_count = len(pairs[n])
        assert class_count + duplicate_count == 1 << n
        assert duplicate_count == (16 if n == 17 else 0)
        assert class_count == ((1 << n) - 16 if n == 17 else 1 << n)
        results.append((n, class_count, duplicate_count))

    observed_pairs = {
        normalized_pair((format(a, '017b'), format(b, '017b')))
        for a, b in pairs[17]
    }
    assert len(observed_pairs) == 16
    with (Path(__file__).resolve().parent / 'COLLISIONS.csv').open(newline='', encoding='utf-8') as stream:
        csv_pairs = {normalized_pair((r['word_a'], r['word_b'])) for r in csv.DictReader(stream)}
    assert observed_pairs == csv_pairs, 'collision listing differs from census'
    for a, b in observed_pairs:
        assert a != b and direct_deck(a) == direct_deck(b)

    unresolved = set(observed_pairs)
    reps = []
    while unresolved:
        rep = min(unresolved)
        orb = dihedral_orbit(rep)
        assert len(orb) == 4 and orb <= observed_pairs
        reps.append(rep)
        unresolved.difference_update(orb)
    assert len(reps) == 4

    # Literal enumeration independently checks the DP on all short words.
    independently_checked = 0
    for n in range(MIN_LENGTH, 11):
        for digits in product('01', repeat=n):
            word = ''.join(digits)
            states2 = [initial_state()]
            for digit in word:
                states2.append(extend(states2, int(digit)))
            assert flatten(states2[-1]) == direct_deck(word)
            independently_checked += 1

    print('VERIFY_OK', 'length_range=7..17', 'words_at_17=131072',
          'distinct_decks_at_17=131056', 'doubleton_decks_at_17=16',
          'singleton_decks_at_17=131040', 'symmetry_orbits=4',
          'independent_short_words=' + str(independently_checked))
    for n, classes, doubles in results:
        print('n=%d classes=%d doubletons=%d' % (n, classes, doubles))
    for a, b in sorted(reps):
        print('orbit_representative', a, b)
    return results, sorted(observed_pairs)


if __name__ == '__main__':
    full_census()
