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

Analytical checks: verify the monomial normalization and the scalar phase factors in the parity split; compare the Toeplitz row-symbol supremum with weakly-null plane-wave packets; confirm that compactly supported Bergman Toeplitz symbols are compact via the reproducing kernel trace bound.

Executable: `python3 verify.py` tests basis coefficients for the monomial cases and the antipodal Fourier identity using deterministic finite data. Finite tests cannot certify the infinite-dimensional essential norm; that is proved in `RESULT.md`.

No independent audit has been performed.
