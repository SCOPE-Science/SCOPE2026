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

# Reproducibility

Run `python3 johnson_cycle_checker.py` with Python 3 standard library from the extracted package. It uses exact `fractions.Fraction` arithmetic, enumerates the triangular graphs for integers n=3..9, checks the reference-column mean-zero potential and all signed Laplacian identities, constructs every projected edge column, and checks symmetric projection coefficients and the two all-column norm formulas.

The output ends with `CHECK_OK: exact incidence, potential, symmetry, and full column norms` after seven parameter cases. The analytical proof of all-n uniqueness and optimality is in `RESULT.md`; finite checks alone cannot prove it. No independent audit or external formal certification was performed.
