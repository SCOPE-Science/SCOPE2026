#!/usr/bin/env python3
"""Exact-integer checks of Pell companion index-gcd classifications.

All computations are finite tests supplementary to the symbolic proof.
"""
from math import gcd


def q_pair_mod(n, modulus):
    """Return (Q_n,Q_{n+1}) modulo modulus by Pell trace doubling."""
    if modulus < 1 or n < 0:
        raise ValueError('invalid modulus or index')
    if n == 0:
        return (1 % modulus, 1 % modulus)
    a, b = q_pair_mod(n // 2, modulus)
    sign = -1 if (n // 2) % 2 else 1
    even = (2 * a * a - sign) % modulus
    odd = (2 * a * b - sign) % modulus
    if n % 2 == 0:
        return even, odd
    return odd, (2 * b * b + sign) % modulus


def factor(n):
    res = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            res.append((p, a))
        p = 3 if p == 2 else p + 2
    if n > 1:
        res.append((n, 1))
    return res


def expected(k, factors):
    if len(factors) < 2:
        return 1
    (p,a),(q,b) = factors
    return (q ** b) if q_pair_mod(p ** a, q)[0] == 0 else 1


def run():
    pell_q = [1,1]
    for i in range(2,4001):
        pell_q.append(2*pell_q[-1] + pell_q[-2])
    for n in range(4001):
        if q_pair_mod(n, 1000003)[0] != pell_q[n] % 1000003:
            raise AssertionError(('fast Q mismatch',n))
    count = 0
    count_two = 0
    for k in range(2,30001):
        fs = factor(k)
        if len(fs) <= 2:
            g = gcd(k, q_pair_mod(k,k)[0])
            target = expected(k,fs)
            if g != target:
                raise AssertionError(('gcd mismatch',k,fs,g,target))
            count += 1
            if len(fs)==2: count_two += 1
    # Specific direct high-index tests computed strictly modulo each index.
    high_cases = [
        2**31 * 3**13,
        3**20 * 7**9,
        5**12 * 11**10,
        7**9 * 17**11,
        11**7 * 13**8,
        2**64 * 17**32,
        3**31 * 41**13,
    ]
    for k in high_cases:
        fs = factor_known(k)
        target = expected(k,fs)
        g = gcd(k, q_pair_mod(k,k)[0])
        if g != target:
            raise AssertionError(('high-index mismatch',k,g,target))
    for a in range(2,100):
        k=3*(2**a)
        if gcd(k,q_pair_mod(k,k)[0]) != 1:
            raise AssertionError(('conjecture counterfamily failed',a))
    for b in range(1,61):
        k=2*3**b
        if gcd(k,q_pair_mod(k,k)[0]) != 3**b:
            raise AssertionError(('positive family failed',b))
    print('VERIFY_OK')
    print('direct_recurrence_Q_mod_fast_indices_0_to_4000=PASS')
    print(f'omega_at_most_two_indices_2_to_30000={count}_PASS')
    print(f'exact_two_prime_support_indices={count_two}_PASS')
    print(f'large_index_exact_modular_tests={len(high_cases)}_PASS')
    print('published_conjecture_counterfamily_a_2_to_99=98_PASS')
    print('nontrivial_full_prime_power_gcd_family_b_1_to_60=60_PASS')
    print('finite_tests_supplement_symbolic_unrestricted_proof')


def factor_known(k):
    # Only used for seven explicitly supplied large-index cases.
    known = [2,3,5,7,11,13,17,41]
    fs=[]
    for p in known:
        if k%p==0:
            e=0
            while k%p==0:
                k//=p;e+=1
            fs.append((p,e))
    if k!=1:raise AssertionError(('unexpected prime',k))
    return fs


if __name__=='__main__':
    run()
