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

# Verification

The mathematical proof checks the closed Jacobi formulas at degrees one, two and three, their critical-point ordering, the positivity of every cross-multiplied denominator, a factor identity for the singular boundary, uniqueness of the cubic zero, and the strict rational certificate. `verify.py` verifies all exact polynomial and rational identities using SymPy and separately checks a finite grid of ordinary Jacobi polynomial values; the finite samples are supplementary.

No independent mathematical audit has been performed. The proof does not assert the maximal full-degree parameter range and does not extend to the excluded boundary parameter.
