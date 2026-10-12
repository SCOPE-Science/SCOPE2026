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

The proof is analytic. The standalone checker evaluates the diagonal one-observation functions
\[
q_W(u)=u^2-u+\frac13
\]
and
\[
q_A(u)=-1-\log(u(1-u))
\]
by numerical quadrature and verifies their means, variances, and covariance against the closed constants.

It separately evaluates the three squared Brownian-bridge kernel integrals over the triangle \(0<s<t<1\), doubles them by symmetry, and compares with
\[
\frac1{90},\qquad
\frac1{18},\qquad
\frac{\pi^2}{3}-3.
\]

The checker then reconstructs the exact finite-sample covariance and both variances from the Hoeffding decomposition for \(1\le n\le100\), checks the resulting correlations are valid, and verifies the limiting correlation numerically.

The numerical calculations are supplementary. The identities for arbitrary \(n\) follow from the exact decomposition and elementary integrals in `RESULT.md`.

Independent audit has not been performed.

Deterministic replay result: `VERIFY_OK integral_checks=8 finite_formula_checks=400 limit=0.9789229548736679`.
