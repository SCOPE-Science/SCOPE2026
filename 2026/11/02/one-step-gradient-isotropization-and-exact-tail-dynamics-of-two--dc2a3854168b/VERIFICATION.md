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

# Reproducibility and limitations

Run `python3 VERIFY.py` in this package directory using the Python standard library only. The script constructs positive-definite two-by-two left curvature matrices and gradient polar SPD factors with exact rational rotations, as well as two- and three-column rational row-isometries. It confirms the first-step symmetric trace-free identity, exact scalar-square property, and gradient isotropy, and checks six successive linear-tail identities. It also tests rank-one boundaries. This is finite supplementary evidence; the result for all real positive-definite matrices, all column counts, and arbitrarily many iterations is proved algebraically in `RESULT.md`.

Additional independently executed direct SVD checks of 300 randomized dense two-by-many matrices numerically agreed with exact first-step isotropy and subsequent linearization. These floating-point tests cannot establish the theorem. No independent mathematical audit, formal proof-assistant certification, or third-party reproduction has been performed.
