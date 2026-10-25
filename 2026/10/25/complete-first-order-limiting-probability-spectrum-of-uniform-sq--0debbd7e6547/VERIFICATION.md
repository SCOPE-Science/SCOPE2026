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

Run `python3 square_permutation_check.py` using Python 3 standard library. The program independently enumerates permutations through size eight and checks the parity criterion against exact rational generating-function coefficients for four events at each size. Observed output: `SQUARE_PERM_EXACT_OK 8 16517 4x8_coeff_checks 14280`. Reproduction is finite; no statement about asymptotic convergence, locality or novelty follows from the checker alone. Infinite claims rely on the mathematical proof in RESULT.md.
