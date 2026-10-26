#!/usr/bin/env python3
"""Reproduce the fixed-composition Parikh-matrix class census.

This verifies finite instances; the all-parameter proof is algebraic.
"""
from collections import defaultdict
from itertools import combinations


def signature(word):
    # Direct streaming counts of scattered subwords ab, bc, abc.
    a = b = ab = bc = abc = 0
    for letter in word:
        if letter == 'a':
            a += 1
        elif letter == 'b':
            ab += a
            b += 1
        else:
            abc += ab
            bc += b
    return (ab, bc, abc)


def triangle(t, budget):
    """Number of x,y,z >= 0: x+y+z=budget, y+2z=t."""
    if t < 0 or t > 2 * budget:
        return 0
    return t // 2 - max(0, t - budget) + 1


def multiplicity(m, ab, bc, abc):
    if not (0 <= bc <= m):
        return 0
    h = m - bc
    # c a a
    x = triangle(ab, h) if abc == 0 else 0
    # a c a
    x += int(0 <= abc <= bc and h + abc <= ab <= 2 * h + abc)
    # a a c
    if ab == abc + 2 * h:
        x += triangle(abc, bc)
    return x


def all_signatures(m):
    result = set()
    for bc in range(m + 1):
        h = m - bc
        result.update((ab, bc, 0) for ab in range(2*h+1))
        result.update((ab, bc, abc)
                      for abc in range(bc + 1)
                      for ab in range(h + abc, 2*h + abc + 1))
        result.update((abc + 2*h, bc, abc) for abc in range(2*bc + 1))
    return result


def brute_classes(m):
    groups = defaultdict(int)
    n = m+3
    for pair in combinations(range(n), 2):
        for ci in range(n):
            if ci in pair:
                continue
            word = ['b'] * n
            word[pair[0]] = word[pair[1]] = 'a'
            word[ci] = 'c'
            groups[signature(word)] += 1
    return groups


def verify(limit=35):
    total_words_checked = 0
    for m in range(limit + 1):
        groups = brute_classes(m)
        keys = all_signatures(m)
        assert keys == set(groups), (m, 'key mismatch')
        for (ab, bc, abc), observed in groups.items():
            predicted = multiplicity(m, ab, bc, abc)
            assert observed == predicted, (m, ab, bc, abc, observed, predicted)
        observed_n = len(groups)
        predicted_n = (m+1)*(m*m+11*m+6)//6
        assert observed_n == predicted_n
        observed_max = max(groups.values())
        assert observed_max == max(3, m//2+2)
        assert sum(groups.values()) == (m+3)*(m+2)*(m+1)//2
        total_words_checked += sum(groups.values())
        if m in (0, 1, 2, 5, 10, 20, 35):
            print(f'm={m:2d}: images={observed_n:6d}; maximum fiber={observed_max:2d}; words={sum(groups.values()):6d}')
    print(f'PASS: {total_words_checked} words across m=0..{limit}, all fibers and exact formulas')


if __name__ == '__main__':
    verify()
