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

The proof is analytic. The accompanying checker uses exact rational arithmetic for integer sample sizes and positive integer powers.

It independently reconstructs the mean normalized variance from two fixed endpoints and \(n-2\) iid uniform interior observations.

It checks the beta range moment formula, evaluates the unsimplified covariance
\[
\mathbb EQ\left(\mathbb E[R^{q+2}]-\mathbb E[R^q]\mathbb E[R^2]\right),
\]
and verifies equality with the closed expression in `RESULT.md` over a large grid of \((n,q)\).

It also verifies the special simplification
\[
\operatorname{Cov}(R,S^2)=\frac1{3(n+1)(n+3)}
\]
on the unit interval.

The finite replay is supplementary. The independence statement and all-real-\(q>0\) theorem are proved by the transformed joint density and beta-moment algebra.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK normalized_mean_checks=399 range_moment_checks=6783 covariance_identity_checks=7980 positivity_checks=7980 q1_checks=399`.
