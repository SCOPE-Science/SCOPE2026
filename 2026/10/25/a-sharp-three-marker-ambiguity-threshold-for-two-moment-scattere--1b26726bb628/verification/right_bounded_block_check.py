#!/usr/bin/env python3
"""Exact integer checks for two-moment right-bounded-block reconstruction."""
from collections import defaultdict
from itertools import product
from math import comb, isqrt


def direct_observation(w):
    count_a = count_b = ab = aa = aab = 0
    for letter in w:
        if letter == 'a':
            aa += count_a
            count_a += 1
        else:
            aab += aa
            ab += count_a
            count_b += 1
    return (count_a, count_b, ab, aab)


def moment_observation(w):
    k = w.count('a')
    t = 0
    positions = []
    for letter in w:
        if letter == 'a':
            t += 1
        else:
            positions.append(t)
    return (k, len(positions), sum(positions),
            sum(v * (v - 1) // 2 for v in positions))


def word_from_positions(k, positions):
    p0, p1, p2 = positions
    assert 0 <= p0 <= p1 <= p2 <= k
    return 'a' * p0 + 'b' + 'a' * (p1-p0) + 'b' + 'a' * (p2-p1) + 'b' + 'a' * (k-p2)


def norm_points(r):
    value = 7 ** r
    L = isqrt(value)
    solutions = []
    for x in range(L + 1):
        disc = 4 * value - 3 * x * x
        root = isqrt(disc)
        if root * root == disc and root >= x and (root - x) % 2 == 0:
            y = (root - x) // 2
            assert x * x + x * y + y * y == value
            solutions.append((x, y))
    return solutions


def main():
    expected = {
        (4, 3, 6, 6): {'abbaaab', 'baaabba'},
        (3, 4, 6, 3): {'abbbaab', 'baabbba'},
    }
    for n in range(0, 11):
        classes = defaultdict(set)
        for symbols in product('ab', repeat=n):
            w = ''.join(symbols)
            d = direct_observation(w)
            assert d == moment_observation(w), (n, w, d, moment_observation(w))
            classes[d].add(w)
        if n <= 6:
            assert all(len(c) == 1 for c in classes.values()), n
        if n == 7:
            ambiguous = {obs: words for obs, words in classes.items() if len(words) > 1}
            assert ambiguous == expected, ambiguous
        print(f'length={n} words={2**n} classes={len(classes)} max_fiber={max(map(len, classes.values()))}')
    for r in range(1, 10):
        value = 7 ** r
        L = isqrt(value) + (isqrt(value) ** 2 != value)
        k = 2 * L + 1
        S = 3 * L + 1
        solutions = norm_points(r)
        assert len(solutions) == (r + 1 if r % 2 else r + 2)
        eligible = [(x, y) for x, y in solutions if (2*x+y) % 3 == 1]
        assert len(eligible) == r//2 + 1
        obs = set()
        words = set()
        for x, y in eligible:
            t0 = (S-2*x-y)//3
            t1 = t0+x
            t2 = t1+y
            assert (S-2*x-y) % 3 == 0
            w = word_from_positions(k, (t0, t1, t2))
            assert len(w) == k + 3
            assert direct_observation(w) == moment_observation(w)
            obs.add(direct_observation(w))
            words.add(w)
        assert len(obs) == 1 and len(words) == len(eligible)
        print(f'power={r} norm={value} length={k+3} same_observation_words={len(words)}')
    print('RBB_TWO_MOMENT_PASS first_collisions=7 classes=2 growing_three_marker_fibers=1..9')


if __name__ == '__main__':
    main()
