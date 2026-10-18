#!/usr/bin/env python3
"""Independent finite checks for the closure-rank polynomial on C_2 x C_n.

No external dependencies. Run: python3 verify.py
"""
from collections import Counter
from itertools import product
from math import comb


def convol(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def expected(n):
    a, b = [1], [1]
    for _ in range(n):
        a = convol(a, [1, 1, 1])
    for _ in range(n - 1):
        b = convol(b, [1, 1])
    for i, x in enumerate(b):
        a[i] -= x
    return a


def elements(n):
    return [(layer, level) for layer in (0, 1) for level in range(n)]


def leq(x, y):
    return x[0] <= y[0] and x[1] <= y[1]


def raw_closed_sets(n):
    """Brute-force subsets, checking ALL unordered pairwise meets."""
    els = elements(n)
    top = 2 * n - 1
    out = Counter()
    for mask in range(1 << (2 * n)):
        if not (mask & (1 << top)):
            continue
        f = {els[i] for i in range(2 * n) if mask & (1 << i)}
        if all((min(x[0], y[0]), min(x[1], y[1])) in f
               for x in f for y in f):
            out[len(f)] += 1
            if n <= 4:
                image = []
                for x in els:
                    above = [y for y in f if leq(x, y)]
                    image.append((min(y[0] for y in above),
                                  min(y[1] for y in above)))
                assert all(y in f for y in image)
                assert all(leq(x, y) for x, y in zip(els, image))
                assert all(image[els.index(image[i])] == image[i]
                           for i in range(len(els)))
                assert all(leq(image[i], image[j])
                           for i, x in enumerate(els)
                           for j, y in enumerate(els) if leq(x, y))
    return out


def direct_operator_counts(n):
    """Enumerate endofunctions from their extensive options; test the three axioms.

    This does not assume that closed sets or the theorem's normal form are valid.
    """
    els = elements(n)
    options = [[j for j, y in enumerate(els) if leq(x, y)] for x in els]
    comparable = [(i, j) for i, x in enumerate(els)
                  for j, y in enumerate(els) if leq(x, y)]
    out = Counter()
    for image in product(*options):
        if any(image[image[i]] != image[i] for i in range(len(els))):
            continue
        if any(not leq(els[image[i]], els[image[j]])
               for i, j in comparable):
            continue
        out[sum(image[i] == i for i in range(len(els)))] += 1
    return out


def main():
    for n in range(1, 9):
        poly = expected(n)
        closed = raw_closed_sets(n)
        assert [closed[i] for i in range(2*n + 1)] == poly
        assert sum(poly) == 3**n - 2**(n-1)
        assert poly[0] == 0 and all(v > 0 for v in poly[1:])
        if n <= 5:
            ops = direct_operator_counts(n)
            assert ops == closed, (n, ops, closed)
        print('n={} coefficients={} total={}'.format(
            n, poly[1:], sum(poly)))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
