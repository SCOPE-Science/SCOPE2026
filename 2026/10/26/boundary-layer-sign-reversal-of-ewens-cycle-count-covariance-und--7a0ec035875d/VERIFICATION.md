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
Run `python3 verification/verify.py` with a standard Python installation. This exact-rational program checked 2,464 finite covariance formulas and specified sign examples, 12 direct full-permutation Ewens enumerations, 15 closed-form special instances, and 72 coefficient-telescope identities; every check passed. It uses no external dependencies.

The computations test exact finite formulas; the asymptotic limits and eventual sign assertions rest on the proof in `RESULT.md`. The checker does not claim exhaustive symbolic verification of all infinite parameter choices. Historical priority and independent replication have not been established.
