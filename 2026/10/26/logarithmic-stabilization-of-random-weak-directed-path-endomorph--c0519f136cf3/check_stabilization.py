#!/usr/bin/env python3
"""Finite checks for stabilization of weak endomorphisms of directed paths.
Run: python3 check_stabilization.py
No third-party dependencies.
"""
from collections import Counter
from itertools import product


def is_weak_path_map(f):
    return all(f[i+1] - f[i] in (0, 1) for i in range(len(f)-1))


def stabilization_time(f):
    n = len(f)
    fixed = [i for i in range(n) if f[i] == i]
    assert fixed and fixed == list(range(fixed[0], fixed[-1]+1))
    a, b = fixed[0], fixed[-1]
    current = tuple(range(n))
    t = 0
    while any(current[i] != min(b, max(a, i)) for i in range(n)):
        current = tuple(f[j] for j in current)
        t += 1
        assert t <= n-1
    return t, a, b


def maps(n):
    for first in range(n):
        for bits in product((0, 1), repeat=n-1):
            seq = [first]
            for bit in bits:
                seq.append(seq[-1] + bit)
            if seq[-1] < n:
                yield tuple(seq)


def binomial_side_time(bits):
    # bits are the free increments at distances two, three, ...
    prefix = [0, 0]
    for bit in bits:
        prefix.append(prefix[-1] + bit)
    d = len(bits)+1
    t = 0
    while d:
        d = prefix[d]
        t += 1
    return t


def check(n):
    hist = Counter()
    ranks = Counter()
    for f in maps(n):
        assert is_weak_path_map(f)
        t, a, b = stabilization_time(f)
        hist[t] += 1
        ranks[b-a+1] += 1
        u, v = a, n-1-b
        # reconstruct each side's free bit string in distance coordinates
        left_bits = [f[a-d+1] - f[a-d] for d in range(2, u+1)]
        right_bits = [f[b+d] - f[b+d-1] for d in range(2, v+1)]
        predicted = max(binomial_side_time(left_bits) if u else 0,
                        binomial_side_time(right_bits) if v else 0)
        assert t == predicted, (n, f, t, predicted)
    assert sum(hist.values()) == (n+1)*(2**(n-2))
    assert hist[n-1] == 2
    for r in range(1, n):
        assert ranks[r] == (n-r+3)*2**(n-r-2) if n-r>=2 else ranks[r] == 2
    assert ranks[n] == 1
    print(n, 'total', sum(hist.values()), 'stabilization distribution', sorted(hist.items()))


if __name__ == '__main__':
    for n in range(2, 12):
        check(n)
    print('All checks passed for n=2,...,11.')
