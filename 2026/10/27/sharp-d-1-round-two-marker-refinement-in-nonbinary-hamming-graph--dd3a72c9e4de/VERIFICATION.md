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

Run `python verify.py` using Python 3 standard library. The script performs direct full-vertex synchronous one-dimensional color refinement and also independently forms the weighted orbit-quotient transitions. The first method verifies orbit labels, exact class-size formulas and strict round thresholds in 46 configurations; the second verifies transitions and thresholds in 630 configurations. Both have completed and returned `ALL_CHECKS_PASS`.

The all-dimensional and all-alphabet assertions follow from the mathematical proof in RESULT.md, not from these finite tests. No external verification, formal proof assistant, or independent audit was performed.
