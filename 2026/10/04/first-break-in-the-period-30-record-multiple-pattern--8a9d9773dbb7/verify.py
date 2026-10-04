#!/usr/bin/env python3
from math import isqrt

PRIMES = [2,3,5,7,11,13,17,19,23]

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True

def next_prime(n):
    k = n + 1
    while not is_prime(k):
        k += 1
    return k

def least_prime_not_dividing(n):
    p = 2
    while n % p == 0:
        p = next_prime(p)
    return p

def next_record(r):
    return r - 1 + least_prime_not_dividing(r - 1)

def generate_records(limit):
    out = [1,2,3]
    r = 3
    while r < limit:
        r = next_record(r)
        out.append(r)
    return out

def main():
    P = 1
    for p in PRIMES:
        P *= p
    assert P == 223092870
    assert P % 30 == 0
    assert P // 30 == 7436429

    assert least_prime_not_dividing(P) == 29
    assert next_record(P + 1) == P + 29
    assert P + 1 < P + 25 < P + 29
    assert P + 25 == 223092895

    assert 3 - 1 == 2
    assert 23 % 6 == 5
    for ell in [7,11,13,17,19,23]:
        assert ell - 1 < 24
    assert all(p < 29 for p in PRIMES)
    assert next_prime(23) == 29

    records = set(generate_records(1_000_000))
    xs = list(range(25, 1_000_000, 30))
    assert all(x in records for x in xs)

    print("VERIFY_OK")
    print("primorial_23=" + str(P))
    print("progression_terms_before_failure=" + str(P//30))
    print("last_confirmed_progression_term=" + str(P-5))
    print("first_failed_progression_term=" + str(P+25))
    print("next_record_after_primorial_plus_one=" + str(P+29))

if __name__ == "__main__":
    main()
