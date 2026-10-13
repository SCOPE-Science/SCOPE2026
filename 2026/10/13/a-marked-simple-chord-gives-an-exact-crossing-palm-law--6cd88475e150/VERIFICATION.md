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

The theorem is analytic. The accompanying checker performs an independent exact-rational replay on all perfect matchings through size \(7\).

For each \(n\), it directly reconstructs the circular simple-chord count \(S_n\) and crossing count \(X_n\). It verifies
\[
\mathbb E S_n=\frac{2n}{2n-1},
\qquad
\mathbb E X_n=\frac{n(n-1)}6,
\]
the covariance (6), the simple-chord variance (7), and the established crossing variance (8).

It verifies the Palm identity for \(f(x)=1\), \(f(x)=x\), \(f(x)=x^2\), \(f(x)=x^3\), and for every point-mass indicator on the finite crossing support.

It also checks first-order stochastic domination of \(X_n\) over \(X_{n-1}\) from the exact empirical laws.

The all-\(n\) proof does not rely on enumeration. The checker is a finite replay of the deletion and moment consequences.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK matchings_checked=146599 moment_checks=30 palm_checks=86 stochastic_checks=62 correlation_checks=6`.
