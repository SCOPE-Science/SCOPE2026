#!/usr/bin/env python3
"""Finite checks of local modular-order classification for fixed prime supports."""
from itertools import combinations, product
from math import gcd


def factor(x):
    out = {}
    d = 2
    while d * d <= x:
        while x % d == 0:
            out[d] = out.get(d, 0) + 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def vp(x, p):
    a = 0
    while x % p == 0:
        x //= p
        a += 1
    return a


def multiplicative_order(base, modulus):
    assert gcd(base, modulus) == 1
    phi = modulus
    for p in factor(modulus):
        phi = phi // p * (p - 1)
    order = phi
    for q, exponent in factor(phi).items():
        for _ in range(exponent):
            if order % q == 0 and pow(base, order // q, modulus) == 1:
                order //= q
            else:
                break
    assert pow(base, order, modulus) == 1
    return order


def threshold(base, support, powers):
    odd = [p for p in support if p != 2]
    orders = {p: multiplicative_order(base, p) for p in odd}
    for p in odd:
        s = vp(pow(base, orders[p]) - 1, p)
        h = max([0] + [vp(orders[q], p) for q in odd if q != p])
        if powers[support.index(p)] < s + h:
            return False
    if 2 not in support:
        return True
    g = max([0] + [vp(orders[q], 2) for q in odd])
    a = powers[support.index(2)]
    d = vp(base - 1, 2)
    if d >= 2:
        return a >= d + g
    e = vp(base + 1, 2)
    if g == 0:
        return a == 1 or a >= e + 1
    return a >= e + g


def direct(base, support, powers):
    n = 1
    for p, a in zip(support, powers):
        n *= p ** a
    L = multiplicative_order(base, n)
    return all(pow(base, L, p ** (a + 1)) != 1 for p, a in zip(support, powers))


def run():
    tested = 0
    observed_exception = 0
    for base in (2, 3, 5, 7, 9, 11, 13, 17):
        allowed = [p for p in (2, 3, 5, 7, 11) if gcd(base, p) == 1]
        for size in (1, 2, 3):
            for primes in combinations(allowed, size):
                for powers in product((1, 2, 3, 4), repeat=size):
                    n = 1
                    for p, a in zip(primes, powers):
                        n *= p ** a
                    if n > 4000000:
                        continue
                    lhs = direct(base, primes, powers)
                    rhs = threshold(base, primes, powers)
                    assert lhs == rhs, (base, primes, powers, lhs, rhs)
                    tested += 1
    for a, expected in ((1, True), (2, False), (3, False), (4, True), (5, True)):
        v = direct(7, (2, 3), (a, 1))
        assert v == expected, (a, v)
        observed_exception += 1
    assert tested > 3000
    print(f'VERIFY_OK modular_order_cases={tested} dyadic_examples={observed_exception} classification=PASS')


if __name__ == '__main__':
    run()
