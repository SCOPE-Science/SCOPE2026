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

The analytic proof establishes the renewal formula, strict unique global Bellman-optimal residence threshold, exact Laplace-order comparison, classical limit, and small-hazard variance expansion. For finite reproducibility checks run `python3 verification/check.py` from the root of this package using only the Python 3 standard library.

The script verifies 2,311 assertions including the rational Laplace factors in the exact two-law example, the corresponding analytic thresholds and exact optimized rewards, finite parameter sweeps of monotonicity and unimodality, a nonexponential strictly decreasing marginal-gain function, and convergence to the small-hazard variance coefficient. A successful script is a numerical/symbolic consistency check, not a substitute for the analytic infinite-distribution proof. No independent validation or audit was conducted.
