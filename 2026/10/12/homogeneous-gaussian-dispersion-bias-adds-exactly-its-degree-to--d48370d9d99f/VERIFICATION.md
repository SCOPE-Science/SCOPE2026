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

The proof is analytic and rests on the exact polar decomposition of the centered Gaussian residual vector.

The accompanying checker verifies two algebraic consequences over a grid of dimensions and homogeneity degrees.

For integer even degree shifts it compares normalized even moments of the radially tilted \(\chi_d\) law against the moment sequence of \(\chi_{d+q}\).

For integer and noninteger shifts it evaluates gamma-ratio moments and verifies the covariance consequence
\[
\operatorname{Cov}(T,S^2)
=
\frac{q\sigma^2}{d}\mathbb ET
\]
at the radial-factor level.

It also checks the degree-one specialization corresponding to the sample range and Gini mean difference.

These computations are supplementary. The universal statement for arbitrary admissible \(h\) is proved by the exact factorization
\[
T=\sigma^qR^qh(U)
\]
with independent \(R\) and \(U\).

Independent audit has not been performed.

Exact replay result: `VERIFY_OK exact_integer_moment_checks=700 gamma_moment_checks=560 covariance_checks=140 degree_one_checks=20`.
