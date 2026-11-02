#!/usr/bin/env python3
"""Finite checks for two-sided transversals on rectangular bands.
No external dependencies; all computations use the defining multiplication.
"""
from itertools import permutations, product
from math import factorial


def mul(x, y):
    return x[0], y[1]


def direct(n):
    cells = [(i, j) for i in range(2) for j in range(n)]
    count_left = 0
    count_two = 0
    for perm in permutations(cells):
        image_l = {mul(x, y) for x, y in zip(cells, perm)}
        if len(image_l) != 2*n:
            continue
        count_left += 1
        image_r = {mul(y, x) for x, y in zip(cells, perm)}
        if len(image_r) == 2*n:
            count_two += 1
    return count_left, count_two


def cycles(p):
    n = len(p)
    seen = set()
    c = 0
    for i in range(n):
        if i not in seen:
            c += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return c


def cycle_sum(n):
    return sum(2 ** cycles(p) for p in permutations(range(n)))


def encode_from_parameters(n, p, q, eps):
    # The two row-first coordinates are epsilon_j and 1-epsilon_j.
    return tuple((eps[j] if i == 0 else 1-eps[j], (p if i == 0 else q)[j])
                 for i in range(2) for j in range(n))


def parameter_count(n):
    perms = list(permutations(range(n)))
    total = 0
    for p in perms:
        for q in perms:
            for eps in product((0, 1), repeat=n):
                alpha = encode_from_parameters(n, p, q, eps)
                if len(set(alpha)) == 2*n:
                    total += 1
    return total


def main():
    for n in range(1, 5):
        left, two = direct(n)
        expected_left = (2 ** n) * factorial(n) ** 2
        expected_two = factorial(n)*factorial(n+1)
        assert (left, two) == (expected_left, expected_two), (n, left, two)
        print('direct', n, left, two)
    for n in range(1, 8):
        c = cycle_sum(n)
        assert c == factorial(n+1), (n,c)
        print('cycle', n, c)
    for n in range(1, 5):
        cnt = parameter_count(n)
        assert cnt == factorial(n)*factorial(n+1), (n,cnt)
        print('parameter', n, cnt)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
