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

The analytic proof uses a Hilbert-space quadratic-form identity. The accompanying checker uses a different route based on classical order-statistic formulas.

For iid uniforms with order statistics \(Y_{(1)}<\cdots<Y_{(n)}\), it constructs
\[
W_n^2
=
\frac1{12n}
+
\sum_{i=1}^n
\left(
Y_{(i)}-\frac{2i-1}{2n}
\right)^2
\]
and
\[
U_n^2
=
W_n^2
-
n\left(\overline Y-\frac12\right)^2
\]
as exact multivariate polynomials.

Each monomial is integrated over
\[
0<Y_{(1)}<\cdots<Y_{(n)}<1
\]
against density \(n!\). For exponents \(a_1,\ldots,a_n\), the checker uses the exact iterated-integral identity
\[
n!\int_{0<y_1<\cdots<y_n<1}
\prod_{i=1}^ny_i^{a_i}\,dy
=
\frac{n!}{
\prod_{k=1}^n
\left(k+\sum_{i=1}^ka_i\right)
}.
\]

All arithmetic is rational. For \(1\le n\le8\), the checker recomputes both means, both variances, and the covariance from the polynomial integrals and compares them to the theorem. For \(2\le n\le8\), it also verifies the exact squared-correlation formula.

These finite checks do not prove the all-\(n\) theorem; the arbitrary-\(n\) proof is the independent quadratic-form derivation in `RESULT.md`.

Independent audit has not been performed.

Deterministic replay result: `VERIFY_OK sample_sizes=8 exact_moment_checks=40 exact_correlation_squared_checks=7`.
