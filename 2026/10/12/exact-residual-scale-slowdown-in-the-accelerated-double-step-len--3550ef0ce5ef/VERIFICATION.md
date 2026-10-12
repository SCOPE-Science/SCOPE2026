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

The proof is exact algebra on the scalar family \(F_a(s)=a s\). The source secant update is evaluated symbolically, and the source line-search inequality is reduced to a quadratic inequality in the trial step.

The bundled verifier checks four points independently: exact secant recovery of \(a\); equivalence of the original line-search inequality with the derived quadratic test over randomized positive parameters; finite stabilization of the geometric backtracking index for a positive summable sequence; and the predicted \(a^2\) contraction-gap and logarithmic backtracking scaling over decreasing residual scales.

Finite numerical checks do not prove the quantified asymptotic statements. Those follow from the explicit formulas and inequalities in `RESULT.md`. No claim is made about multidimensional worst-case complexity or about failure of the source convergence theorem.
