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

The exact domain is a uniform Dirichlet spacing vector with \(m\ge2\).

The critical proof steps are the affine conditional law under \(M_m>t\), the majorization monotonicity of \(\sum_iD_i^a\), the survival-integral identity for covariance, and exact Beta/Dirichlet moments for integer powers.

`checker.py` performs exact rational checks for the integer covariance formula, the Greenwood covariance and correlation, the minimum and power-sum variances, and the threshold-conditioned Greenwood identity over broad finite ranges. It also evaluates \(\mathbb E[M_mP_{m,q}]\) by direct low-dimensional simplex integration for \(m=2\) and \(m=3\) and matches the general formula.

The sign theorem for noninteger powers is analytic and uses strict Schur convexity or concavity; no finite experiment is used as a substitute for that proof.
