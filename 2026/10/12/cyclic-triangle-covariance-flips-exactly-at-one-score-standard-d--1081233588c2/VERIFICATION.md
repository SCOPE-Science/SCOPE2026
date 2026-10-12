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

The proof is analytic. The accompanying checker performs exact exhaustive replay for every tournament orientation on \(3\le n\le6\).

It computes outdegrees and cyclic triangles directly from oriented triples. It does not use the classical score-sequence identity to construct \(C_n\).

For every score class it verifies the conditional mean, exact covariance, both marginal variances, the sign transition, and the squared correlation formula. It also verifies the master additive-score identity for several nonlinear functions.

The asymptotic profile is not inferred from enumeration. It follows from the exact correlation formula and the fair-binomial local central limit theorem.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK tournaments=33864 conditional_checks=18 covariance_checks=18 variance_checks=22 sign_checks=18 master_checks=12`.
