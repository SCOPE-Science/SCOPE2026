#!/usr/bin/env python3
"""Exact finite certificate for a prime-support obstruction to a Dedekind-psi congruence.

Only Python standard-library integer arithmetic is used. The complete branch
enumeration proves finitely many rational inequalities; the unbounded
mathematical reduction is given in RESULT.md.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import isqrt

BASE = (3, 5, 7, 11, 13)
SUPPORT_CUTOFF = 709
SIEVE_LIMIT = 20_000

# Expected 709th primes are used as a second check on the exhaustive prime sieve.
EXPECTED_LAST = {
    (): 5417,
    (3,): 11959,
    (5,): 7457,
    (7,): 6619,
    (3, 7): 14731,
    (5, 7): 9103,
    (11,): 6073,
    (5, 11): 8311,
    (7, 11): 7481,
    (5, 7, 11): 10193,
    (13,): 5903,
    (3, 13): 13159,
    (5, 13): 8243,
    (11, 13): 6661,
    (5, 11, 13): 9161,
}


def prime_sieve(limit):
    prime = bytearray(b"\x01") * (limit + 1)
    prime[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if prime[p]:
            for multiple in range(p * p, limit + 1, p):
                prime[multiple] = 0
    return prime


def compatible(subset):
    return all(q % r != r - 1
               for r in subset for q in subset if q != r)


def eligible(q, subset):
    if (q in BASE) != (q in subset):
        return False
    return all(q == r or q % r != r - 1 for r in subset)


prime = prime_sieve(SIEVE_LIMIT)
odd_primes = [q for q in range(3, SIEVE_LIMIT + 1, 2) if prime[q]]
rows = []

for mask in range(1 << len(BASE)):
    subset = tuple(r for i, r in enumerate(BASE) if mask & (1 << i))
    if not compatible(subset):
        continue
    allowed = [q for q in odd_primes if eligible(q, subset)]
    assert len(allowed) > SUPPORT_CUTOFF, subset
    leading = allowed[:SUPPORT_CUTOFF]
    assert leading[-1] == EXPECTED_LAST[subset], (subset, leading[-1])
    numerator = denominator = 1
    for q in leading:
        numerator *= q + 1
        denominator *= q
    # This is an EXACT arbitrary-precision inequality, not floating point.
    assert numerator < 3 * denominator, (subset, leading[-1])
    rows.append((subset, leading[-1], numerator, denominator))

assert len(rows) == len(EXPECTED_LAST) == 15
assert {row[0] for row in rows} == set(EXPECTED_LAST)
champion = max(rows, key=lambda row: Fraction(row[2], row[3]))
assert champion[0] == (11, 13) and champion[1] == 6661

# The chosen 709-factor cutoff is the exact limit of this five-prime sieve:
# the maximum branch passes 3 at its next eligible prime.
next_eligible = [q for q in odd_primes if eligible(q, (11, 13))][SUPPORT_CUTOFF]
assert next_eligible == 6673
assert champion[2] * (next_eligible + 1) >= 3 * champion[3] * next_eligible

# Independent finite residue check, NOT an unbounded proof.
TEST_LIMIT = 100_000
smallest = list(range(TEST_LIMIT + 1))
smallest[0] = 0
smallest[1] = 1
for p in range(2, isqrt(TEST_LIMIT) + 1):
    if smallest[p] == p:
        for m in range(p*p, TEST_LIMIT + 1, p):
            if smallest[m] == m:
                smallest[m] = p

prime_examples = 0
for n in range(2, TEST_LIMIT + 1):
    m = n
    psi = 1
    distinct = 0
    sole_exponent = 0
    while m > 1:
        p = smallest[m]
        exponent = 0
        while m % p == 0:
            m //= p
            exponent += 1
        distinct += 1
        sole_exponent = exponent
        psi *= p**(exponent - 1) * (p + 1)
    is_prime_n = (distinct == 1 and sole_exponent == 1)
    assert (psi % n == 1) == is_prime_n, (n, psi)
    prime_examples += is_prime_n

with localcontext() as ctx:
    ctx.prec = 24
    ratio = Decimal(champion[2]) / Decimal(champion[3])
print(
    "VERIFY_OK",
    f"compatible_branches={len(rows)}",
    f"tested_support_cutoff={SUPPORT_CUTOFF}",
    f"maximum_subset={champion[0]}",
    f"maximum_709th_prime={champion[1]}",
    f"largest_exact_ratio_below_three={ratio}",
    f"next_prime={next_eligible}",
    f"direct_residues_through={TEST_LIMIT}",
    f"prime_hits={prime_examples}",
)
