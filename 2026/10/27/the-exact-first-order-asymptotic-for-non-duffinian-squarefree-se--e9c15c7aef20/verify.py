"""Exact finite corroboration for exceptional Duffinian semiprimes.

Run with Python 3 standard library: python verify.py
This does not prove the asymptotic.
"""
from bisect import bisect_right
from math import gcd, isqrt, log


def primes_to(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * ((n-p*p)//p + 1)
    return [i for i, v in enumerate(sieve) if v]


def independent_counts(limit, primes):
    # Criterion count and independent gcd computation across ALL distinct-prime pairs.
    exact = 0
    predicted = 0
    total = 0
    for i, p in enumerate(primes):
        if p * p > limit:
            break
        stop = bisect_right(primes, limit // p)
        for q in primes[i+1:stop]:
            total += 1
            via_gcd = gcd(p*q, (p+1)*(q+1)) > 1
            via_criterion = (p == 2 or (q+1) % p == 0)
            assert via_gcd == via_criterion, (limit, p, q)
            exact += via_gcd
            predicted += via_criterion
    assert exact == predicted
    return total, exact


def constant_interval(N, primes):
    # Sum over p>=3 with p<=N. Tail bounded by sum_{n>N} 1/[n(n-1)] = 1/N.
    v = 0.5 + sum(1/(p*(p-1)) for p in primes if 3 <= p <= N)
    return v, v + 1/N


def main():
    limits = (1000, 10000, 100000, 1000000)
    p = primes_to(limits[-1])
    c_lo, c_hi = constant_interval(limits[-1], p)
    assert 0.773156 < c_lo < c_hi < 0.773158
    for X in limits:
        total, bad = independent_counts(X, p)
        assert 0 < bad < total
        print(f'X={X} total={total} exceptional={bad} norm={bad*log(X)/X:.8f}')
    print(f'C interval at prime cutoff 1000000: [{c_lo:.12f}, {c_hi:.12f}]')
    print('VERIFY_OK: independent gcd/congruence comparison, exact pair census, rigorous constant interval')

if __name__ == '__main__':
    main()
