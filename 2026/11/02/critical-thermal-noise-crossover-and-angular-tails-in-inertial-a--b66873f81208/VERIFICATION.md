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

# Verification record

The analytic claim was checked against the exact complete-reset stationary renewal representation and the Itô variation-of-constants formulas for the physical model. Conditional on the exponential reset age, the limiting translational noise has the positive-definite two-variable covariance stated in the proof. The density is a Gaussian mixture, and the directional saddle equation has exactly one positive root and a positive second derivative. The large-radius asymptotic is for the limiting stationary law, not for a uniform joint limit in radius and reset rate.

Execute `python3 verify.py` in the directory containing the embedded files. This run returned `PASS 650 deterministic algebra, covariance, angular-tail and quadrature checks`. Checks include the exact conditional covariance determinant, analytic saddle equation and angular order, exact high-rate mean identity, finite-reset thermal covariance and direct numerical integration of the limiting radial density. The test code is supplemental: it does not establish generality beyond the analytical derivation and does not constitute independent validation.

Source inspection covered the relevant full-text sections of the 2026 inertial resetting study and two earlier full-text studies of unforced random acceleration and overdamped active resetting. The previously known zero-force law and the known \(r^{-3}\) mean-squared-displacement regime are not claimed as discoveries. Broader priority coverage has not been independently certified.
