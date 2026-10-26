#!/usr/bin/env python3
"""Independent finite checks of uniform idempotent-map star counts."""
from itertools import product
from math import comb, factorial


def count_idempotents_formula(n):
    if n == 0:
        return 1
    return sum(comb(n, k) * k ** (n - k) for k in range(1, n + 1))


def falling(n, k):
    z = 1
    for i in range(k):
        z *= n - i
    return z


def exhaustive(n):
    total = 0
    counts = [0] * n
    second_factorials = [0] * n
    for f in product(range(n), repeat=n):
        if any(f[f[x]] != f[x] for x in range(n)):
            continue
        total += 1
        roots = [x for x in range(n) if f[x] == x]
        stars = [sum(f[y] == x for y in range(n)) - 1 for x in roots]
        c = [stars.count(s) for s in range(n)]
        for s in range(n):
            counts[s] += c[s]
            second_factorials[s] += c[s] * (c[s] - 1)
    expected = count_idempotents_formula(n)
    assert total == expected, (n, total, expected)
    for s in range(n):
        h = s + 1
        first = (falling(n, h) // factorial(s)) * count_idempotents_formula(n - h)
        assert counts[s] == first, (n, s, counts[s], first)
        if 2 * h <= n:
            second = falling(n, 2*h) // factorial(s)**2 * count_idempotents_formula(n-2*h)
        else:
            second = 0
        assert second_factorials[s] == second, (n, s, second_factorials[s], second)
    return total


def main():
    for n in range(1, 7):
        print('N', n, 'IDEMPOTENTS', exhaustive(n))
    print('IDEMPOTENT_STAR_MOMENTS_OK')


if __name__ == '__main__':
    main()
