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

The proof is analytic and uses only differentiated Dirichlet gamma moments.

The accompanying checker independently evaluates the same moments through digamma and trigamma formulas for a grid of dimensions. It verifies the mixed moment, covariance, Greenwood variance, entropy variance, and exact correlation.

It also evaluates the correlation at increasing dimensions and confirms convergence to
\[
-\frac1{2\sqrt{\pi^2/3-3}}.
\]

Finite numerical replay is supplementary. The all-\(m\) theorem follows from the symbolic moment identities in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK dimensions=200 identity_checks=800 asymptotic_checks=7 limit=-0.92868785736691`.
