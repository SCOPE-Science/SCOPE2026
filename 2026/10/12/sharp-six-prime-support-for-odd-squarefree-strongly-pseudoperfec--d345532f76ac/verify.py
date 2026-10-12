#!/usr/bin/env python3
"""Exact exhaustive arithmetic verification of the odd squarefree prime-support bound.
No external packages are required; execute: python3 verify.py
"""
import csv
import sys
from math import isqrt
from pathlib import Path

BOUNDS = {11: 384, 13: 64, 17: 30, 19: 25}
FACTORS = (3, 5, 7)
WITNESS_FACTORS = (3, 5, 11, 13, 19, 23)
WITNESS_OMITTED_PAIRS = ((55, 17043), (57, 16445), (65, 14421),
                         (143, 6555), (165, 5681))


def is_prime(n):
    if n < 2:
        return False
    return all(n % k for k in range(2, isqrt(n) + 1))


def prime_list(n):
    # Independent sieve, cross-checked against trial division.
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            for v in range(p*p, n + 1, p):
                sieve[v] = 0
    result = [p for p in range(2, n+1) if sieve[p]]
    assert result == [p for p in range(2, n+1) if is_prime(p)]
    return result


def complementary_pairs(primes):
    n = 1
    divisors = [1]
    for p in primes:
        assert is_prime(p) and n % p != 0
        n *= p
        divisors += [d * p for d in divisors]
    assert len(divisors) == 2**len(primes)
    pairs = sorted((d, n//d) for d in divisors if d*d < n)
    assert len(pairs)*2 == len(divisors)
    assert len({x for pair in pairs for x in pair}) == len(divisors)
    assert all(x*y == n for x,y in pairs)
    return n, pairs


def subset_bitset(weights):
    bits = 1
    for w in weights:
        bits |= bits << w
    return bits


def subset_mitm_present(weights, target):
    assert len(weights) == 16
    left = [sum(weights[i] for i in range(8) if mask & (1 << i))
            for mask in range(256)]
    right = {sum(weights[8+i] for i in range(8) if mask & (1 << i))
             for mask in range(256)}
    return any(target - v in right for v in left)


def candidate_rows():
    plist = prime_list(384)
    seen = set()
    for q, upper in BOUNDS.items():
        assert upper == (32*(q+1)) // (3*q-32)
        for r in plist:
            if not (q < r <= upper):
                continue
            n, pairs = complementary_pairs((*FACTORS, q, r))
            assert len(pairs) == 16
            sigma = 192*(q+1)*(r+1)
            delta = sigma - 2*n
            assert delta > 0 and delta == sum(x+y for x,y in pairs) - 2*n
            weights = [x+y for x,y in pairs]
            bits = subset_bitset(weights)
            present = bool((bits >> delta) & 1)
            independently_present = subset_mitm_present(weights, delta)
            assert present == independently_present
            assert not present, (q,r)
            # These two nearest reachable sums provide convenient audit checks.
            lower = ((bits & ((1 << delta) - 1)).bit_length() - 1)
            tail = bits >> (delta+1)
            assert tail
            upper_reachable = delta+1 + ((tail & -tail).bit_length()-1)
            row = (q, r, n, delta, lower, upper_reachable)
            assert (q,r) not in seen
            seen.add((q,r))
            yield row


def check_witness():
    n, pairs = complementary_pairs(WITNESS_FACTORS)
    assert n == 937365
    omitted = set(WITNESS_OMITTED_PAIRS)
    assert len(omitted) == 5 and omitted.issubset(set(pairs))
    sigma = sum(x+y for x,y in pairs)
    assert sigma == 1935360
    removed = sum(x+y for x,y in omitted)
    assert removed == 60630 and sigma - removed == 2*n
    assert len([p for p in WITNESS_FACTORS if is_prime(p)]) == 6
    return n,sigma,removed


def main():
    rows = list(candidate_rows())
    counts = {q:sum(x[0] == q for x in rows) for q in BOUNDS}
    assert counts == {11:71, 13:12, 17:3, 19:1}
    assert len(rows)==87
    cert_path = Path(__file__).with_name('cases.csv')
    headers = ('q','r','n','delta','max_subset_below_delta','min_subset_above_delta')
    if sys.argv[1:] == ['--generate-certificate']:
        with cert_path.open('w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(headers)
            writer.writerows(rows)
    with cert_path.open(newline='',encoding='utf-8') as f:
        reader=csv.reader(f)
        assert tuple(next(reader))==headers
        embedded_rows=[tuple(int(v) for v in line) for line in reader]
    assert embedded_rows==rows, 'The attached certificate differs from exact regenerated values'
    n,sigma,delta=check_witness()
    checksum=0
    for q,r,N,D,lo,hi in rows:
        checksum=(checksum*1315423911 + q*1000+r+D)%1000000007
    assert checksum==83946581
    print('odd_squarefree_support_bound: PASS')
    print('prime_enumeration: sieve == independent trial division')
    print('candidate_q_counts:',counts)
    print('exhaustive_five_prime_cases:',len(rows))
    print('two_independent_subset_methods: 87/87 agree, all exclude')
    print('case_checksum_mod_1000000007:',checksum)
    print('certificate_rows_verified:',len(embedded_rows))
    print('sharp_six_prime_witness:',n,'sigma:',sigma,'omitted_sum:',delta)
    print('all_checks: PASS')

if __name__=='__main__':
    main()
