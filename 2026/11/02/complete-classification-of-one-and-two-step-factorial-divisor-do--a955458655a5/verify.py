#!/usr/bin/env python3
"""Exact certificate for small factorial-divisor doubling windows.

All comparisons are integer inequalities. The search 2 <= m < 2048
is exhaustive; estimates in the accompanying proof handle m >= 2048.
"""
from math import isqrt, gcd

LIMIT = 2048

def sieve_spf(n):
    spf = list(range(n + 1))
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for k in range(p * p, n + 1, p):
                if spf[k] == k:
                    spf[k] = p
    return spf

def factors(x, spf):
    result = {}
    while x > 1:
        p = spf[x]
        a = 0
        while x % p == 0:
            x //= p
            a += 1
        result[p] = a
    return result

def factorial_valuation(m, p):
    v = 0
    while m:
        m //= p
        v += m
    return v

def ratio(m, spf):
    N = D = 1
    for p, a in factors(m, spf).items():
        v = factorial_valuation(m - 1, p)
        N *= v + a + 1
        D *= v + 1
    return N, D

def is_prime(n, spf):
    return n > 1 and spf[n] == n

def double_prime_pair(m, spf):
    return ((m % 2 == 0 and m % 3 != 0 and is_prime(m // 2, spf)
             and (m + 1) % 3 == 0 and is_prime((m + 1) // 3, spf))
            or (m % 3 == 0 and is_prime(m // 3, spf)
                and (m + 1) % 2 == 0 and is_prime((m + 1) // 2, spf)))

def main():
    spf = sieve_spf(LIMIT)
    exceptional = set()
    pair_hits = 0
    total_hits = 0
    one_step_composite = []
    examined = 0
    for m in range(2, LIMIT):
        n1, d1 = ratio(m, spf)
        n2, d2 = ratio(m + 1, spf)
        if not is_prime(m, spf) and n1 >= 2*d1:
            one_step_composite.append(m)
        if not is_prime(m, spf) and not is_prime(m+1, spf):
            examined += 1
            hit = (n1*n2 >= 2*d1*d2)
            pp = double_prime_pair(m, spf)
            if pp:
                assert hit, (m, 'missed prime pair')
                pair_hits += 1
            if hit:
                total_hits += 1
                if not pp:
                    exceptional.add(m)
            assert (not hit) or pp or m in {8, 15, 20, 25, 34}, m
    assert one_step_composite == [4], one_step_composite
    assert exceptional == {8, 15, 20, 25, 34}, exceptional
    assert total_hits == pair_hits + len(exceptional)
    # Independent cumulative factorial-divisor calculation on the WHOLE finite range:
    fac_tau = 1
    v = {}
    tau_factorial = {1: 1}
    checks = 0
    for m in range(2, LIMIT + 1):
        previous = fac_tau
        for p, a in factors(m, spf).items():
            old = v.get(p, 0)
            new = old + a
            v[p] = new
            fac_tau = fac_tau // (old + 1) * (new + 1) if fac_tau % (old + 1) == 0 else None
            assert fac_tau is not None
        qn, qd = ratio(m, spf)
        assert fac_tau * qd == previous * qn, (m, 'independent factorial')
        checks += 1
        tau_factorial[m] = fac_tau
    for m in range(2, LIMIT):
        if not is_prime(m, spf) and not is_prime(m + 1, spf):
            is_doubled = tau_factorial[m + 1] >= 2 * tau_factorial[m - 1]
            predicted = double_prime_pair(m, spf) or m in {8, 15, 20, 25, 34}
            assert is_doubled == predicted, (m, 'cumulative ratio comparison')
    print(f'VERIFY_OK composite_pairs={examined} two_step_hits={total_hits} prime_pair_hits={pair_hits} '
          f'exceptional={sorted(exceptional)} one_step={one_step_composite} '
          f'independent_factorial_checks={checks} exact_integer=PASS')

if __name__ == '__main__':
    main()
