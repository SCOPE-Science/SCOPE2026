#!/usr/bin/env python3
"""Exact bounded verification for the even two-prime k-deficient-perfect criterion.

No third-party packages are required.
"""

from collections import Counter


def primes_below(limit):
    sieve = bytearray(b"\x01") * limit
    if limit > 0:
        sieve[0] = 0
    if limit > 1:
        sieve[1] = 0
    for q in range(2, int(limit**0.5) + 1):
        if sieve[q]:
            sieve[q*q:limit:q] = b"\x00" * (((limit - 1 - q*q) // q) + 1)
    return [q for q in range(2, limit) if sieve[q]]


def theorem_k(a, b, p):
    M = (1 << (a + 1)) - 1
    if not (M < p < 2 * M):
        return None
    t = p - M
    return t.bit_count() + (b - 1) * (t - 1).bit_count()


def sigma_2apb(a, b, p):
    return ((1 << (a + 1)) - 1) * ((p ** (b + 1) - 1) // (p - 1))


def brute_cardinality_counts(a, b, p):
    n = (1 << a) * (p ** b)
    delta = 2 * n - sigma_2apb(a, b, p)
    if delta <= 0:
        return {}

    divisors = []
    for j in range(b + 1):
        pj = p ** j
        for i in range(a + 1):
            d = (1 << i) * pj
            if d < n and d <= delta:
                divisors.append(d)

    # dp[s][r] is the number of subsets of r distinct proper divisors
    # summing to s, capped at 2 because only uniqueness vs. non-uniqueness matters.
    dp = {0: {0: 1}}
    for d in divisors:
        new = {s: dict(counts) for s, counts in dp.items()}
        for s, counts in dp.items():
            ns = s + d
            if ns > delta:
                continue
            target = new.setdefault(ns, {})
            for r, count in counts.items():
                target[r + 1] = min(2, target.get(r + 1, 0) + count)
        dp = new
    return dp.get(delta, {})


def main():
    tests = 0
    positives = 0
    distribution = Counter()
    mismatches = []

    for a in range(1, 7):
        for b in range(1, 5):
            for p in primes_below(200):
                if p == 2:
                    continue
                n = (1 << a) * (p ** b)
                if n > 2_000_000:
                    continue

                tests += 1
                predicted = theorem_k(a, b, p)
                counts = brute_cardinality_counts(a, b, p)
                actual_cardinalities = set(counts)

                if predicted is None:
                    if actual_cardinalities:
                        mismatches.append((a, b, p, predicted, counts))
                else:
                    # The theorem predicts one representation, of one cardinality.
                    if actual_cardinalities != {predicted} or counts[predicted] != 1:
                        mismatches.append((a, b, p, predicted, counts))
                    else:
                        positives += 1
                        distribution[predicted] += 1

    print(f"tested tuples: {tests}")
    print(f"qualifying tuples: {positives}")
    print("cardinality distribution:",
          " ".join(f"k={k}:{distribution[k]}" for k in sorted(distribution)))
    print(f"mismatches: {len(mismatches)}")
    if mismatches:
        for row in mismatches[:20]:
            print("  ", row)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
