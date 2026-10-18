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

Exact-rational validation: `python3 verify.py` reproduces all three classes, coefficients, thresholds, and signed first derivatives. The program checks the transient-chain matrix residuals in exact fractions and uses no simulation or rounding. Its conclusion concerns the finite model and weak-selection limit only.
