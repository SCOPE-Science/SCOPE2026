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

The analytic proof reduces the result to four checkable ingredients: conditional exchangeability; the fixed-count first- and second-order inclusion probabilities; an exact linear-plus-degenerate-quadratic decomposition of AP@k; and two coefficient-square limits.

The included `verify.py` performs finite exhaustive checks for \(2\le k\le8\), verifies the published online mean and variance formulas at several prevalence values, verifies the exact decomposition term by term, confirms the exact identity
\[
\eta_k(m)-\mu_k(m/k)=\frac{m(k-m)(H_k-k)}{k^3(k-1)},
\]
and numerically checks convergence of the normalized coefficient sums to \(5\) and \(1\). Its expected terminal output is `VERIFY_OK`.

The checker supports finite algebra only. It is not a substitute for the Lindeberg argument, the Riemann-sum proof, or the literature comparison. No claim is made for prevalence sequences approaching the boundary, heterogeneous relevance probabilities, or dependent relevance indicators.
