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

# Verification details

The companion matrix is \(B=\begin{pmatrix}ap&a(1-p)\\1&0\end{pmatrix}\). The critical symbolic steps are the strict Schur inequalities, the Yule--Walker elimination, the factorized derivative, and the limit \((a+3)^2\operatorname{Var}_*/\sigma^2\to4\). All hold for the full parameter ranges by algebra; sampling does not constitute proof.

The standalone `verify.py` ran successfully on the actual package contents, reporting `VERIFY_OK exact_stationary_cases=2658 lyapunov_cases=801 optimality_grids=997`. Its exact-rational checks cover covariance recurrences and matrix-root stability over rational grids; independent Lyapunov solves test stochastic covariance normalization; optimizer grids test sharpness without replacing the derivative proof. No formal proof assistant, third-party certification, or independent audit has been performed. Assumptions of scalar coefficients, convex nonnegative weights, and fresh independent innovations are necessary to interpret the result as stated.
