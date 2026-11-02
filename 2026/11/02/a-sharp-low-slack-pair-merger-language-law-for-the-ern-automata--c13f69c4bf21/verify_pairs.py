#!/usr/bin/env python3
"""Exact finite checks for the Cerny pair low-slack theorem; Python stdlib."""
from collections import deque
from functools import lru_cache
from itertools import product
from math import comb


def transform(n, states, letter):
    if letter == 'a':
        return tuple(sorted({(q + 1) % n for q in states}))
    if letter == 'b':
        return tuple(sorted({0 if q == n - 1 else q for q in states}))
    raise ValueError(letter)


def predicted_distance(n, states):
    if len(states) == 1:
        return 0
    i, j = states
    h = j - i
    if 2 * h < n:
        return n * h - i
    if 2 * h == n:
        return n * (n - 1) // 2 - i
    return (n - h) * (n + 1) - n - i


def coefficient(s, t):
    # Coefficient of z^t / ((1-z)^s (1-2z)).
    return sum((comb(s + e - 1, e) if s else (1 if e == 0 else 0))
               * (2 ** (t - e)) for e in range(t + 1))


def verify(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    singles = [(i,) for i in range(n)]
    ranks = {p: predicted_distance(n, p) for p in pairs}
    m = n * (n - 1) // 2
    assert sorted(ranks.values()) == list(range(1, m + 1))
    edges = {p: tuple(transform(n, p, c) for c in 'ab')
             for p in pairs + singles}
    reverse = {p: [] for p in pairs + singles}
    for p in pairs + singles:
        for q in edges[p]:
            reverse[q].append(p)
    distances = {p: 0 for p in singles}
    queue = deque(singles)
    while queue:
        current = queue.popleft()
        for p in reverse[current]:
            if p not in distances:
                distances[p] = distances[current] + 1
                queue.append(p)
    assert all(distances[p] == ranks[p] for p in pairs)
    jump_edges = []
    for p in pairs:
        d = ranks[p]
        assert sum(predicted_distance(n, q) == d - 1 for q in edges[p]) == 1
        for q in edges[p]:
            if len(q) == 2 and q != p and predicted_distance(n, q) >= d:
                jump_edges.append((predicted_distance(n, q) - d, p))
    k = (n - 1) // 2
    assert sum(delta == k for delta, _ in jump_edges) == 1
    assert all(delta >= k for delta, _ in jump_edges)

    @lru_cache(None)
    def exact_words(p, length):
        if length < 0:
            return 0
        if len(p) == 1:
            return 2 ** length
        if length == 0:
            return 0
        return sum(exact_words(q, length - 1) for q in edges[p])

    for p in pairs:
        d = ranks[p]
        s = sum(ranks[q] <= d for q in pairs if q[1] != n - 1)
        for slack in range(k + 1):
            assert exact_words(p, d + slack) == coefficient(s, slack), (n, p, slack)
    farthest = max(pairs, key=ranks.get)
    assert farthest == (0, n // 2)
    s = comb(n - 1, 2)
    assert exact_words(farthest, m + k + 1) == coefficient(s, k + 1) + 1

    # Independent enumeration of literal input words for small instances.
    if n <= 5:
        for p in pairs:
            d = ranks[p]
            for slack in range(k + 2):
                length = d + slack
                brute = 0
                for letters in product('ab', repeat=length):
                    q = p
                    for c in letters:
                        q = transform(n, q, c)
                    brute += len(q) == 1
                assert brute == exact_words(p, length), (n, p, slack)

    return m, k, coefficient(s, 1)


def check_boundary():
    for t in range(9):
        length = t + 1
        assert sum('b' in letters for letters in product('ab', repeat=length)) == 2 ** (t + 1) - 1


if __name__ == '__main__':
    check_boundary()
    for n in range(3, 23):
        print(n, *verify(n))
    print('VERIFY_OK')
