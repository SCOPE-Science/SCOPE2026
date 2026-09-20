#!/usr/bin/env python3
"""Exact bounded checks for the ordered-prime Novák criterion."""
import sympy as sp

LIMIT_N = 1_000_000
PRIME_LIMIT = 200_000
MAX_A = 8
MAX_B = 3


def prefix_criterion(n):
    if n == 1:
        return True
    fac = list(sp.factorint(n).items())
    if not fac or fac[0][0] != 3:
        return False
    prefix = 3 ** fac[0][1]
    for p, a in fac[1:]:
        if pow(2, prefix, p) != p - 1:
            return False
        prefix *= p ** a
    return True


def main():
    direct_count = 0
    criterion_count = 0
    mismatches = []
    for n in range(1, LIMIT_N + 1, 2):
        direct = pow(2, n, n) == (n - 1) % n
        predicted = prefix_criterion(n)
        direct_count += int(direct)
        criterion_count += int(predicted)
        if direct != predicted:
            mismatches.append((n, direct, predicted))

    triple_tests = 0
    direct_hits = 0
    predicted_hits = 0
    two_prime_mismatches = []
    first_level = {}
    for q in sp.primerange(5, PRIME_LIMIT):
        for a in range(1, MAX_A + 1):
            predicted_base = pow(2, 3 ** a, q) == q - 1
            if predicted_base and q not in first_level:
                first_level[q] = a
            for b in range(1, MAX_B + 1):
                triple_tests += 1
                n = (3 ** a) * (q ** b)
                direct = pow(2, n, n) == n - 1
                direct_hits += int(direct)
                predicted_hits += int(predicted_base)
                if direct != predicted_base:
                    two_prime_mismatches.append((a, q, b, direct, predicted_base))

    print(f"odd n <= {LIMIT_N}: direct Novák count = {direct_count}")
    print(f"odd n <= {LIMIT_N}: prefix-criterion count = {criterion_count}")
    print(f"prefix-criterion mismatches = {len(mismatches)}")
    print(f"two-prime triples tested = {triple_tests}")
    print(f"two-prime direct hits = {direct_hits}")
    print(f"two-prime predicted hits = {predicted_hits}")
    print(f"two-prime mismatches = {len(two_prime_mismatches)}")
    print("first appearance levels for q < 200000:")
    print(sorted((a, q) for q, a in first_level.items()))

    assert not mismatches
    assert not two_prime_mismatches


if __name__ == "__main__":
    main()
