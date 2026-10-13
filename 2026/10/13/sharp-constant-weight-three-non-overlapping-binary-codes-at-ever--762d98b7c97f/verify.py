#!/usr/bin/env python3
"""Independent finite checks of a fixed-three-marker cross-bifix-free construction."""
from itertools import combinations
from math import comb


def build(n):
    t = n // 3
    return ["0" * a + "1" + "0" * (n-3-a-c) + "1" + "0" * c + "1"
            for c in range(t) for a in range(t, n-2-c)]


def collides(x, y):
    return any(x[:k] == y[-k:] for k in range(1, len(x)))


def necklace(x):
    return min(x[i:] + x[:i] for i in range(len(x)))


def primitive(x):
    return all(x != x[i:] + x[:i] for i in range(1, len(x)))


def check(n):
    code = build(n)
    target = (n-1)*(n-2)//6
    assert len(code) == target == len(set(code)), (n, len(code), target)
    assert all(len(x) == n and x.count('1') == 3 for x in code)
    assert all(not collides(x, y) for x in code for y in code), n
    assert len({necklace(x) for x in code}) == len(code)
    if n <= 25:
        words = [''.join('1' if j in picks else '0' for j in range(n))
                 for picks in combinations(range(n), 3)]
        cyclic_classes = {necklace(x) for x in words if primitive(x)}
        assert len(cyclic_classes) == target
        assert {necklace(x) for x in code} == cyclic_classes
    return n, target


if __name__ == '__main__':
    for n in range(4, 41):
        print(*check(n), sep=',')
    print('VERIFY_OK')
