#!/usr/bin/env python3
"""Independent direct rank-two FO check, enumerating all binary paths of size <=14.

For a pointed vertex x, retain the set of realized quantifier-free 2-point
atomic diagrams (x,y). A rank-one formula in x can depend only on this set.
A rank-two closed sentence can depend only on the set of pointed rank-one
profiles. No window automaton, truncation rule, or theorem formula is used.
"""
from collections import Counter
from itertools import product


def direct_signature(word):
    pointed_profiles = set()
    for i, x in enumerate(word):
        pair_diagrams = frozenset((x, y, i == j, abs(i-j) == 1)
                                  for j, y in enumerate(word))
        pointed_profiles.add(pair_diagrams)
    return frozenset(pointed_profiles)


def main():
    minima = {}
    new = Counter()
    for size in range(1, 15):
        for word in product((0, 1), repeat=size):
            signature = direct_signature(word)
            if signature not in minima:
                minima[signature] = (size, ''.join(map(str, word)))
                new[size] += 1
    assert len(minima) == 70
    assert dict(sorted(new.items())) == {1: 2, 2: 3, 3: 6, 4: 10, 5: 14,
                                         6: 18, 7: 10, 8: 5, 10: 2}
    longest = sorted(w for n, w in minima.values() if n == 10)
    assert longest == ['0011001100', '1100110011']
    print('direct_words_checked=' + str(sum(2 ** n for n in range(1, 15))))
    print('rank_two_theories_through_14=70')
    print('minimum_length_distribution=' + str(dict(sorted(new.items()))))
    print('length_ten_witnesses=' + ','.join(longest))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
