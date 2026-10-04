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
`verify.py` is a standalone deterministic replay for the formulas in `RESULT.md`.

It checks:

1. the identity \(|u+v|-|u-v|=2\,\operatorname{sgn}(uv)\min(|u|,|v|)\) on a finite rational grid;
2. strict negativity of the analytic derivative \(F_\lambda'(\rho)\) on a broad deterministic grid with \(\lambda>0\) and \(0<\rho<1\);
3. the displayed formula for \(F_\lambda''(0)\) against a centered finite-difference calculation;
4. deterministic Simpson quadrature for \(\Pi_d(\lambda)\), reproducing the reported values for \((\lambda,d)=(1,3),(1,10),(2,3)\);
5. convergence of \(d[F_\lambda(0)-\Pi_d(\lambda)]\) toward the analytic coefficient \(A(\lambda)\) at a larger residual dimension.

A successful run prints `VERIFY_OK`.

The finite grid and numerical quadrature are checks, not proofs of the infinite statements. Strict monotonicity is proved analytically in `RESULT.md`. The sphere-coordinate density and exact moments are used for the asymptotic expansion; the verifier does not establish global FDR control, cross-feature behavior, or validity of any modified perturbation rule.
