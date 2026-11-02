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

# Reproducibility
Execute `python3 verify_restricted_cubic.py` using Python 3 with no third-party dependencies. The verifier constructs finite-field operations independently (prime fields and quadratic quotient fields), exhausts all ordered triples and all target fibers, checks the quadratic-character and collision-count formula for every target, then verifies the exact missing-target sets for all six smaller fields. Execution completed with `VERIFY_OK distinct_and_unrestricted_fibers= 6371 fields=11` and PASS lines for field orders 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 49.

The finite computation proves the small-field exceptions by exhaustive enumeration. It does **not** establish the infinite claim; that follows from the character-sum identity, repeated-root classification, Hasse's bound, and the uniform at-most-nine collision correction in RESULT.md. The verifier is ordinary reproducibility code; neither a formal proof assistant nor an external independent certification was used. No independent audit has been performed.
