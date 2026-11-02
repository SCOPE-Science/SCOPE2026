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

# Reproducibility

Run `python verify_thermal_refresh.py` using Python 3 with NumPy and SciPy. The code independently enumerates all eight reset/no-reset gap patterns in 250 samples and compares connected four-point moments with the analytic formula; checks 237 inequalities for decreasing two-window variance ratios; numerically recovers the model parameters from 80 synthetic three-moment sets; simulates 150,000 conditionally Gaussian renewal histories; and checks both short-time and long-time cumulant coefficients. The simulation has random sampling uncertainty and numerical tolerance; neither finite grids nor finite simulations certify an infinite-parameter theorem. The analytic proof in RESULT.md establishes all-time claims.

Independent scientific audit is not performed.
