---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and scope

Run `python3 verify.py` with Python 3 and no external packages. The checker directly enumerates the bi-unitary prime-power divisor sums (deleting the midpoint divisor for even exponents), confirms their exact factorization, and verifies the square factor condition whenever the exponent is at least four. It also checks that none of the tested ordered distinct prime pairs produces a harmonic integer, including a supplementary exponent-two boundary.

The machine output includes `VERIFY_OK distinct_prime_pairs_times_levels= 9324 formula_and_square_factor_checked_levels=1..7`. Its finite range uses primes below 160 and integer exponents one through seven on the binary exponent parameter. The proof of the general infinite statement is the exact prime-support argument in `RESULT.md`; finite enumerations alone would not suffice. Independent audit was not performed.
