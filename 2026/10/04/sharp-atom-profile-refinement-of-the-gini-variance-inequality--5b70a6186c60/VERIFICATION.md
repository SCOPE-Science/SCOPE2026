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

The proof is analytic. The accompanying checker uses exact rational arithmetic.

For randomly generated finite probability vectors and ordered rational support
locations, it verifies
\[
\Delta=4\operatorname{Cov}(X,F_{\rm mid}(X)),
\]
\[
\operatorname{Var}(F_{\rm mid}(X))
=
\frac{1-\sum_i p_i^3}{12},
\]
and the claimed Gini--variance inequality.

For each random probability vector it constructs
\[
x_i=F_{\rm mid}(x_i)
\]
up to a positive affine rescaling and checks exact equality. It also verifies
the support-cardinality bound and the uniform arithmetic-progression equality
case.

For random reflection-symmetric probability profiles, the checker constructs
the mid-distribution-spaced symmetric support, enumerates all two-sample
minimum/maximum outcomes, and verifies the sharp correlation value
\[
\frac{1-\sum_i p_i^3}{2+\sum_i p_i^3}.
\]

Finite replay does not replace the Cauchy--Schwarz and randomized-transform
proof.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK identity_checks=72000 inequality_checks=24000 equality_checks=119600 cardinality_checks=48000 symmetry_checks=9000 uniform_checks=198`.
