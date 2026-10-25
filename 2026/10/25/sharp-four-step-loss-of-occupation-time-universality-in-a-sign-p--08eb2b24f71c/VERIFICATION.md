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

# Reproducible finite consistency checks

Running `python3 verify.py` using only Python standard-library modules produced `EXACT_RATIONAL_CHECKS_OK 686`. The script checks the eight sign-word probability aggregation, normalization, special persistence values, two magnitude-law witnesses and short-horizon laws with exact fractions. The proof in RESULT.md, not the finite checks, establishes the universal distribution formulas and the sharp parameter range. No independent audit has been performed.
