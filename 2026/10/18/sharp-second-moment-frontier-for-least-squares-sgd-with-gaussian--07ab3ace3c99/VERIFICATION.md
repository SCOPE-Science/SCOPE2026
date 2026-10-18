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

# Verification and reproducibility

Run `python gaussian_ar1_sgd_verify.py` with NumPy and SciPy. The program computes the principal eigenvalue of a symmetric Gauss–Hermite Nyström approximation, checks the exact iid growth factor \(1-2s+3s^2\), verifies the exact two-point fourth-moment formulas using independent normal quadrature, and confirms convergence of local critical roots across three quadrature orders. The run completed: `PASSED 106 deterministic quadrature/threshold checks`.

The calculations are finite-order approximations; none certify the infinite-dimensional top eigenvalue, operator compactness, strict spectral monotonicity, or the universal asymptotic expansion. Those conclusions are derived in `RESULT.md`. The classical correlated-input LMS literature, especially the full text of Douglas (1993), was not completely accessible; this is a bibliographic limitation, not a numerical verification.
