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

Run `python checker.py` with Python 3 and NumPy. The checker separately sums the defining Zak series and compares it with the geometric closed formula, verifies the modulus factorization, numerical spectral normalization, Hessian coefficients at the unique zero, and the exact parameter ordering around the golden-ratio transition. The separate density-validation script evaluates the spectral density on both sides of the seam cusp and compares the sharp coefficient.

The mathematical evidence for the unrestricted theorem is the exact conditional density change of variables and the local critical-level analysis in RESULT.md. Sampling cannot prove all-parameter spectral assertions, and the checker is not an independent mathematical audit.
