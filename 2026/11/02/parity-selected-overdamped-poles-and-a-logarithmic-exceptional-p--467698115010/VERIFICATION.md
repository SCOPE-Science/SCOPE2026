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

## Reproducibility
Run `python check_passive_chain_ep.py` with Python 3, NumPy and SciPy available. This evaluates the normalized finite-dimensional survival-sector matrix, independently forms its characteristic determinant, and checks the Chebyshev expression, imaginary-axis root residuals, selected thresholds, length ordering, and representative asymptotic values. The recorded execution reported `PASS: 495 numerical determinant/pole/ordering/asymptotic checks`.

## Mathematical checks and limitations
The matrix normalization is the one displayed in `RESULT.md`: the sink contributes \(-i\kappa/2\) at the last site, and \(g=\kappa/(2J)\). The derivation via Chebyshev recurrence and the hyperbolic root equations is a symbolic all-dimension proof. Log-convexity proves the unique even-length threshold; strict monotonicity proves the odd-length one-pole law. A second-order characteristic zero and one-dimensional tridiagonal eigenspace prove defectiveness. The large-length constant follows from the exact minimizer equation, not numerical extrapolation. The finite script cannot establish novelty, prove all-length statements, or resolve uninspected publications.
