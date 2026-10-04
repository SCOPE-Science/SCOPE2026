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

The analytic verification reconstructs the Gaussian/Wishart reduction, the Beta factorization, the exact quadratic-risk decomposition, and the source-only comparison. The key finite-sample identity is
\[
\mathbb E\|\widehat\theta_A-\theta\|^2
=\frac{r\sigma^2}{n_s+n_t}+\frac{\sigma^2n_s}{n_t(n_s+n_t)}K_{r,n_s}.
\]
The included deterministic checker evaluates \(K_{r,n_s}\) by numerical quadrature, checks the \((r,n_s)=(4,100)\) value and boundary, checks the limiting \(\chi_r^2\) integral, and confirms \(H_4=4e^{-2}\) numerically.

The checker is not an exhaustive proof engine. The infinite-family statements rely on the analytic argument in RESULT.md. No claim is made outside the stated Gaussian mean specialization, and no independent audit has been performed.
