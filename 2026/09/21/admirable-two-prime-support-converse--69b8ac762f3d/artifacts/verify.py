#!/usr/bin/env python3
"""Exact finite checks for the two-prime-support admirable classification."""

def primes_below(n):
    sieve = bytearray(b"\x01") * n
    if n > 0:
        sieve[0] = 0
    if n > 1:
        sieve[1] = 0
    q = 2
    while q*q < n:
        if sieve[q]:
            sieve[q*q:n:q] = b"\x00" * (((n - 1 - q*q)//q) + 1)
        q += 1
    return [q for q in range(2, n) if sieve[q]]

def sigma_prime_power(p, b):
    return (p**(b+1)-1)//(p-1)

def admirable(a, p, b):
    n = (1 << a) * p**b
    sigma = ((1 << (a+1))-1) * sigma_prime_power(p,b)
    excess = sigma - 2*n
    if excess <= 0 or (excess & 1):
        return False, None
    d = excess // 2
    return (d < n and n % d == 0), d

def predicted(a, p, b):
    M = (1 << (a+1)) - 1
    if b == 1:
        # Power-of-two deleted divisor.
        for s in range(a):
            if p == M - (1 << (s+1)):
                return True
        # The isolated odd deleted divisor d=5.
        if a == 3 and p == 5:
            return True
        # Deleted divisor is an even perfect number.
        if a % 2 == 1:
            h = (a+1)//2
            if h >= 2 and p == (1 << h) - 1:
                return True
        return False
    if b == 3:
        # Mersenne-cube family.
        return p == M
    return False

def vp(n,p):
    u = 0
    while n % p == 0:
        u += 1
        n //= p
    return u

def main():
    ps = [p for p in primes_below(20000) if p != 2]
    tests = 0
    hits = []
    mismatches = []

    for a in range(1, 19):
        for p in ps:
            for b in range(1, 10):
                tests += 1
                got, d = admirable(a,p,b)
                pred = predicted(a,p,b)
                if got:
                    hits.append((a,p,b,d))
                if got != pred:
                    mismatches.append((a,p,b,d,pred))

    # A separate scan targets the proof's high-p-adic-valuation branch.
    high_valuation_candidates = 0
    high_valuation_hits = []
    for a in range(1, 301):
        M = (1 << (a+1)) - 1
        for p in ps:
            if M % p:
                continue
            u = vp(M,p)
            for b in (3,5,7,9):
                if u >= b:
                    high_valuation_candidates += 1
                    got, d = admirable(a,p,b)
                    if got:
                        high_valuation_hits.append((a,p,b,u,d))

    print("classification tuples tested:", tests)
    print("admirable hits:", len(hits))
    print("classification mismatches:", len(mismatches))
    print("high-valuation candidates tested:", high_valuation_candidates)
    print("high-valuation admirable hits:", len(high_valuation_hits))
    print("higher-power hits (b >= 3):")
    for row in hits:
        if row[2] >= 3:
            print(" ", row)
    if mismatches or high_valuation_hits:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
