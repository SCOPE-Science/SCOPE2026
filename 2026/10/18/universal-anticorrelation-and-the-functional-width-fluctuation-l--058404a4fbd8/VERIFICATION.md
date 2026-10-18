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

Analytically verified: the support-width profile for even and odd regular polygons, the explicit two-piece autocorrelation integral, strict derivative sign via the decreasing sinc function, zero average of centered autocorrelation, uniform Taylor limit in the sup norm, the limiting covariance, odd-to-double-even exact process law, and the limiting marginal third moment.

Reproducible finite computational checks: run `python3 verify.py` with Python 3 and standard library only. The checker enumerates all vertices and directly projects onto 24,000 deterministic directions for each of nine polygon orders and five lags, comparing the empirical means and covariances to the analytic formulas. It reports 45 comparisons and discrepancies below the stated thresholds.

Finite numerical checks do not certify the all-\(n\) identities, uniform errors, or originality; those rely on the proof and literature comparisons. Independent external validation has not been performed.
