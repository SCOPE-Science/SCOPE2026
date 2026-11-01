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

The accompanying `checks/check_laguerre.py` constructs exact rational beta moments, rational covariance matrices and determinants, checks the monic Jacobi determinant identity at finite parameter values, computes homogeneous multiplicity sums, and compares selected high-precision eigenvalue ratios to their Laguerre limits. Run with `python checks/check_laguerre.py` and installed `mpmath`. An assertion-free completion prints the count actually checked. The infinite-dimensional proof instead rests on the positive compression identity, Rodrigues integration, min–max eigenvalue separation, dominant principal minors, and counting-function inversion, as detailed in RESULT.md.

No independent mathematical audit, publication-priority certification, or machine proof has been performed. Finite computations cannot establish the limit statements on their own.
