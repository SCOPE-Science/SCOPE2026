#!/usr/bin/env python3
"""Exact residue checks for reciprocal-sum square-defect events.

Runs with the Python standard library. This finite check supplements the proof.
"""
from fractions import Fraction
from math import gcd, isqrt


def factor(n):
    ans = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            ans.append((p, a))
        p += 1
    if n > 1:
        ans.append((n, 1))
    return ans


def local_counts(p):
    if p == 2:
        return 1, 0
    if p % 4 == 3:
        return 0, 0
    if p == 5:
        return 2, 2
    if p % 20 in (13, 17):
        return 2, 0
    assert p % 20 in (1, 9)
    return 2, 4


def expected_counts(h):
    factors = factor(h)
    modulus = h
    no2 = no3 = neither = Fraction(1)
    for p, a in factors:
        modulus *= p
        c2, c3 = local_counts(p)
        alpha = Fraction(c2, p ** (a+1))
        beta = Fraction(c3, p ** (a+1))
        no2 *= 1 - alpha
        no3 *= 1 - beta
        neither *= 1 - alpha - beta
    return modulus, tuple(int(modulus * q) for q in
                          (1-no2, 1-no3, 1-no2-no3+neither, neither))


def direct_events(h, x):
    g = gcd(h, x)
    u, v = x // g, h // g
    u1, v1 = u*u + v*v, u*v
    u2 = u1*u1 + v1*v1
    return gcd(h, u1) > 1, gcd(h, u2) > 1


def is_integer_square(q):
    return q.denominator == 1 and isqrt(q.numerator)**2 == q.numerator


def rational_events(h, x):
    x0 = Fraction(x)
    x1 = Fraction(h*h, x)
    x2 = Fraction(h*h, 1)/(x0+x1)
    x3 = Fraction(h*h, 1)/(x0+x1+x2)
    def bad(y):
        return not is_integer_square(Fraction(2*y.numerator, h) + y.denominator)
    return bad(x2), bad(x3)


def later_defect(h, x, steps=28):
    g = gcd(h, x)
    u, v = x // g % h, h // g % h
    bad = []
    for n in range(1, steps):
        u, v = (u*u+v*v) % h, (u*v) % h
        if gcd(h, u) != 1:
            bad.append(n+1)
    return bad


def main():
    tested_h = sorted(set([h for h in range(1, 91) if expected_counts(h)[0] <= 5000]
                          + [13*17, 5*17, 2*13, 3*13, 2*17, 5*13]))
    residue_cases = rational_cases = late_cases = 0
    for h in tested_h:
        modulus, counts = expected_counts(h)
        if modulus > 60000:
            continue
        got2 = got3 = gotboth = gotneither = 0
        for x in range(1, modulus+1):
            ev2, ev3 = direct_events(h, x)
            got2 += ev2
            got3 += ev3
            gotboth += ev2 and ev3
            gotneither += not (ev2 or ev3)
            residue_cases += 1
            if x <= min(30, modulus):
                assert (ev2, ev3) == rational_events(h, x), (h, x)
                rational_cases += 1
        assert (got2, got3, gotboth, gotneither) == counts, (h, counts, got2, got3, gotboth, gotneither)
        allowed = all(p == 2 or p % 4 == 3 or p % 20 in (13, 17) for p, a in factor(h))
        if allowed:
            for x in range(1, min(modulus, 300)+1):
                assert all(n == 2 for n in later_defect(h,x)), (h,x)
                late_cases += 1
    for h in (5, 25, 41, 61, 65, 85, 101, 109):
        forbidden = [p for p, a in factor(h) if p == 5 or p % 20 in (1, 9)]
        assert forbidden
        witness = next(x for x in range(1, 2*h*h+1) if direct_events(h,x)[1])
        assert 3 in later_defect(h,witness,7)
    print('Residue classes checked:', residue_cases)
    print('Direct rational checks:', rational_cases)
    print('Longer recurrence checks in rigid class:', late_cases)
    print('Forbidden-class third-index witnesses: 8')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
