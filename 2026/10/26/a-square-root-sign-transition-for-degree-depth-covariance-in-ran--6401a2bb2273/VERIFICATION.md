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

The exact rational checker `verify_cov_profile.py` was executed using Python 3 and reported `PASS exact assertions 4791 including independent exhaustive parent-array enumerations through n=9`. It independently enumerates parent arrays through nine vertices, computes mixed moments from first principles, and compares them to the claimed formula. Additional rational checks confirm positive adjacent differences and endpoint signs for a finite parameter range; floating checks of the square-root threshold are illustrative only.

The proof of the all-size statement is the ancestor-event factorization and partial summation in RESULT.md. The asymptotic statements use the stated inverse-square tail expansion. Computation is not a proof beyond enumerated sizes. No external independent audit has been performed.
