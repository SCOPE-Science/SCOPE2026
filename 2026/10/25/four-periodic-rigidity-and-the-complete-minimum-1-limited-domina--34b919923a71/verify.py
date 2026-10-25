#!/usr/bin/env python3
"""Independent finite checks for minimum 1-limited domination on Mobius ladders.

Run: python verify.py
The mathematical proof of the infinite statements is in RESULT.md.
"""
from collections import defaultdict
from itertools import combinations


def graph(n):
    # Cyclic vertices 0,...,2n-1, opposite chords.
    size = 2 * n
    neigh = [0] * size
    for v in range(size):
        for u in ((v - 1) % size, (v + 1) % size, (v + n) % size):
            neigh[v] |= 1 << u
    assert all(z.bit_count() == 3 for z in neigh)
    return neigh


def valid(mask, neigh):
    for v, neighbors in enumerate(neigh):
        chosen = bool(mask & (1 << v))
        in_neighbors = (mask & neighbors).bit_count()
        if chosen:
            if in_neighbors < 2:
                return False
        elif in_neighbors < 1:
            return False
    return True


def word_mask(s):
    n = len(s)
    ans = 0
    for i, rung in enumerate(s):
        if rung & 1:
            ans |= 1 << i
        if rung & 2:
            ans |= 1 << (n + i)
    return ans


def predicted_masks(n):
    out = set()
    if n % 4 == 0:
        base = [0, 0, 3, 3] * (n // 4)
        for shift in range(n):
            out.add(word_mask(base[shift:] + base[:shift]))
        return out
    # A unique doubly-selected rung and otherwise singleton rungs.
    for j in range(n):
        out.add(word_mask([1] * j + [3] + [2] * (n - j - 1)))
        out.add(word_mask([2] * j + [3] + [1] * (n - j - 1)))
    if n % 4 == 1:
        r = (n - 1) // 4
        base = [0, 0, 3, 3, 3] + ([0, 0, 3, 3] * (r - 1))
    elif n % 4 == 3:
        r = (n - 3) // 4
        base = [0, 3, 3] + ([0, 0, 3, 3] * r)
    else:
        base = []
    if base:
        assert len(base) == n
        for shift in range(n):
            out.add(word_mask(base[shift:] + base[:shift]))
    return out


def expected(n):
    return (n, 4) if n % 4 == 0 else (n + 1, 2 * n + (n if n % 2 else 0))


def triple_ok(a, b, c):
    for side in (0, 1):
        me = (b >> side) & 1
        inside = ((a >> side) & 1) + ((c >> side) & 1) + ((b >> (1-side)) & 1)
        if me and inside < 2:
            return False
        if not me and inside < 1:
            return False
    return True


def flip(s):
    return ((s & 1) << 1) | ((s & 2) >> 1)


def dp_minimum(n):
    # Open-strip dynamic program, then attach the exact Mobius twist at the seam.
    least = 10**9
    ways_total = 0
    for first in range(4):
        for second in range(4):
            states = {(first, second): (first.bit_count() + second.bit_count(), 1)}
            for _ in range(2, n):
                next_states = {}
                for (before, mid), (size, ways) in states.items():
                    for after in range(4):
                        if not triple_ok(before, mid, after):
                            continue
                        key = (mid, after)
                        cand = size + after.bit_count()
                        if key not in next_states or cand < next_states[key][0]:
                            next_states[key] = (cand, ways)
                        elif cand == next_states[key][0]:
                            oldsize, oldways = next_states[key]
                            next_states[key] = (oldsize, oldways + ways)
                states = next_states
            for (penult, last), (size, ways) in states.items():
                if not triple_ok(penult, last, flip(first)):
                    continue
                if not triple_ok(flip(last), first, second):
                    continue
                if size < least:
                    least, ways_total = size, ways
                elif size == least:
                    ways_total += ways
    return least, ways_total


def exhaustive(n):
    neigh = graph(n)
    prescribed = predicted_masks(n)
    target, count = expected(n)
    assert len(prescribed) == count, (n, 'duplicate candidates')
    assert all(mask.bit_count() == target and valid(mask, neigh) for mask in prescribed)
    # Lower sizes below n are excluded by the proved bipartite cut inequality;
    # explicitly inspect the potentially competing size n and the optimum size.
    for size in range(n, target + 1):
        actual = set()
        for chosen in combinations(range(2*n), size):
            mask = sum(1 << v for v in chosen)
            if valid(mask, neigh):
                actual.add(mask)
        if size < target:
            assert not actual, (n, size, len(actual))
        else:
            assert actual == prescribed, (n, len(actual), len(prescribed), len(actual ^ prescribed))


def main():
    for n in range(3, 10):
        exhaustive(n)
    for n in range(3, 61):
        val = dp_minimum(n)
        assert val == expected(n), (n, val, expected(n))
        forms = predicted_masks(n)
        assert len(forms) == expected(n)[1]
        neighbors = graph(n)
        assert all(s.bit_count() == expected(n)[0] and valid(s, neighbors) for s in forms)
    print('VERIFY_OK exhaustive_n=3..9 dp_n=3..60 explicit_n=3..60')


if __name__ == '__main__':
    main()
