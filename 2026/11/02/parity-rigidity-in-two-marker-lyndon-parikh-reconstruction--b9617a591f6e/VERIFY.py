"""Standalone checks for exact binary two-marker Lyndon-Parikh fibers.

No external dependencies. The direct observation uses literal word rotations,
not the formulas used in the proof. Invoke: python VERIFY.py
"""
from collections import Counter, defaultdict
from itertools import combinations


def count_01(word):
    z = p = 0
    for ch in word:
        if ch == '0': z += 1
        else: p += z
    return p


def direct_observation(word):
    rotation = min(word[k:] + word[:k] for k in range(len(word)))
    return word.count('0'), word.count('1'), count_01(word), count_01(rotation)


def theoretical_observation(a, b, c):
    N = a + b + c
    return N, 2, 2 * a + b, N + max(b, a + c)


def all_words(N):
    for i, j in combinations(range(N + 2), 2):
        yield ''.join('1' if k == i or k == j else '0' for k in range(N + 2))


def pair_words(h, t, j):
    high = '0' * j + '1' + '0' * (2 * h - t) + '1' + '0' * (t - j)
    low = '0' * (j + h - t) + '1' + '0' * t + '1' + '0' * (h - j)
    return high, low


def check(N):
    buckets = defaultdict(list)
    for w in all_words(N):
        i, j = [k for k, c in enumerate(w) if c == '1']
        a, b, c = i, j - i - 1, N + 1 - j
        sd = direct_observation(w)
        assert sd == theoretical_observation(a, b, c), (N, w, sd, a, b, c)
        buckets[sd].append(w)
    actual = Counter(len(v) for v in buckets.values())
    if N % 2 == 1:
        expected = {1: (N + 1) * (N + 2) // 2}
    else:
        h = N // 2
        expected = {1: (h + 1) ** 2}
        if h:
            expected[2] = h * (h + 1) // 2
        collisions = {frozenset(v) for v in buckets.values() if len(v) == 2}
        pairs = {frozenset(pair_words(h, t, j)) for t in range(h) for j in range(t + 1)}
        assert collisions == pairs, (N, len(collisions), len(pairs))
        assert len(pairs) == h * (h + 1) // 2
    assert dict(actual) == expected, (N, actual, expected)
    assert sum(k * v for k, v in actual.items()) == (N + 1) * (N + 2) // 2
    return len(buckets), actual


if __name__ == '__main__':
    tested = 0
    for N in range(61):
        count, hist = check(N)
        tested += (N + 1) * (N + 2) // 2
        if N <= 8:
            print(f'N={N}: profiles={count}, histogram={dict(sorted(hist.items()))}')
    print(f'VERIFY_OK zero_counts=0..60 words={tested} direct_rotations=yes explicit_pairs=yes')
