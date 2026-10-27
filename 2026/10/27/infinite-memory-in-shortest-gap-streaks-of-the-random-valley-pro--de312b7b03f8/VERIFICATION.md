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

# Verification of the valley-gap streak theorem

`verify_valley_streak.py` is a Python 3 standard-library program. Running `python verify_valley_streak.py` generates `verification_output.txt` contents. The program independently enumerates strict alternating orderings through nine sites, computes higher Euler numbers from a separate exact integer recurrence, and uses rational fractions to check finite streak probabilities and strict inequalities. It computes the comparison limit to 100-digit precision using Machin's arctangent identity rather than machine-precision rounding.

The recorded run passed 108 assertions. This is a finite diagnostic only. The analytical ingredients needed for every streak length are the elementary bijection between successive minimum gaps and alternating permutations, the classical tangent generating function and cosine product, strict Cauchy–Schwarz for \(S_s\), and the stationary Markov contradiction. Historical priority and independent correctness validation have not been externally certified.
