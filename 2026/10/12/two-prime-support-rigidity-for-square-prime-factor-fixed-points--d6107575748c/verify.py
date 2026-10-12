#!/usr/bin/env python3
from math import isqrt

PRIME_LIMIT = 300
EXP_LIMIT = 14

def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n-p*p)//p)+1)
    return [i for i in range(2, n+1) if sieve[i]]

def t2_factorization(f):
    return sum(e*p*p for p,e in f.items())

def main():
    ps = primes_upto(PRIME_LIMIT)
    fixed = set()
    prime_power_cases = 0
    two_support_cases = 0

    for p in ps:
        for a in range(1, EXP_LIMIT + 1):
            n = p ** a
            prime_power_cases += 1
            if t2_factorization({p:a}) == n:
                fixed.add(n)

    for i,p in enumerate(ps):
        for q in ps[i+1:]:
            for a in range(1, 8):
                for b in range(1, 8):
                    n = (p ** a) * (q ** b)
                    two_support_cases += 1
                    if a*p*p + b*q*q == n:
                        fixed.add(n)

    assert fixed == {16,27}, fixed

    # Regression for the inequalities used in the proof.
    inequality_checks = 0
    for A in range(2, 60):
        assert 3 ** (2*A - 1) > 4*A
        inequality_checks += 1
    for C in range(1, 30):
        for D in range(1, 30):
            assert 3 ** (16*C + 7*D) > 2*C + D
            inequality_checks += 1
    for C in range(1, 30):
        for B in range(1, 30):
            assert 2 ** (8*C) * 3 ** (2*B - 2) > 2*C + B
            inequality_checks += 1

    print("VERIFY_OK")
    print("prime_limit=" + str(PRIME_LIMIT))
    print("prime_power_cases=" + str(prime_power_cases))
    print("two_support_cases=" + str(two_support_cases))
    print("inequality_checks=" + str(inequality_checks))
    print("fixed_points=" + ",".join(map(str, sorted(fixed))))

if __name__ == "__main__":
    main()
