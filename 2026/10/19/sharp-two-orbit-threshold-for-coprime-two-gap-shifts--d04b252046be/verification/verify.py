#!/usr/bin/env python3
"""Independent exact finite diagnostics for two-length S-gap periodic orbits.

Run with: python3 verification/verify.py
Requires Python standard library only. These are diagnostics, not a proof
of the all-parameter theorem; see RESULT.md for the general argument.
"""
from itertools import product
from math import comb, gcd


def mu(n):
    k, factors = n, 0
    divisor = 2
    while divisor * divisor <= k:
        if k % divisor == 0:
            k //= divisor
            factors += 1
            if k % divisor == 0:
                return 0
        while k % divisor == 0:
            k //= divisor
        divisor += 1
    if k > 1:
        factors += 1
    return (-1) ** factors


def necklace(r, s):
    total = sum(mu(d) * comb((r + s) // d, r // d)
                for d in range(1, gcd(r, s) + 1) if gcd(r, s) % d == 0)
    assert total % (r + s) == 0
    return total // (r + s)


def necklaces_at_length(a, b, n):
    answer = (n == a) + (n == b)
    for r in range(1, n // a + 1):
        remaining = n - a * r
        if remaining > 0 and remaining % b == 0:
            answer += necklace(r, remaining // b)
    return answer


def zeta_orbits(a, b, N):
    # Earlier S-gap zeta formula: zeta(t)=1/(1-t**a-t**b).
    # Its logarithmic derivative gives periodic point counts.
    coefficient = [0] * (N + 1)
    coefficient[0] = 1
    for n in range(1, N + 1):
        coefficient[n] = (coefficient[n - a] if n >= a else 0) + (
            coefficient[n - b] if n >= b else 0)
    points = [0] * (N + 1)
    for n in range(1, N + 1):
        points[n] = (a * coefficient[n - a] if n >= a else 0) + (
            b * coefficient[n - b] if n >= b else 0)
    orbits = [0] * (N + 1)
    for n in range(1, N + 1):
        numerator = sum(mu(d) * points[n // d] for d in range(1, n + 1)
                        if n % d == 0)
        assert numerator % n == 0
        orbits[n] = numerator // n
    return orbits


def direct_cyclic_orbits(a, b, n):
    results = set()
    for p in product((0, 1), repeat=n):
        positions = [i for i, symbol in enumerate(p) if symbol]
        if not positions:
            continue
        k = len(positions)
        lengths = [((positions[(j + 1) % k] - positions[j]) % n)
                   if k > 1 else n for j in range(k)]
        if any(length not in (a, b) for length in lengths):
            continue
        if any(p == p[shift:] + p[:shift] for shift in range(1, n)):
            continue
        results.add(min(p[shift:] + p[:shift] for shift in range(n)))
    return len(results)


def main():
    zeta_cases = 0
    threshold_cases = 0
    direct_cases = 0
    for a in range(2, 14):
        for b in range(a + 1, 22):
            if gcd(a, b) != 1:
                continue
            M = max((a + 1) * b, 2 * (a + b))
            upper = M + 60
            independent = zeta_orbits(a, b, upper)
            for n in range(1, upper + 1):
                assert independent[n] == necklaces_at_length(a, b, n), (
                    'zeta/necklace discrepancy', a, b, n)
                zeta_cases += 1
            assert independent[M] == 1, ('sharp endpoint', a, b)
            for n in range(M + 1, upper + 1):
                assert independent[n] >= 2, ('eventual multiplicity', a, b, n)
                threshold_cases += 1
    for a in range(2, 6):
        for b in range(a + 1, 9):
            if gcd(a, b) != 1:
                continue
            for n in range(1, 17):
                assert direct_cyclic_orbits(a, b, n) == necklaces_at_length(a, b, n), (
                    'cyclic enumeration', a, b, n)
                direct_cases += 1
    print('PASS:', zeta_cases, 'exact zeta/necklace comparisons;',
          threshold_cases, 'sharp-threshold instances;',
          direct_cases, 'independent cyclic-word enumerations.')
    for a, b in ((2, 3), (3, 5), (4, 7), (5, 8)):
        M = max((a + 1) * b, 2 * (a + b))
        print('example', a, b, 'last singleton', M, 'Q(M)=',
              necklaces_at_length(a, b, M), 'Q(M+1)=',
              necklaces_at_length(a, b, M + 1))


if __name__ == '__main__':
    main()
