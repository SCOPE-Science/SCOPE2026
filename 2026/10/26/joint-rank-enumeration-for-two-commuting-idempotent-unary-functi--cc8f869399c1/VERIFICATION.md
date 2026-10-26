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

The included `checker.py` implements the exact rooted-fiber coefficient formula, the distinguished-label recurrence, and a separate brute-force loop over all ordered idempotent endofunction pairs for every domain size from one through five. The checker tests equality of **the entire joint coefficient dictionary** indexed by common fixed points, first-function fixed points, and second-function fixed points, not merely equality of total counts. It reports `FULL_PROFILE_CHECK_OK` and computes totals through size ten.

The all-size identity is proved combinatorially in `RESULT.md` by a bijection, without extrapolation from a finite census. The computational cross-check is an ordinary proof consistency test, not an independent mathematical audit. The general action-enumeration literature was not exhaustively surveyed; originality has a documented residual coverage risk.
