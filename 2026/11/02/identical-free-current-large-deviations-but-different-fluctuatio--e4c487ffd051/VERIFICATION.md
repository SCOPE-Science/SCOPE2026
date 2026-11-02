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

# Reproduction and checked limits

Install Python 3, NumPy, and SciPy, and run `python verify.py` in the directory containing this document. The completed execution returned:

`PASS 432 independent deterministic matrix, quadrature and Legendre checks`

The executable independently constructs the four-phase tilted generator rather than relying on the displayed symbolic factorization, computes its characteristic determinant and eigenvalues at multiple parameters, uses numerical matrix exponentiation for the phase orientation correlation, evaluates both finite-time and harmonic covariances by direct numerical quadrature, checks the derived strict gaps, and compares a numerical Legendre optimization with the athermal rate formula.

For an exact algebraic check, expansion of the four-state determinant gives a product of the two quadratic factors stated in equation (7) of `RESULT.md`. Its spectral ordering is elementary and remains true for all real tilts, not just the tested grid. The finite-noise LDP follows from finite-state Feynman–Kac, Gaussian independence, and contraction. The boundary case \(D=0\) uses explicit no-reversal events to prove the endpoints, since differentiability of the cumulant-generating function alone does not provide lower bounds at both finite-slope extremes.

The numerical tests are bounded sample checks and are not an exhaustive certificate for the infinitely many parameters or the infinite time limit. The publication-priority comparison is based on inspected accessible material, not a claim that every possible reference has been read. Independent external auditing remains unperformed.
