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

The proof in `RESULT.md` derives the exact normalized recurrence and its limiting cap analytically.

`artifacts/verify_curvature_ceiling.py` replays the source recurrence for several admissible parameter choices and verifies numerical convergence to the closed-form limit. It also checks the sharp parameter envelope by deterministic transformed-parameter grids.

The finite replay is supporting evidence only. The convergence theorem and supremum formulas follow from the product-divergence and elementary minimization arguments in the proof.
