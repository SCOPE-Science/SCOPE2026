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
The algebraic verification is contained in `verify.py`. It reconstructs the exact normalized two-patch equilibrium equations from the displayed model, substitutes the analytic branch ansatz, and checks the coefficients of the first two powers of the asymmetry parameter. It then verifies the host-prevalence curvature, the vector-prevalence curvature, and the factorization that produces the unique transition polynomial.

The proof uses the implicit-function theorem at the balanced endemic equilibrium. Its Jacobian has two strictly negative eigenvalues for every \(V>1\) and \(q>0\), so the analytic expansion is justified. Patch-exchange symmetry makes both global prevalences even functions of the asymmetry parameter. Numerical finite differences in the checker are only supplementary sanity checks; they are not used to infer the infinite statement.

The result does not cover the threshold \(V=1\), arbitrary large asymmetry, or the sign of the quartic term when the quadratic host coefficient vanishes.
