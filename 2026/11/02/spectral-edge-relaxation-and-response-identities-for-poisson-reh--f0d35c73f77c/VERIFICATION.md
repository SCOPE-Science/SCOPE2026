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

The full analytic proof and domain restrictions are in `RESULT.md`. `verify.py` is independently executable using Python, NumPy, and SciPy; it checks numerical quadratures for the two exact covariance representations, strict log-convexity at sampled lags, the edge coefficient, the derivative of the published stationary mean, the Haff long-lag amplitude, and the generator's short-lag slope identity.

At the tested parameters it completed 288 numerical comparisons. The maximum tested relative error between direct-age and positive gamma-mixture covariance quadratures was approximately \(4.82\times10^{-7}\), and the maximum small-edge ratio deviation at the tested positive cutoffs was approximately \(0.00414\). Finite quadratures and finite-lag trends are not a proof of the all-parameter result or asymptotic limits; these are established by the positivity identity, dominated convergence, and Watson's lemma in the manuscript.

No external independent scientific audit has been performed. Claims about microscopic collision noise or statistical error bounds from finite time series are not established.
