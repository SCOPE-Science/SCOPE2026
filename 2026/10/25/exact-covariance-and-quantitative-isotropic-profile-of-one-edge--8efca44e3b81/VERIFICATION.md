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

Analytic verification: resolve coordinates into their mean and zero-sum component, integrate the conditional uniform-interval second moment against the Dirichlet gap simplex, and reconstruct the covariance eigenvalues and the determinant. Both forms of the covariance agree algebraically after the factorization \(1+(d+2)t+3dt^2+d^2t^3=(1+dt)(1+2t+dt^2)\). The rational derivative factorization and the curvature at \(t=1\) are checked symbolically.

Numerical verification: `verify.py` independently triangulates the complete polytope boundary with the origin as interior apex for dimensions 2–4 and weights 1/4, 1, 3. The checks compare polytope volumes and raw integrated covariance matrices, not merely evaluated closed formulas. The proof, not the finite test set, covers all integers \(d\ge2\) and real \(t\ge0\).

Independent validation has not been performed. The previously established uniqueness of the isotropic minimizer is credited to Kipp and is not offered as new.
