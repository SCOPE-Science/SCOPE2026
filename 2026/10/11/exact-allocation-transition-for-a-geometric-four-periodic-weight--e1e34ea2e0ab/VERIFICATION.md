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

# Reproducibility and limits

The analytic proof is in `RESULT.md`. To perform the finite supplementary checks, run `python verify_weighted_shift_budget.py` with Python 3, SymPy, NumPy, and SciPy installed. The executed program returned `WEIGHTED_SHIFT_BUDGET_THRESHOLD_AND_ASYMPTOTIC_CHECKS_OK`.

The script checks the four-vertex characteristic equation at its exact threshold for three rational geometric ratios, confirms the effective two-state eigenvalue equation and ordering at the predicted optimizer displacement, and numerically minimizes the largest eigenvalue of 100-by-100 truncated Jacobi matrices for three geometric ratios below and above the threshold and at large budgets. The exact-rational identities are finite algebraic checks; the finite-section spectra are numerical evidence only. Neither those checks nor a successful process exit certifies the assertion for all infinite-dimensional operators or all real parameters.

Critical noncomputational steps requiring mathematical scrutiny are the compact Jacobi Perron eigenvector simplicity, the strict positive Hessian from the row comparison, the endpoint one-sided perturbations, and the uniform spectral-gap Schur estimate before the two-level optimization. The proof provides these steps, but no independent scientific audit has been performed. The complete manuscript of the 2026 motivating paper was not accessible during the literature comparison; this limits the originality assessment without altering the standalone analytic derivation.
