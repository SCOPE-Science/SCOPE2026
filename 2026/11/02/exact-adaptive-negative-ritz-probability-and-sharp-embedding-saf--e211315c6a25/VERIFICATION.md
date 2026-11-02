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

Execute `python verify.py` beside the seven packaged artifacts (NumPy and SciPy needed). The reported successful execution gave 5,612 deterministic checks and 480,000 seeded Gaussian sketch samples, at sketch dimensions 2, 3, 5 and 8; exact-beta analytic reference values are also printed for dimensions 4 and 12. It checks the two-by-two symmetric determinant test, the cosine/Householder sharpness construction, and probabilistic empirical agreement. One fixed-before-sketch comparison is a diagnostic of differing quantifiers and is not claimed as a new formula.

The exact event probability is proven using the spherical beta distribution; the deterministic all-vector statement is proven by the spectral cosine inequality and explicit Householder construction. Finite checks cannot establish universal claims. Numerical sampling only diagnoses formula implementation.

The motivating full manuscript was not available for comprehensive inspection, and no independent mathematical audit or exhaustive specialist priority certification is asserted.
