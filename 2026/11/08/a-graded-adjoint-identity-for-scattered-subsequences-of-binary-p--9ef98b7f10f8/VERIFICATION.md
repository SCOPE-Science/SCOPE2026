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

# Reproducibility and limits

Run `python3 verify_graded.py` with the Python standard library. A successful run prints `VERIFY_OK` and the checked counts. The checker independently constructs the complete distinct-subsequence length profile from full hosts, compares all coefficients of the two quadratic formulas for binary half-words through length 12, and checks 381 cases by explicit set enumeration. The analytical proof, rather than these finite cases, covers unbounded lengths. A separate, external validation has not been performed.
