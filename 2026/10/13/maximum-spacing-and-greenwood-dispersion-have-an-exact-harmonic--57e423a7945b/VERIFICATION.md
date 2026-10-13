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

The proof is analytic. The accompanying checker performs exact-rational algebra for every
\[
2\le m\le80.
\]

For each \(m\) and each inclusion-exclusion order \(k\), the checker expands the polynomial
\[
(1-kt)^{m-1}
\left(
kt^2+\frac{2kt(1-kt)}m+\frac{2(1-kt)^2}{m+1}
\right)
\]
coefficient by coefficient and integrates it exactly over \(0\le t\le1/k\).

It then sums the resulting rational values with inclusion-exclusion and compares them with the closed mixed moment. Independently, it verifies the two binomial-harmonic identities, the maximum-spacing first two moments, the Greenwood first two moments, the covariance, strict positivity, and the exact correlation-square relation.

The asymptotic statement is proved from the standard harmonic-number asymptotics; the checker evaluates several large-\(m\) ratios only as a supplementary numerical sanity check.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK term_integrals=3239 mixed_moments=79 harmonic_identities=158 marginal_checks=316 covariance_checks=79 positivity_checks=79 correlation_checks=79 asymptotic_checks=3`.
