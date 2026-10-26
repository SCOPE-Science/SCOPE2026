#!/usr/bin/env python3
"""Exact-arithmetic checks for the factoradic one-step descent theorem."""
import math


def digits_modulo(n):
    """Factoradic digits by repeated quotient/remainder."""
    assert n >= 0
    i = 1
    digits = []
    while n:
        n, a = divmod(n, i + 1)
        digits.append(a)
        i += 1
    return digits


def s_modulo(n, r):
    return sum(a ** r for a in digits_modulo(n))


def s_descending(n, r):
    """Independent factorial-weight greedy decomposition."""
    if n == 0:
        return 0
    k = 1
    while math.factorial(k + 1) <= n:
        k += 1
    total = 0
    for i in range(k, 0, -1):
        d, n = divmod(n, math.factorial(i))
        assert 0 <= d <= i
        total += d ** r
    assert n == 0
    return total


def parameters(r):
    assert r >= 2
    j = 2
    while math.factorial(j) <= j ** (r - 1):
        j += 1
    p = sum(i ** r - i * math.factorial(i) for i in range(1, j))
    a = max(t for t in range(j + 1) if p + t ** r - t * math.factorial(j) >= 0)
    return j, p, a, (a + 1) * math.factorial(j)


def main():
    example = [6, 24, 720, 10080, 362880, 7257600, 159667200, 6227020800]
    assert [parameters(r)[3] for r in range(2, 10)] == example
    for r in range(2, 41):
        j, p, a, c = parameters(r)
        assert j >= 3 and 0 <= a <= j
        assert p >= 0
        for i in range(1, j):
            assert i ** r - i * math.factorial(i) >= 0
            for d in range(i + 1):
                assert d ** r - d * math.factorial(i) <= i ** r - i * math.factorial(i)
        for t in range(a + 1, j + 1):
            assert p + t ** r - t * math.factorial(j) < 0
        assert s_modulo(c - 1, r) - (c - 1) == p + a ** r - a * math.factorial(j)
        assert s_modulo(c - 1, r) >= c - 1
        assert s_descending(c - 1, r) == s_modulo(c - 1, r)
        if a < j:
            assert s_modulo(c, r) < c
    for r in range(2, 7):
        j, _, _, c = parameters(r)
        limit = math.factorial(j + 1)
        last_failure = -1
        for n in range(limit):
            if s_modulo(n, r) >= n:
                last_failure = n
        assert last_failure == c - 1, (r, last_failure, c)
        for n in (0, 1, 2, c - 1, c, limit - 1, limit):
            assert s_descending(n, r) == s_modulo(n, r)
    print('VERIFIED: exact block endpoints, exponents 2..40, exhaustive lower ranges for 2..6')


if __name__ == '__main__':
    main()
