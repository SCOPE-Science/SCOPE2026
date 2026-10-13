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

The proof in `RESULT.md` is analytic and valid for every integer \(n\ge1\) under the stated atomless symmetry and finite-variance assumptions.

The standalone checker performs exact finite combinatorial checks of the two identities that carry the proof.

For the Walsh representation it assigns distinct deterministic absolute magnitudes, exhausts all sign patterns, and verifies
\[
\sum_i R_i\mathbf1\{X_i>0\}
=
\sum_{i\le j}\mathbf1\{X_i+X_j>0\}.
\]
This is done through sample size \(12\).

For the signed-rank null moments it exhausts all \(2^n\) sign patterns and computes exact rational means and variances through sample size \(14\), requiring agreement with
\[
\frac{n(n+1)}4
\]
and
\[
\frac{n(n+1)(2n+1)}{24}.
\]

For an independent route to the covariance, the checker uses the centered uniform parent. If \(A_i=|X_i|\sim\operatorname{Unif}[0,a]\), then
\[
\mathbb E A_{(r)}=\frac{ar}{n+1}.
\]
Conditioning on the absolute ranks gives
\[
\operatorname{Cov}(\bar X_n,W_n^+)
=
\frac1{2n}\sum_{r=1}^n r\,\mathbb E A_{(r)}
=
\frac{a(2n+1)}{12}.
\]
The checker compares this exact order-statistic expression through sample size \(200\) with the theorem's formula using
\[
\mathbb E|X|=\frac a2
\]
and
\[
\mathbb E|X-X'|=\frac{2a}{3}.
\]

The normal and uniform correlation simplifications are also checked numerically over a finite grid of sample sizes. These computations are supplementary and do not substitute for the general proof.

Independent audit has not been performed.

Deterministic replay result: `VERIFY_OK walsh_identity_checks=8190 exact_null_moment_checks=28 uniform_covariance_checks=200 uniform_correlation_checks=200 normal_correlation_checks=200`.
