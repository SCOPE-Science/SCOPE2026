#!/usr/bin/env python3
"""Direct checks for small-factor attractors of Thue--Morse iterates."""
from collections import Counter
from itertools import combinations

SUB = str.maketrans({'0': '01', '1': '10'})


def thue_morse(order):
    word = '0'
    for _ in range(order):
        word = ''.join('01' if x == '0' else '10' for x in word)
    return word


def coverage_masks(word, max_factor):
    """Build position masks directly from occurrences of ALL factors."""
    n = len(word)
    factors = sorted(set(word[start:start + length]
                         for length in range(1, max_factor + 1)
                         for start in range(n - length + 1)))
    indices = {factor: i for i, factor in enumerate(factors)}
    masks = [0] * n
    for length in range(1, max_factor + 1):
        for start in range(n - length + 1):
            bit = 1 << indices[word[start:start + length]]
            for pos in range(start, start + length):
                masks[pos] |= bit
    return masks, (1 << len(factors)) - 1, factors


def directly_valid_pairs(word, max_factor):
    masks, target, _ = coverage_masks(word, max_factor)
    return {p for p in combinations(range(len(word)), 2)
            if masks[p[0]] | masks[p[1]] == target}


def locally_predicted_pairs(word, max_factor):
    radius = max_factor - 1
    # The theorem uses only exact centered contexts, not global factor coverages.
    if max_factor == 2:
        families = (('001', '110'), ('100', '011'))
    elif max_factor == 3:
        families = (('01001', '10110'), ('01101', '10010'))
    else:
        raise ValueError('Only lengths two and three are compared')
    sets = {s: [] for family in families for s in family}
    for i in range(radius, len(word) - radius):
        s = word[i - radius:i + radius + 1]
        if s in sets:
            sets[s].append(i)
    return {tuple(sorted((i, j))) for a, b in families
            for i in sets[a] for j in sets[b]}


def expected_count(order, max_factor):
    n = 1 << order
    if max_factor == 2:
        return ((n - 4) * (n + 2) if order % 2 == 0
                else (n - 2) ** 2) // 18
    if max_factor == 3:
        return ((n - 4) ** 2 if order % 2 == 0
                else (n + 4) * (n - 8)) // 72
    raise ValueError


def profile(order):
    c = Counter(thue_morse(order)[i:i+5] for i in range((1 << order) - 4))
    n = 1 << order
    if order % 2 == 0:
        a = b = (n - 4) // 12
    else:
        a, b = (n + 4) // 12, (n - 8) // 12
    assert c['01001'] == c['01101'] == a
    assert c['10110'] == c['10010'] == b
    return a, b


def check_local_table():
    w = thue_morse(4)
    factors = sorted(set(w[i:i+5] for i in range(len(w)-4)))
    assert len(factors) == 12
    universe = set(w[i:i+length]
                   for length in (1, 2, 3)
                   for i in range(len(w) - length + 1))
    def local_cover(s):
        return {s[2], s[1:3], s[2:4], s[:3], s[1:4], s[2:]}
    pair_types = {frozenset((a, b)) for a, b in combinations(factors, 2)
                  if local_cover(a) | local_cover(b) == universe}
    assert pair_types == {frozenset(('01001', '10110')),
                          frozenset(('01101', '10010'))}
    print('Twelve-factor local table: exactly two compatible context pairs')


def main():
    check_local_table()
    for order in range(3, 11):
        word = thue_morse(order)
        for max_factor in (2, 3):
            if max_factor == 3 and order < 4:
                continue
            observed = directly_valid_pairs(word, max_factor)
            predicted = locally_predicted_pairs(word, max_factor)
            expected = expected_count(order, max_factor)
            assert observed == predicted, (order, max_factor, len(observed ^ predicted))
            assert len(observed) == expected, (order, max_factor, len(observed), expected)
            masks, target, factors = coverage_masks(word, max_factor)
            assert not any(mask == target for mask in masks)
            print('order', order, 'N', len(word), 'k', max_factor,
                  'minimum', 2, 'pair_count', len(observed), 'factors', len(factors))
        if order >= 4:
            profile(order)
    for order in range(11, 15):
        profile(order)
    print('PASS: independent global coverage vs local context comparisons (orders 3..10),'
          ' exact closed counts and context frequencies (orders 4..14)')


if __name__ == '__main__':
    main()
