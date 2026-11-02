#!/usr/bin/env python3
"""Exact finite checks for geometric-odds sign-flip chains.

All computations use integers/Fractions; no random sampling or external packages.
Finite checks corroborate the proof but do not establish its all-length claim.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb


def gaussian(n, k, q):
    if k < 0 or k > n or n < 0:
        return Fraction(0)
    values = [Fraction(0)] * (k + 1)
    values[0] = Fraction(1)
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            values[j] += q ** (i - j) * values[j - 1]
    return values[k]


def normal_mass(n, k, q):
    return q ** (k * (k + 1) // 2) * gaussian(n - 1, k, q)


def direct(n, k, q, scale):
    masses = defaultdict(Fraction)
    for changes in combinations(range(1, n), k):
        walls = set(changes)
        weight = Fraction(1)
        for i in walls:
            weight *= scale * q ** i
        for first in (-1, 1):
            sign, total = first, first
            for i in range(1, n):
                if i in walls:
                    sign = -sign
                total += sign
            a = (n + total) // 2
            masses[a] += weight
    z = sum(masses.values())
    return {a: m / z for a, m in masses.items()}


def formula(n, j, q):
    values = {}
    z = 2 * normal_mass(n, 2 * j - 1, q)
    for a in range(j, n - j + 1):
        b = n - a
        w = q ** (2 * j * (j - 1)) * (q ** a + q ** b)
        w *= gaussian(a - 1, j - 1, q ** 2)
        w *= gaussian(b - 1, j - 1, q ** 2)
        if w:
            values[a] = w / z
    return values


def tails(values, n):
    return {h: sum(v for a, v in values.items() if abs(2 * a - n) >= h)
            for h in range(n + 1)}


def four_moment_zero(weights, k):
    # Exact probability that the four-spin magnetization equals zero.
    Z = Fraction(0)
    A = Fraction(0)
    for subset in combinations(range(1, 4), k):
        w = Fraction(1)
        for i in subset:
            w *= weights[i-1]
        Z += w
        state, total = 1, 1
        for i in range(1, 4):
            if i in subset:
                state = -state
            total += state
        if total == 0:
            A += w
    return A / Z


def main():
    checks = 0
    for q in (Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)):
        for n in range(2, 12):
            all_laws = {}
            for k in range(n):
                law = direct(n, k, q, Fraction(3, 2))
                assert sum(law.values()) == 1
                assert all(law.get(a, 0) == law.get(n-a, 0) for a in range(n+1))
                all_laws[k] = law
                checks += 2
            for j in range(1, n // 2 + 1):
                odd = all_laws[2*j - 1]
                expected = formula(n, j, q)
                assert odd == expected, (n, j, q, odd, expected)
                checks += 1
                if 2 * j <= n - 1:
                    assert odd == all_laws[2*j], (n, j, q)
                    checks += 1
                if j < n // 2:
                    next_law = all_laws[2*j + 1]
                    t1, t2 = tails(odd, n), tails(next_law, n)
                    assert all(t1[h] >= t2[h] for h in range(n+1))
                    assert any(t1[h] > t2[h] for h in range(n+1))
                    checks += 2
                    r1 = {abs(2*a-n) for a in odd}
                    r2 = {abs(2*a-n) for a in next_law}
                    ratios = []
                    for r in sorted(r1 & r2):
                        p1 = sum(v for a, v in odd.items() if abs(2*a-n) == r)
                        p2 = sum(v for a, v in next_law.items() if abs(2*a-n) == r)
                        ratios.append(p2/p1)
                    assert all(x >= y for x,y in zip(ratios, ratios[1:]))
                    checks += 1
    testsets = [(Fraction(1),Fraction(1),Fraction(1)),
                (Fraction(1),Fraction(2),Fraction(4)),
                (Fraction(1),Fraction(2),Fraction(5)),
                (Fraction(3),Fraction(6),Fraction(12)),
                (Fraction(1),Fraction(3),Fraction(6)),
                (Fraction(2),Fraction(1),Fraction(2))]
    for w in testsets:
        equal = four_moment_zero(w,1) == four_moment_zero(w,2)
        assert equal == (w[1]**2 == w[0]*w[2]), (w,equal)
        checks += 1
    print('PASS exact assertions:', checks)
    print('Checked complete weighted spin configurations for n=2..11, q=1/2,1,3/2,2')
    print('Verified Gaussian-binomial law, odd/even plateaus, tail order and likelihood ratios')
    print('Verified four-site geometric-odds characterization')


if __name__ == '__main__':
    main()
