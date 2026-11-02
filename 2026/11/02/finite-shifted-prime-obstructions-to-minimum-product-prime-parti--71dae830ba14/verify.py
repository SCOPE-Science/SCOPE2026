"""Independent finite checks for the finite-offset criterion for prime-set minimizers.

Run: python3 verify.py
All calculations use exact Python integers. Not a proof of the infinite theorem.
"""
from math import prod

LIMIT = 1400

def primes_to(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            for x in range(p * p, n + 1, p):
                sieve[x] = 0
    return [p for p in range(n + 1) if sieve[p]]

PRIMES = primes_to(LIMIT)
PSET = set(PRIMES)

def finite_offsets(A):
    m = prod(A)
    d = sum(A)
    offsets = set()
    def visit(start, product, total):
        if product < m and (d - total) % 2 == 0:
            offsets.add(d - total)
        for i in range(start, len(PRIMES)):
            p = PRIMES[i]
            if product * p >= m:
                break
            visit(i + 1, product * p, total + p)
    visit(0, 1, 0)
    return offsets

def minimum_prime_set_products(n):
    dp = [None] * (n + 1)
    dp[0] = 1
    for p in PRIMES:
        if p > n:
            break
        for s in range(n, p - 1, -1):
            if dp[s - p] is None:
                continue
            value = dp[s - p] * p
            if dp[s] is None or value < dp[s]:
                dp[s] = value
    return dp

def main():
    dp = minimum_prime_set_products(LIMIT)
    cases = [(2,), (3,), (3, 5), (3, 5, 19)]
    tested = 0
    for A in cases:
        d, m = sum(A), prod(A)
        assert dp[d] == m, (A, dp[d], m)
        offsets = finite_offsets(A)
        assert 0 not in offsets
        for q in PRIMES:
            if q <= d or q + d > LIMIT:
                continue
            criterion = not any(q + e in PSET for e in offsets)
            observed = dp[q + d] == q * m
            assert criterion == observed, (A, q, offsets, dp[q + d])
            tested += 1
    assert finite_offsets((2,)) == {2}
    assert finite_offsets((3,)) == set()
    assert finite_offsets((3, 5)) == {6, 8}
    def trial_prime(n):
        return n >= 2 and all(n % d for d in range(2, int(n ** 0.5) + 1))
    q = 810149
    assert trial_prime(q) and trial_prime(q + 2)
    assert not trial_prime(q + 6) and not trial_prime(q + 8)
    print(f'VERIFY_OK fixed_sets={len(cases)} exact_sum_cases={tested} even_offsets_for_3_5_19={len(finite_offsets((3,5,19)))}')

if __name__ == '__main__':
    main()
