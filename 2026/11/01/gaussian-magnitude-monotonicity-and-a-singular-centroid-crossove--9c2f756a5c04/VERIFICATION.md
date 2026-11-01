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

The critical claims are established analytically in RESULT.md: the negative-type threshold by an exact zero-sum quadratic-form decomposition; positive definiteness by the two-block kernel spectrum and strict weighted arithmetic–geometric mean inequality; monotonicity by the derivative-sign reduction to a one-variable function with strictly negative third derivative at the critical parameter; and the small-scale laws by explicit Taylor expansions.

Run `python3 verify.py` in the directory containing this document. The checker is self-contained and uses the Python standard library. It compares exact finite-dimensional Gaussian elimination with the claimed kernel-magnitude expression for rational cases, including positive-type boundary cases. It tests high-precision derivative positivity on a finite parameter grid and the critical derivative factor. The recorded complete run passed 5,273 assertions.

These computations are **diagnostics**, not a proof by exhaustive computation. No independent review has been performed. The references and statement-comparison limitations in RESULT.md remain applicable.
