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
# Reproducibility and evidential limits

Run `python mahler_checker.py` with Python 3 and SciPy. The script uses adaptive quadrature to reproduce the two integrals, Brent root finding to locate sample maxima, two independent computations of planar polar area, and an analytic Euclidean specialization in three dimensions. All assertions passed in the documented execution. This finite check does **not** establish uniqueness or the all-dimensional claim; that follows from the exact differentiation and strict decrease of \(T\) in `RESULT.md`. External independent audit is not available.
