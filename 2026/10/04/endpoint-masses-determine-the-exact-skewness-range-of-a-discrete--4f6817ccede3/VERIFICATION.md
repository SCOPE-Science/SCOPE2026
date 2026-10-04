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

The proof is analytic. The accompanying checker uses exact rational arithmetic
where the square roots can be eliminated.

For random rational profiles and strictly increasing rational supports it
computes the central second and third moments exactly. The comparisons with
the endpoint constants are performed by sign-aware cross multiplication after
squaring, so no floating-point decision is used for the inequalities.

The checker also constructs explicit sequences in which all but the first atom
collapse, and all but the last atom collapse, and confirms convergence toward
the two predicted boundary skewnesses.

For two-point laws it verifies the exact Bernoulli skewness formula.

Finally, for small rational examples it enumerates iid samples and checks
\[
\operatorname{Cov}(\bar X,S^2)
=
\frac{\mu_3}{n}.
\]

Finite replay does not replace the compact-stratum and Lagrange proof.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK bound_checks=60000 boundary_checks=60000 two_point_checks=4950 covariance_checks=9 sign_checks=30000`.
