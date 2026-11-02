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
# Reproducibility and limitations

The attached `verify_thermal_peak.py` is standalone with Python, NumPy and SciPy-compatible numerical-array operations (the implementation uses NumPy only). It computes exact orbital mean-crossing bounds analytically, solves the eccentric-anomaly equation by bracketed bisection, evaluates the periodic scalar filter by Fourier multipliers and performs comparisons at 32 parameter points. It reports finite-grid accuracy only; the proof of all-eccentricity and all-positive-time-constant quantifiers is in `RESULT.md`.

The checks do not establish atmospheric applicability, observer light-curve timing, historical priority, measurement uncertainty or external independent validation. The supplied evidence concerns the linear, constant-relaxation-time proxy exactly as defined in `RESULT.md`.
