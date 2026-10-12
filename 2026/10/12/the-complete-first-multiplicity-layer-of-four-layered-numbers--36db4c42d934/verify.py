#!/usr/bin/env python3
"""Exact rational prime-factor search and divisor-partition certificate checks.

Run: python3 verify.py
All necessary certificate data live in partitions.json alongside this script.
"""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json

EXPECTED = [27720, 32760, 120120, 180180, 235620]


def prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def next_prime(n):
    n += 1
    while not prime(n):
        n += 1
    return n


def envelope(last, remaining):
    """Maximal Euler-factor product for at most `remaining` later primes."""
    result = Fraction(1)
    for _ in range(remaining):
        last = next_prime(last)
        result *= Fraction(last, last - 1)
    return result


def enumerate_abundant_exact_omega(total):
    count_nodes = 0
    count_prime_trials = 0
    maximal_tested_prime = 0
    hits = []

    def visit(last, left, n, ratio, factors):
        nonlocal count_nodes, count_prime_trials, maximal_tested_prime
        count_nodes += 1
        if left == 0:
            if ratio >= 4:
                hits.append((n, factors, ratio))
            return
        # A threshold-reaching partial prefix would permit arbitrarily large
        # appended primes. This cannot occur for total<=8, as independently
        # established by the completed enumeration through total=7.
        assert ratio < 4, ('premature threshold', n, ratio)
        if ratio * envelope(last, left) < 4:
            return
        p = next_prime(last)
        while True:
            count_prime_trials += 1
            maximal_tested_prime = max(maximal_tested_prime, p)
            # If even the supremum for this p and the remaining prime slots
            # is below four, the same holds for every larger first prime.
            if ratio * Fraction(p, p - 1) * envelope(p, left - 1) < 4:
                break
            for exponent in range(1, left + 1):
                exact_ratio = ratio * Fraction(p ** (exponent + 1) - 1,
                                               p ** exponent * (p - 1))
                if exact_ratio * envelope(p, left - exponent) >= 4:
                    visit(p, left - exponent, n * p ** exponent,
                          exact_ratio, factors + ((p, exponent),))
            p = next_prime(p)

    visit(1, total, 1, Fraction(1), ())
    return sorted(hits), count_nodes, count_prime_trials, maximal_tested_prime


def factorize(n):
    fac = {}
    p = 2
    remaining = n
    while p * p <= remaining:
        if remaining % p == 0:
            a = 0
            while remaining % p == 0:
                remaining //= p
                a += 1
            fac[p] = a
        p = next_prime(p)
    if remaining > 1:
        fac[remaining] = 1
    return fac


def exact_divisors(n):
    divisors = [1]
    for p, exponent in factorize(n).items():
        divisors = [d * p ** e for d in divisors for e in range(exponent + 1)]
    return sorted(divisors)


def verify():
    from_json = json.loads((Path(__file__).resolve().parent / 'partitions.json').read_text('utf-8'))
    stats = []
    discovered = []
    for omega in range(1, 9):
        hits, nodes, trials, pmax = enumerate_abundant_exact_omega(omega)
        assert len({n for n, _, _ in hits}) == len(hits)
        if omega < 8:
            assert hits == [], ('below-boundary counterexample', omega, hits)
        else:
            assert [n for n, _, _ in hits] == EXPECTED
            discovered = hits
        stats.append((omega, nodes, trials, pmax, len(hits)))

    assert set(from_json) == {str(n) for n in EXPECTED}
    for n, fac, ratio in discovered:
        assert dict(fac) == factorize(n)
        assert sum(a for _, a in fac) == 8
        ds = exact_divisors(n)
        sigma = sum(ds)
        assert Fraction(sigma, n) == ratio
        assert sigma % 4 == 0
        cert = from_json[str(n)]
        assert cert['target'] == sigma // 4
        bins = cert['bins']
        assert len(bins) == 4
        assert all(isinstance(b, list) and b for b in bins)
        assert sorted(d for b in bins for d in b) == ds
        assert all(sum(b) == sigma // 4 for b in bins)
        print(f'PARTITION_OK n={n} omega=8 sigma={sigma} target={sigma//4} '
              f'divisors={len(ds)} ratio={ratio} bins={[len(b) for b in bins]}')
    print(f'EXHAUSTIVE_SEARCH_OK maxima_by_omega={stats} '
          f'four_abundant_omega_le8={EXPECTED} four_layered_omega_le8={EXPECTED}')


if __name__ == '__main__':
    verify()
