#!/usr/bin/env python3
"""Exact checks for the divisor-partition formula for n = 2^a p."""

from collections import Counter


def odd_primes(limit: int):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for q in range(2, int(limit ** 0.5) + 1):
        if sieve[q]:
            sieve[q * q : limit + 1 : q] = b"\x00" * (((limit - q * q) // q) + 1)
    return [q for q in range(3, limit + 1, 2) if sieve[q]]


def direct_partition_count(a: int, p: int) -> int:
    divisors = [1 << i for i in range(a + 1)] + [p * (1 << i) for i in range(a + 1)]
    total = sum(divisors)
    if total & 1:
        return 0
    target = total // 2
    counts = Counter({0: 1})
    for d in divisors:
        for s, c in list(counts.items()):
            if s + d <= target:
                counts[s + d] += c
    return counts[target] // 2


def predicted_partition_count(a: int, p: int) -> int:
    M = (1 << (a + 1)) - 1
    return (M + p) // (2 * p)


def omega_sieve(limit: int):
    omega = [0] * (limit + 1)
    for p in range(2, limit + 1):
        if omega[p] == 0:
            for m in range(p, limit + 1, p):
                omega[m] += 1
    return omega


def main():
    mismatches = []
    tested = 0
    for a in range(1, 8):
        for p in odd_primes(199):
            tested += 1
            got = direct_partition_count(a, p)
            want = predicted_partition_count(a, p)
            if got != want:
                mismatches.append((a, p, got, want))

    print(f"direct parameter pairs checked: {tested}")
    print(f"direct-count mismatches: {len(mismatches)}")
    if mismatches:
        for row in mismatches[:20]:
            print("mismatch", row)
        raise SystemExit(1)

    for a, p in [(1, 3), (2, 5), (3, 3), (3, 5), (4, 3), (5, 7)]:
        print(f"A083206(2^{a}*{p}) = {direct_partition_count(a, p)}")

    # Exact aggregate identity: sum_p A083206(2^a p)
    # equals sum_{odd m <= M} omega(m), where M = 2^(a+1)-1.
    Mmax = (1 << 18) - 1
    primes = odd_primes(Mmax)
    omega = omega_sieve(Mmax)
    aggregate_mismatches = []
    for a in range(1, 18):
        M = (1 << (a + 1)) - 1
        lhs = sum(predicted_partition_count(a, p) for p in primes if p <= M)
        rhs = sum(omega[m] for m in range(1, M + 1, 2))
        if lhs != rhs:
            aggregate_mismatches.append((a, lhs, rhs))
    print(f"aggregate identities checked: 17")
    print(f"aggregate mismatches: {len(aggregate_mismatches)}")
    if aggregate_mismatches:
        for row in aggregate_mismatches:
            print("aggregate mismatch", row)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
