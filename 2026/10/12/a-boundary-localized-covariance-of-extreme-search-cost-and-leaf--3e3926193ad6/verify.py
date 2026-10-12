#!/usr/bin/env python3
"""Rational finite checks for a random binary-search-tree covariance identity."""
from fractions import Fraction as F
from itertools import permutations
from math import factorial


def insert(root, x):
    if root is None:
        return [x, None, None]
    curr = root
    while True:
        side = 1 if x < curr[0] else 2
        if curr[side] is None:
            curr[side] = [x, None, None]
            return root
        curr = curr[side]


def quantities(root):
    right = 0
    node = root
    while node is not None:
        right += 1
        node = node[2]
    stack = [root]
    leaves = 0
    while stack:
        node = stack.pop()
        if node[1] is None and node[2] is None:
            leaves += 1
        else:
            if node[1] is not None:
                stack.append(node[1])
            if node[2] is not None:
                stack.append(node[2])
    return right, leaves


def harmonic(n):
    return sum((F(1, i) for i in range(1, n + 1)), F(0))


def formula(n):
    return F((n - 2) * (n + 1), 12 * n * (n - 1))


def exact_enumeration():
    for n in range(2, 9):
        sr = sl = sr_l = 0
        for seq in permutations(range(1, n + 1)):
            root = None
            for x in seq:
                root = insert(root, x)
            r, l = quantities(root)
            sr += r
            sl += l
            sr_l += r * l
        denom = factorial(n)
        assert F(sr, denom) == harmonic(n)
        assert F(sl, denom) == F(n + 1, 3)
        cov = F(sr_l, denom) - F(sr * sl, denom * denom)
        assert cov == formula(n), (n, cov, formula(n))
        print('EXHAUSTIVE', n, denom, str(cov))


def split_recurrence():
    c = [F(0), F(0)]
    for n in range(2, 501):
        H = [harmonic(j) for j in range(n)]
        leaf = [F(0), F(1)] + [F(j + 1, 3) for j in range(2, n)]
        mean_r = sum(H, F(0)) / n
        right_left_means = [leaf[m] + leaf[n - 1 - m] for m in range(n)]
        mean_l = sum(right_left_means, F(0)) / n
        cov_split = sum((H[m] * right_left_means[m] for m in range(n)), F(0)) / n - mean_r * mean_l
        assert cov_split == F(n - 2, 3 * n * (n - 1))
        current = sum(c, F(0)) / n + cov_split
        assert current == formula(n), (n, current, formula(n))
        c.append(current)
    print('SPLIT_RECURRENCE', 499, 'exact')


if __name__ == '__main__':
    exact_enumeration()
    split_recurrence()
    print('VERIFY_OK')
