#!/usr/bin/env python3
"""Independent exact rational checks for rank-two matroid angular laws.

All tests are finite corroboration of separately stated symbolic proofs.
Run: python3 check.py (Python >= 3.9, no external dependencies).
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def partitions(n, minimum=1):
    for head in range(minimum, n + 1):
        if head == n:
            yield (head,)
        else:
            for tail in partitions(n - head, head):
                yield (head,) + tail


def groups(parts):
    return tuple(i for i, size in enumerate(parts) for _ in range(size))


def predicted(parts):
    n = sum(parts)
    lookup = groups(parts)
    result = {}
    for x in range(n):
        for y in range(x + 1, n):
            if lookup[x] != lookup[y]:
                ax, ay = parts[lookup[x]], parts[lookup[y]]
                result[(x, y)] = Fraction(1, n) * (
                    Fraction(1, n - ax) + Fraction(1, n - ay))
    return result


def counts_bruteforce(parts):
    lookup = groups(parts)
    n = sum(parts)
    hits = Counter()
    for order in permutations(range(n)):
        x = order[0]
        y = next(y for y in order[1:] if lookup[y] != lookup[x])
        hits[tuple(sorted((x, y)))] += 1
    den = factorial(n)
    return {pair: Fraction(c, den) for pair, c in hits.items()}


def collision(parts):
    return sum((p * p for p in predicted(parts).values()), Fraction(0))


def face_zero_one(parts):
    n = sum(parts)
    return (sum(parts[i]*parts[j] for i in range(len(parts)) for j in range(i+1, len(parts))),
            sum(a * comb(n-a, 2) for a in parts))


def run():
    inspected = 0
    for n in range(2, 9):
        for parts in partitions(n):
            if len(parts) < 2:
                continue
            actual = counts_bruteforce(parts)
            expected = predicted(parts)
            assert actual == expected, ('probability', parts, actual, expected)
            assert sum(expected.values()) == 1
            bs = [Fraction(a, n-a) for a in parts]
            via_reduced_formula = (sum(bs) + 2*sum(bs[i]*bs[j] for i in range(len(bs))
                                    for j in range(i+1, len(bs)))) / n**2
            assert collision(parts) == via_reduced_formula
            inspected += 1

    inequality_tests = 0
    for n in range(3, 16):
        for parts in partitions(n):
            if len(parts) < 2:
                continue
            base = collision(parts)
            for small in range(len(parts)):
                for large in range(len(parts)):
                    if small == large or parts[small] < 2 or parts[large] < parts[small]:
                        continue
                    new = list(parts)
                    new[small] -= 1
                    new[large] += 1
                    assert collision(tuple(new)) > base, ('majorization', parts, tuple(new))
                    inequality_tests += 1
            m = len(parts)
            q, r = divmod(n, m)
            balanced = (q,)*(m-r) + (q+1,)*r
            skewed = (1,)*(m-1) + (n-m+1,)
            assert collision(balanced) <= base <= collision(skewed)

    a = (1, 4, 5, 8)
    b = (2, 2, 7, 7)
    assert face_zero_one(a) == face_zero_one(b) == (109, 1250)
    assert collision(a) == Fraction(11581, 1253070)
    assert collision(b) == Fraction(11617, 1254528)
    assert collision(b) - collision(a) == Fraction(2151, 119799680)
    for m in range(2, 12):
        for a0 in range(1, 20):
            parts = (a0,) + (1,)*(m-1)
            assert len(predicted(parts)) == face_zero_one(parts)[0]
    print('PASS: exhaustive greedy rank-two cone law for', inspected, 'class partitions of size at most 8')
    print('PASS: exact strict integer majorization for', inequality_tests, 'Robin-Hood reverse transfers')
    print('PASS: exact two face-count twins, 109 vertices and 1250 edges, with distinct angular collisions')
    print('PASS: exact normalization and closed collision identity')


if __name__ == '__main__':
    run()
