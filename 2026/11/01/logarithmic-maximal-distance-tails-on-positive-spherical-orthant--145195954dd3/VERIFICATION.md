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
# Reproducible verification

Run `python check_orthant.py` with Python 3, NumPy, SciPy, and SymPy. It verifies the exactly integrated product-density identity for the three-dimensional chart, the beta-simplex coefficient, sphere-area normalizations, the exact two-dimensional probability, and formulas for several dimensions. The deterministic Sobol quadrature integrates an entire three-dimensional projective chart after splitting its domain at a coordinate ratio equal to the small threshold; for the tested thresholds the chart transformation and spherical weights are exact. Its ratios to the predicted coefficient were approximately 1.36835, 1.18371, 1.09261, and 1.04622 for angular inner-product thresholds \(e^{-5}\), \(e^{-10}\), \(e^{-20}\), and \(e^{-40}\), respectively. The trend is consistent with the stated logarithmic leading term and its slow lower-order correction; deterministic numerical quadrature alone does not prove the limit.

The all-dimensional claim is supported by the direct finite-box comparison and exact beta-simplex integral in `RESULT.md`, not by extrapolation from tested dimensions. The proof assumes dimension fixed as the threshold goes to zero. No independent audit has been performed.
