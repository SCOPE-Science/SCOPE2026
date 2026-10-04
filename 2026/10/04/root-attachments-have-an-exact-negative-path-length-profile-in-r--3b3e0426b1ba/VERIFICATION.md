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

The proof is analytic. The accompanying checker uses exact integer and rational arithmetic.

It exhaustively enumerates every recursive tree through order \(9\) from its independent parent sequence. For every admissible arrival index \(j\), it verifies the local covariance
\[
-\frac{n(H_{j-1}-1)}{j(j-1)},
\]
the conditional mean gap, and strict first-order stochastic ordering of
\[
T_n\mid(A_j=1)
\quad\text{and}\quad
T_n\mid(A_j=0).
\]

For each enumerated order it also verifies the total covariance, root-degree mean and variance, and total-path-length mean.

A separate exact-rational loop verifies the harmonic telescoping identity over hundreds of orders.

The asymptotic correlation is not inferred from finite computation. It follows from the exact covariance and root-degree variance together with the classical \(L^2\) total-path-length limit stated in the cited primary literature.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK trees_enumerated=46233 local_cov_checks=36 conditional_mean_checks=28 stochastic_cdf_checks=490 global_cov_checks=8 marginal_moment_checks=24 telescoping_checks=499`.
