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

Run `python verify.py` with Python 3 and SymPy in the same directory. The script derives the characteristic polynomial directly from the Jacobian, checks the equilibrium identities and simplified coefficient expressions symbolically, verifies the exact stability-window factorization and endpoint imaginary pairs, and compares quartic root counts with Routh signs for 24 parameter-speed combinations. All assertions completed in the accompanying reproducibility run.

The general proof is the exact equilibrium parametrization, positivity of the quartic coefficients on the entire negative-strength range, and the quartic Routh–Hurwitz argument. Numerical spectra are auxiliary checks and do not establish stability for infinitely many parameter values. No claim is made about the nonlinear behavior at either spectral crossing, global population convergence, or the existence of limit cycles.
