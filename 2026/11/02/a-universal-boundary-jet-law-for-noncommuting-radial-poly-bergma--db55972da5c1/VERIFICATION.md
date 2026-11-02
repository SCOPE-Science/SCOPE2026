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

# Verification

## Analytic evidence
The result follows from the explicit Fourier-block decomposition in the primary literature and the complete direct proof in `RESULT.md`, Steps 1–4. The critical identities are the beta-variance formula for the first Jacobi off-diagonal, the next Jacobi recurrence coefficient, the exact compression identity for the square of the radial variable, and the uniform third-order Taylor bound. These are algebraically checkable for any fixed \(\alpha>-1\), and their limits are given in the proof.

## Computational cross-check
Run `python CHECK.py` using NumPy and SciPy. The script recomputes compressed polynomial matrices via Gauss–Jacobi quadrature, independently of the displayed closed coefficients. It checks 35 parameter/frequency pairs, the large-frequency coefficient for several parameters, and the boundary-jet law for a pair of nonmonomial cubic symbols. The script prints two PASS lines and totals 121 passed assertions. Finite experiments are corroborative and do not certify infinite-dimensional assertions.

## Boundaries and open checks
No independent mathematical audit has been performed. The complete text of one relevant 2025 paper was not available; the historical-priority comparison therefore has a residual risk. The sharp Schatten classification requires a nonzero boundary two-jet determinant and does not extend as stated to the vanishing case.
