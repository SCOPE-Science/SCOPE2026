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

# Reproducibility and proof limits

Run `python verify_minimax.py` using Python 3 with NumPy and SciPy installed. The standalone program checks exact rational spherical variance coefficients for dimensions 3, 4 and 6, then computes the nonasymptotic curvature weights of corresponding ellipsoids by Gauss–Jacobi quadrature. Its numerical simplex maximizers concentrate on the first and last intrinsic-volume indices; the observed quadratic ratios approach the mathematically derived constants.

These numerical experiments are not infinite proofs, do not substitute for the stated minimax/KKT and Taylor arguments, and do not certify historical priority. The result is proved for the minimax of the already-established leading random-polytope error functionals; no finite-sample minmax theorem or uniform remainder across all sampling densities is claimed.

Independent audit has not been performed.
