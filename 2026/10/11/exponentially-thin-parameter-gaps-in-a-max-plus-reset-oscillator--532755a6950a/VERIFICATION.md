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

# Reproducible checks

The analytical proof is contained in `RESULT.md`. The supplementary `tools/check_gap.py` requires Python with SymPy and mpmath. Run `python tools/check_gap.py` within the extracted package. It verifies the positive-branch trigonometric formula against the direct affine recurrence at three rational parameter values, then numerically finds the adjacent roots for \(n\in\{7,8,9,10,12,15,18,24\}\) at 85-digit working precision. It checks the root equations, root ordering, positivity of all preceding positive-branch coordinates, and relative accuracy of the predicted leading gap. A successful run terminates with `RESET_GAP_CHECK_OK`.

These tests cover finitely many \(n\) and do not establish the uniform asymptotic, unique-root existence for all large \(n\), or historical originality. Those claims rely on the separate analytic argument and literature comparison. Independent audit has not been performed.
