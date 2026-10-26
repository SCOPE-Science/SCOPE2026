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

The exact root-splitting recurrence in `RESULT.md` is implemented in `verify.py` with complete enumeration of query labels, integer-bitset version spaces, and memoization. The direct certificate `witness.json` supplies all depth-seven path realizers. The complete run output is in `CHECKS.txt`; rerun `python3 verify.py` and `python3 verify_secondary.py` to inspect the actual computations.

Scope: all seven first-occurrence bounds, a depth-eight exclusion at the specified finite value, and all 128 explicit witness paths. No infinite-height statement, external independent certification, or exhaustive historical-priority claim is made.
