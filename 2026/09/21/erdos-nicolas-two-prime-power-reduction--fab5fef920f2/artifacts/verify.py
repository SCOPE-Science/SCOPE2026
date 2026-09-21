#!/usr/bin/env python3
"""Exact checks for initial-divisor sums of n = 2^a p^b."""


def primes_upto(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for q in range(2, int(limit**0.5) + 1):
        if sieve[q]:
            sieve[q*q : limit + 1 : q] = b"\x00" * (((limit - q*q) // q) + 1)
    return [q for q in range(3, limit + 1, 2) if sieve[q]]


def factor_trial(n):
    factors = {}
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def prefix_hit(a, b, p):
    n = (1 << a) * (p**b)
    divisors = sorted((1 << i) * (p**j) for i in range(a + 1) for j in range(b + 1))
    total = 0
    for k, d in enumerate(divisors, 1):
        total += d
        if total == n:
            return k, len(divisors)
        if total > n:
            return None
    return None


def theorem_b1(a, p):
    return (a == 3 and p == 3) or p == (1 << (a + 1)) - 1


def main():
    # Direct, theorem-independent check of the complete b=1 and b=2 statements
    # on a large rectangular box.
    primes = primes_upto(100_000)
    direct_tested = 0
    direct_hits = []
    direct_mismatches = []
    for b in (1, 2):
        for a in range(1, 21):
            for p in primes:
                direct_tested += 1
                hit = prefix_hit(a, b, p)
                predicted = theorem_b1(a, p) if b == 1 else False
                if hit is not None:
                    direct_hits.append(((1 << a) * (p**b), a, b, p, hit[0], hit[1]))
                if (hit is not None) != predicted:
                    direct_mismatches.append((a, b, p, hit, predicted))

    # The structural theorem reduces every b>=3 solution with a>=4 to:
    # p | 2^(a+1)-1, b odd, and 3 <= b <= a + v_p(2^(a+1)-1) - 1.
    # Enumerate that finite set exactly for a <= 30.
    reduced_candidates = []
    reduced_hits = []
    mersenne_perfect = []
    for a in range(1, 31):
        M = (1 << (a + 1)) - 1
        fac = factor_trial(M)
        if len(fac) == 1 and next(iter(fac.values())) == 1:
            p = next(iter(fac))
            mersenne_perfect.append((a, p, (1 << a) * p))
        if a >= 4:
            for p, v in fac.items():
                if p <= (1 << a):
                    for b in range(3, a + v):
                        if b % 2 == 1:
                            row = (a, b, p, v)
                            reduced_candidates.append(row)
                            hit = prefix_hit(a, b, p)
                            if hit is not None:
                                reduced_hits.append(row + hit)

    print(f"direct b=1,2 tuples tested: {direct_tested}")
    print(f"direct hits: {len(direct_hits)}")
    for n, a, b, p, k, tau in direct_hits:
        print(f"  n={n} a={a} b={b} p={p} k={k} tau={tau}")
    print(f"direct mismatches: {len(direct_mismatches)}")
    print(f"reduced b>=3 candidates for 4<=a<=30: {len(reduced_candidates)}")
    print(f"reduced b>=3 hits: {len(reduced_hits)}")
    print("Mersenne-perfect b=1 cases for 1<=a<=30:")
    for a, p, n in mersenne_perfect:
        print(f"  a={a} p={p} n={n}")
    print("extra nonperfect case: a=3 p=3 b=1 n=24")

    if direct_mismatches or reduced_hits:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
