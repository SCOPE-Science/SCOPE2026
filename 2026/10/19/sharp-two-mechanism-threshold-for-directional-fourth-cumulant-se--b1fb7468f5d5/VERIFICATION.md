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

Run `python verify.py` with Python 3, SymPy, NumPy, and SciPy. The checker derives the characteristic polynomial of the four-heading tilted generator and the second/fourth coefficients using exact symbolic identities. It then independently constructs a 20-state moment hierarchy (four orientations, moment orders zero through four) and compares the long-time connected fourth-cumulant slope in 24 rate/direction cases. The executable test reports **31 passing checks** in its current form.

The complete mathematical justification is the finite-dimensional Perron eigenvalue expansion and exact sign inequalities in `RESULT.md`. Finite parameter tests do not establish the theorem for all rates or prove publication originality. The singular threshold is a statement about the asymptotic coefficient; finite-time behavior there is not certified. Scientific priority remains subject to independent examination of the general Fourier–Laplace transform already available in arXiv:2209.05912.
