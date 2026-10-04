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

The proof reduces fixed-step aPRG on \(F(x)=ax\), \(g(x)=\mu x^2/2\) to a two-step scalar recurrence. The exact Jury conditions are then necessary and sufficient for asymptotic stability.

`artifacts/verify_aprg_scalar_split.py` checks the recurrence coefficients, exact Jury simplifications, finite stability boundary, the rate optimum for several rational split ratios, representative characteristic-root moduli on both sides of the optimum, and the large-step limit for strong proximal curvature.

The finite script is a consistency check. The all-parameter statements follow from the algebraic Jury and derivative calculations in `RESULT.md`. Noncommuting multidimensional splits, adaptive steps, stochastic errors, and finite-precision effects are outside the claim.
