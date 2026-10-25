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

# Reproducibility and verification

Run `python check_torque.py` with Python 3, SymPy, NumPy, SciPy. The standalone deterministic checker passed 77 assertions. It first checks the general symbolic matrix eigenfunction identity, the wedge normalization, the quadratic generator, and the discriminant identity. It then independently computes stationary covariance matrices for five stable rational drifts (including symmetric node, nonsymmetric node, complex-eigenvalue focus, defective Jordan block, and scalar drift), checks the Gaussian transform and positive-variance criterion, and compares direct Wick covariances at four nonnegative lags against the predicted single-exponential covariance. Finally it checks the asymmetric-diffusion Brownian-coupling formulas and critical-normalization limits.

The rigorous proof resides in RESULT.md. Numerical matrix exponentials alone cannot certify all drift matrices; the symbolic generator identity does. The soft-mode limit uses parameter values approaching, not equal to, the excluded boundary. This is not a test of the raw noisy angular-velocity observable or of experimental small-coupling validity. No independent audit has been performed.
