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

The proof is analytic. The accompanying checker uses exact rational arithmetic at unit rate.

For every \(2\le n\le120\), it reconstructs the sample-variance quadratic-form matrix from cumulative exponential spacings, evaluates the independent-coordinate covariance formula before simplification, and verifies exact equality with
\[
\frac{H_{n-1}^2+H_{n-1}^{(2)}}{n-1}.
\]

For every \(2\le n\le500\), it separately verifies the triangular harmonic identity and the exact squared-correlation formula using
\[
\operatorname{Var}(R)=H_{n-1}^{(2)}
\]
and
\[
\operatorname{Var}(S^2)=\frac{2(4n-3)}{n(n-1)}.
\]

Rate scaling is analytic: covariance has homogeneity three and correlation is scale-free.

Finite replay is supplementary. The universal proof is the independent-spacing quadratic-form calculation in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK matrix_cov_checks=119 harmonic_identity_checks=499 variance_checks=998 correlation_checks=998`.
