#!/usr/bin/env python3
"""Finite exact checks for a totient--Carmichael composition theorem.

Run with: python3 verify.py
This is a finite regression check, not an infinite proof.
"""
from math import gcd, lcm


def factor(n):
    assert n >= 1
    result = {}
    d = 2
    while d * d <= n:
        if n % d == 0:
            k = 0
            while n % d == 0:
                n //= d
                k += 1
            result[d] = k
        d = 3 if d == 2 else d + 2
    if n > 1:
        result[n] = 1
    return result


def phi(n):
    result = n
    for p in factor(n):
        result = result // p * (p - 1)
    return result


def carmichael(n):
    if n == 1:
        return 1
    result = 1
    for p, e in factor(n).items():
        if p == 2 and e >= 3:
            period = 2 ** (e - 2)
        else:
            period = (p - 1) * p ** (e - 1)
        result = lcm(result, period)
    return result


def prime(n):
    return n > 1 and factor(n) == {n: 1}


def formula(p, a):
    m = p - 1
    t = 0
    while m % 2 == 0:
        t += 1
        m //= 2
    u = m
    c = lambda j: 0 if j <= 1 else 1 if j == 2 else j - 2
    T = max(t, c(a))
    S = a + t - 1
    K = carmichael(u)
    h = 0
    while K % 2 == 0:
        h += 1
        K //= 2
    E = max(t, c(S), h)
    H = u * phi(u) // lcm(u, K)
    numerator = 2 ** (T + t - 1) * H
    denominator = 2 ** E
    assert numerator % denominator == 0, (p, a)
    return numerator // denominator


def predicted_equal(p, a):
    if p == 3:
        return True
    m = p - 1
    t = 0
    while m % 2 == 0:
        t += 1
        m //= 2
    return m == 1 and t >= 2 and a >= t + 2


def main():
    count = 0
    ones = []
    for p in range(3, 300, 2):
        if not prime(p):
            continue
        for a in range(1, 11):
            predicted = formula(p, a)
            for b in (2, 3, 4):
                n = (2 ** a) * (p ** b)
                x = phi(carmichael(n))
                y = carmichael(phi(n))
                assert x % y == 0, (p, a, b, x, y)
                assert x // y == predicted, (p, a, b, x, y, predicted)
                assert (x == y) == predicted_equal(p, a), (p, a, b)
                count += 1
                if x == y and b == 2 and a in (1, 4, 6, 10):
                    ones.append((p, a))
    assert formula(257, 10) == 1
    assert formula(257, 9) == 2
    assert formula(65537, 18) == 1
    assert formula(65537, 17) == 2
    print('VERIFY_OK cases=%d equality_samples=%s Fermat_thresholds=(257,65537)' % (count, ones[:15]))


if __name__ == '__main__':
    main()
