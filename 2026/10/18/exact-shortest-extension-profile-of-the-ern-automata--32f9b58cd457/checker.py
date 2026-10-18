#!/usr/bin/env python3
"""Reproduce finite checks for the exact Černý subset-extension profile.
Only finite checks: the mathematical proof handles arbitrary n.
"""
from collections import Counter, deque
from math import comb
from itertools import product


def prediction(n, subset):
    bits = [(subset >> i) & 1 for i in range(n)]
    return next(r + 1 for r in range(n)
                if not bits[r] and bits[(r + 1) % n])


def preimage(n, subset, letter):
    if letter == 'a':
        return sum(((subset >> ((i + 1) % n)) & 1) << i for i in range(n))
    if letter == 'b':
        return (subset & ~1) | (((subset >> 1) & 1) << 0)
    raise ValueError(letter)


def shortest_by_bfs(n, target):
    # A word extends the target exactly when its reverse-preimage walk
    # reaches a subset with greater cardinality.
    start_size = target.bit_count()
    dist = {target: 0}
    todo = deque([target])
    while todo:
        x = todo.popleft()
        d = dist[x]
        if x.bit_count() > start_size:
            return d
        for a in 'ab':
            y = preimage(n, x, a)
            if y not in dist:
                dist[y] = d + 1
                todo.append(y)
    raise AssertionError('extension missing')


def check_profile(n):
    tally = Counter()
    refined = Counter()
    stuck = set()
    for subset in range(1, (1 << n) - 1):
        d = shortest_by_bfs(n, subset)
        pred = prediction(n, subset)
        assert d == pred, (n, subset, d, pred)
        tally[d] += 1
        refined[(subset.bit_count(), d)] += 1
        if d == n:
            stuck.add(subset)
    assert len(stuck) == n - 1
    assert stuck == {(1 << k) - 1 for k in range(1, n)}
    for d in range(1, n):
        assert tally[d] == d * 2 ** (n - d - 1)
        for k in range(1, n):
            formula = sum(comb(n - d - 1, k - 1 - h)
                          for h in range(d)
                          if 0 <= k - 1 - h <= n - d - 1)
            assert refined[(k, d)] == formula, (n, k, d)
    assert tally[n] == n - 1
    assert all(refined[(k, n)] == 1 for k in range(1, n))
    assert sum(d * count for d, count in tally.items()) == 3 * (2 ** n - n - 1)
    return tally


def image(n, start, word):
    x = start
    for letter in word:
        if letter == 'a':
            x = (x + 1) % n
        else:
            x = 1 if x == 0 else x
    return x


def verify_unique_word(n, subset):
    d = prediction(n, subset)
    words = []
    for letters in product('ab', repeat=d):
        w = ''.join(letters)
        newsize = sum((subset >> image(n, q, w)) & 1 for q in range(n))
        if newsize > subset.bit_count():
            words.append(w)
    assert words == ['b' + 'a' * (d - 1)], (n, subset, words)


def main():
    for n in range(3, 12):
        hist = check_profile(n)
        print(f'n={n} subsets={(1 << n)-2} distribution=' +
              ','.join(f'{d}:{hist[d]}' for d in range(1, n + 1)))
    count = 0
    for n in range(3, 10):
        for subset in range(1, (1 << n) - 1):
            verify_unique_word(n, subset)
            count += 1
    print(f'brute_force_unique_shortest_words={count}; n=3..9')
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
