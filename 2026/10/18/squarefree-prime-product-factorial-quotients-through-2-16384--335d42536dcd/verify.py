"""Exact squarefreeness census for the prime-product/factorial quotient.

Uses only integer arithmetic. The ternary low-digit filter is a necessary
condition, never a probabilistic primality or random sampling test.
"""
from math import isqrt
from time import monotonic

BIT_BOUND = 16384
TERNARY_BLOCK = 3**12
TERNARY_MODULUS = TERNARY_BLOCK**2


def ternary_digit_sum(x):
    s = 0
    while x:
        x, r = divmod(x, 3)
        s += r
    return s


def limited_ternary_digit_sum(x, max_sum):
    s = 0
    while x:
        x, r = divmod(x, 3)
        s += r
        if s > max_sum:
            return False
    return True


def candidate_indices(N):
    # If the quotient is squarefree, the binary digit sum of m=n+1 is at most 2.
    # Also the ternary digit sum is <= 3 (m odd) or <= 4 (m even).
    table = bytearray(TERNARY_BLOCK)
    for x in range(1, TERNARY_BLOCK):
        table[x] = table[x // 3] + x % 3
    def low_sum_24(x):
        return table[x % TERNARY_BLOCK] + table[x // TERNARY_BLOCK]
    power_residue = [1]
    for _ in range(N):
        power_residue.append((2 * power_residue[-1]) % TERNARY_MODULUS)
    hits = []
    high = 1
    for a in range(N+1):
        ra = power_residue[a]
        # One binary one: m=2^a.
        if low_sum_24(ra) <= 4 and limited_ternary_digit_sum(high, 3 if a==0 else 4):
            hits.append((a, -1, high-1))
        # Two binary ones: m=2^a+2^b, 0<=b<a.
        for b in range(a):
            if low_sum_24((ra + power_residue[b]) % TERNARY_MODULUS) > 4:
                continue
            m = high + (1 << b)
            if limited_ternary_digit_sum(m, 3 if b==0 else 4):
                if m <= (1 << N):
                    hits.append((a, b, m-1))
        high <<= 1
    return hits


def prime_list(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, isqrt(limit) + 1):
        if sieve[i]:
            sieve[i*i:limit+1:i] = b'\x00' * ((limit-i*i)//i+1)
    return [i for i in range(2, limit + 1) if sieve[i]]


def factorial_valuation(m, p):
    s = 0
    while m:
        m //= p
        s += m
    return s


def quotient_valuation(n, p):
    return n // (p-1) - factorial_valuation(n+1, p)


def independent_small_check():
    from math import factorial
    primes = prime_list(80)
    for n in range(80):
        numerator = 1
        for p in primes:
            if p <= n + 1:
                numerator *= p**(n//(p-1))
        assert numerator % factorial(n+1) == 0
        quotient = numerator//factorial(n+1)
        for p in primes:
            assert quotient_valuation(n,p) >= 0
            v=0
            while quotient and quotient % p == 0:
                quotient //= p
                v+=1
            assert quotient_valuation(n,p) == v
        assert quotient==1


def main():
    start = monotonic()
    independent_small_check()
    # Independent direct exhaustive comparison at a small bit bound.
    C = candidate_indices(12)
    brute=[]
    for n in range((1<<12)):
        m=n+1
        if m.bit_count() <= 2 and ternary_digit_sum(m) <= (3 if m%2 else 4):
            brute.append(n)
    assert sorted(n for _,_,n in C)==brute
    hits = candidate_indices(BIT_BOUND)
    assert len(hits) == 42, len(hits)
    assert max(n for _,_,n in hits) == 65663
    primes = prime_list(65664)
    survivors=[]
    failures=[]
    for a,b,n in hits:
        obstruction = next((p for p in primes if p <= n+1 and quotient_valuation(n,p) >= 2), None)
        if obstruction is None:
            survivors.append(n)
        else:
            assert quotient_valuation(n,obstruction) >= 2
            failures.append((n,obstruction))
    assert survivors == [0,1,2,3,4,5,7,8,9,11,15,17,19,23,31,32,33,35,39,47,63,65,71,95,135,143,191,255,257,263,287,515,575,767,1055]
    assert failures == [(271,7),(512,5),(513,5),(1025,7),(2303,5),(32831,5),(65663,5)]
    print('PASS: small independent valuations, small brute-force comparison')
    print('PASS: all n < 2^%d checked via necessary binary/ternary restrictions' % BIT_BOUND)
    print('eligible candidates:',len(hits),'max eligible index:',max(n for _,_,n in hits))
    print('squarefree indices:',survivors)
    print('excluded candidates and square-divisor witnesses:',failures)
    print('elapsed seconds: %.3f' % (monotonic()-start))


if __name__ == '__main__':
    main()
