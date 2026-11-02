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

# Reproduction and scope

Run `python3 verification/check_regular_polygon.py` in Python 3; only the standard library is used.

Actual checks completed successfully: 78 polygon-order comparisons (each based on independent exact piecewise-polynomial triangle integration evaluated with floating-point arithmetic), three checks against known rational values, 480 sampled interior-kernel comparisons, and three large-order convergence checks, for 564 asserted comparisons. The largest difference in the 78 row comparisons was approximately `1.33e-15`. The numerical disk reference was approximately `1.8559734676794573`, and the predicted quadratic convergence coefficient approximately `5.069723344967015`.

The code is an independent finite sanity check of the explicit norm formula; it does not exhaust all polygon orders, prove the continuum vertex-extremizer result, or prove the asymptotic limit. Those parts rely on the analytic proof in `RESULT.md`. No independent mathematical audit is included.
