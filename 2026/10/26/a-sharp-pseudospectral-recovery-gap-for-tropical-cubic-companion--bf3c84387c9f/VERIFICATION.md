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

`check.py` performs exact symbolic checks of the determinant, companion equivalence, and both Gram invariants, followed by direct singular-value calculations for several values of the scale parameter. It checks the limiting normalized pencil residual, both singular-vector recovery ratios, and the exact zero-coordinate thresholds numerically. Run with Python 3, NumPy and SymPy. The exact symbolic identities and proof in `RESULT.md`, rather than finite trials, justify the universal assertions.

The calculation is for unstructured normwise residuals of the explicit pencil, not a statistical claim about the output of a particular generalized eigensolver. The coefficientwise polynomial residual equals one for every positive real parameter directly because all coefficients are positive.
