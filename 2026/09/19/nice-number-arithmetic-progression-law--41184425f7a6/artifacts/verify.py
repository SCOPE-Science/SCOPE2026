#!/usr/bin/env python3
"""Finite checks for the shifted-squarefree-prime constants used in the theorem."""

LIMIT = 1_000_000


def prime_sieve(n):
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[:2] = b"\x00\x00"
    r = int(n**0.5)
    for p in range(2, r + 1):
        if is_prime[p]:
            is_prime[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return is_prime


def squarefree_sieve(n, is_prime):
    sqfree = bytearray(b"\x01") * (n + 1)
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            q = p * p
            sqfree[q : n + 1 : q] = b"\x00" * (((n - q) // q) + 1)
    return sqfree


is_prime = prime_sieve(2 * LIMIT + 1)
primes = [p for p in range(2, LIMIT + 1) if is_prime[p]]
sqfree = squarefree_sieve(LIMIT, is_prime)
shifted = [p for p in primes if sqfree[p - 1]]

artin_partial = 1.0
for p in primes:
    artin_partial *= 1.0 - 1.0 / (p * (p - 1))

mod3_1 = sum(p % 3 == 1 for p in shifted)
mod3_2 = sum(p % 3 == 2 for p in shifted)
sophie = sum(2 * p + 1 <= 2 * LIMIT and is_prime[2 * p + 1] for p in primes)

print(f"prime_limit={LIMIT}")
print(f"prime_count={len(primes)}")
print(f"squarefree_predecessor_primes={len(shifted)}")
print(f"relative_density={len(shifted)/len(primes):.12f}")
print(f"partial_artin_product={artin_partial:.12f}")
print(f"p_mod_3_eq_1={mod3_1}")
print(f"p_mod_3_eq_2={mod3_2}")
print(f"mod_6_n_eq_2_proportion={mod3_1/len(shifted):.12f}")
print(f"mod_6_n_eq_4_proportion={mod3_2/len(shifted):.12f}")
print("predicted_limiting_proportions=0.400000000000,0.600000000000")
print(f"sophie_germain_primes_up_to_{LIMIT}={sophie}")
