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

# Verification checks and limits

Run `python verify.py` using Python 3 with NumPy. The recorded output is in `verification_output.txt`. The program independently evaluates all two-neighbor edge intensities, compares finite-difference Jacobians with the exact cycle matrix, diagonalizes that matrix to check all Fourier eigenvalues, checks maximum-eigenvalue multiplicity and the critical value by parity, inverts the predicted subcritical covariance, checks independent Fourier reconstruction, and confirms conservation of the total vertex firing intensity. It completed 315 checks successfully.

Computations concern finite-dimensional formulas and do not certify the asymptotic central limit theorem. The proof invokes (i) established almost-sure homogenization from Qin (2026, Theorem 1.1); (ii) a localized quadratic moment estimate for normalized deviations, with error exponent strictly below one-half; (iii) spectral variation of constants and dominated integral error bounds; and (iv) a bounded-jump multivariate martingale central limit theorem with predictable brackets converging modewise to the stated covariance. The argument does not cover exponents greater than the displayed critical exponent.
