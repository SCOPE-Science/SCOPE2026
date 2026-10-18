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

# Exact reproducibility and scope

Run `python3 verify_reversal_local.py` with standard Python 3 (no external packages). A successful run prints the sentinel `REVERSAL_LOCAL_EXACT_REGRESSION_OK`, followed by the counts of ten exact divisibility comparisons, twelve subgroup-image comparisons, and four modular-dynamic-program convergence checks. The verifier has no external files or network dependencies.

The ten direct tests enumerate all integers of the stated exact digit lengths and compare the rational proportion divisible by the same prime power in the integer and its digit reversal against the formula for primes dividing the base. The subgroup tests enumerate the image of the two vectors that occur in the proof over twelve prime-power moduli. The independent modular recurrence uses integer counts and rational probabilities to check four prime-power convergence instances. The exact finite tests do not certify the universal quantifiers, the infinite mixing limit, or novelty; these are addressed by the analytical proof and the separate literature comparison.

The formula gives fixed-prime-power local information only. No global gcd distribution, estimate uniform in the modulus, or independence of different prime factors is established. Independent audit remains unperformed.
