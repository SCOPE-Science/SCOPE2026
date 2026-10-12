#!/usr/bin/env python3
"""Exact verification of the first four-prime-support tau/totient fiber.

Python 3 standard library only. The unbounded totient lower bound is proved
in RESULT.md; enumeration here is of a provably finite divisor set.
"""
import csv
import math
import sys

D = 57600
BOUND = 75361


def spf_sieve(limit):
    spf = list(range(limit + 1))
    for p in range(2, math.isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def factor_with_spf(n, spf):
    out = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out


def factor_trial(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p += 1 if p == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out


def tau_factors(factors):
    return math.prod(e + 1 for p, e in factors)


def phi_factors(factors):
    return math.prod((p - 1) * p ** (e - 1) for p, e in factors)


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def divisors(n):
    out = [1]
    for p, e in factor_trial(n):
        old = list(out)
        for a in range(1, e + 1):
            out.extend(d * p ** a for d in old)
    return sorted(out)


def fiber():
    prime_options = [d + 1 for d in divisors(D) if is_prime(d + 1)]
    sol = []

    def visit(start, remaining, selected):
        if len(selected) == 4:
            if remaining == 1:
                sol.append(tuple(selected))
            return
        for j in range(start, len(prime_options)):
            p = prime_options[j]
            if remaining % (p - 1) == 0:
                visit(j + 1, remaining // (p - 1), selected + [p])

    visit(0, D, [])
    sol.sort(key=lambda ps: math.prod(ps))
    assert len(prime_options) == 33
    assert len(sol) == 37
    assert len(set(sol)) == 37
    assert sol[0] == (11, 13, 17, 31)
    assert math.prod(sol[0]) == BOUND
    for ps in sol:
        assert len(ps) == 4 and len(set(ps)) == 4
        assert math.prod(p - 1 for p in ps) == D
        assert all(is_prime(p) for p in ps)
        assert tau_factors([(3, 2), (5, 2), (2, 8)]) == 81
        assert math.prod(3 for _ in ps) == 81
    return prime_options, sol


def below_bound():
    spf = spf_sieve(BOUND)
    four_support_tests = 0
    hits = []
    for n in range(2, BOUND):
        f = factor_with_spf(n, spf)
        if len(f) != 4:
            continue
        four_support_tests += 1
        tau_sq = math.prod(2 * e + 1 for p, e in f)
        phi = phi_factors(f)
        tau_phi = tau_factors(factor_with_spf(phi, spf))
        if tau_sq == tau_phi:
            hits.append(n)
    assert not hits, hits
    at_bound = factor_with_spf(BOUND, spf)
    assert at_bound == [(11, 1), (13, 1), (17, 1), (31, 1)]
    assert phi_factors(at_bound) == D
    assert tau_factors(factor_with_spf(D, spf)) == 81
    assert math.prod(2 * e + 1 for p, e in at_bound) == 81
    return four_support_tests


def main():
    prime_options, sol = fiber()
    scan_count = below_bound()
    if len(sys.argv) == 3 and sys.argv[1] == '--csv':
        with open(sys.argv[2], 'w', encoding='utf-8', newline='') as f:
            w = csv.writer(f, lineterminator='\n')
            w.writerow(['n', 'p1', 'p2', 'p3', 'p4', 'phi_n'])
            for ps in sol:
                w.writerow([math.prod(ps), *ps, D])
    elif len(sys.argv) != 1:
        raise SystemExit('usage: python3 verify.py [--csv output.csv]')
    print('VERIFY_OK')
    print(f'min_totient={D} prime_options={len(prime_options)} fiber_count={len(sol)}')
    print(f'least_four_support={math.prod(sol[0])} factors={sol[0]}')
    print(f'complete_below_minimum_four_support_tests={scan_count} hits=0')
    print('identity_checks=tau(n^2)=81=tau(phi(n))')


if __name__ == '__main__':
    main()
