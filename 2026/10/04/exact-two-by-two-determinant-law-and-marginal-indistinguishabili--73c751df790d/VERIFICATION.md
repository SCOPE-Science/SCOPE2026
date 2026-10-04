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
The package verifies the exact two-dimensional algebra behind Adafactor's factored second-moment reconstruction.

`verify.py` uses exact rational arithmetic to check the determinant checkerboard identity, the underestimation and overestimation families, identical row and column marginals for the indistinguishable pair, and the two-step exponentially smoothed history formula.

The finite checks are algebraic transcription guards. The universal impossibility statement is proved symbolically in `RESULT.md`.
