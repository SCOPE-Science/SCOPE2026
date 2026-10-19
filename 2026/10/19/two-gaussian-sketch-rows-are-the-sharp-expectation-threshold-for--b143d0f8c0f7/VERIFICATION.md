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

The standalone `artifacts/verify.py` performs exact-fraction tests of the two-row orthogonal pivot formula, randomized positive-definite Gram-matrix inequalities, Gaussian probe simulations checked against the exact symmetric-beta CDF, and sketch-dimension tail monotonicity comparisons. Its source and output are included in the package. `artifacts/requirements.txt` records the two numerical Python dependencies.

Exact-rational assertions: 900. Random Gram-matrix assertions: 24000. Independent Gaussian probe pairs: 2000000. Analytic sketch-dimension assertions: 72. Total reported assertions: 24981. Execution completed with PASS.

Mathematical proof, not finite simulation, establishes universal bounds, infinite families and sharp limiting ratios. Floating-point simulations have nonzero tolerances and are checks only. No independent audit or external formal certification has been performed.
