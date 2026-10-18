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

# Reproducibility

Run `python verification/check.py` with SymPy installed in a Python 3 environment. The script independently checks the three stationary moment equations, covariance solution, decomposition into continuous and reset-chord signed-area rates, equal-temperature ratio, and weak/rapid-reset limits as exact rational or symbolic identities. It also solves the stationary linear system independently for 120 deterministic rational parameter choices and compares the result exactly to the closed formulas. Expected output contains two `PASS` lines.

The symbolic identity checks verify the algebraic portion of the proof. The separate contraction argument in RESULT.md establishes existence and uniqueness of the stationary regime, while elementary sign analysis provides the global zero-count classification. The 120 finite checks are corroboration, not an infinite-parameter certificate or independent audit. No full-distribution identity or experimental result is asserted.
