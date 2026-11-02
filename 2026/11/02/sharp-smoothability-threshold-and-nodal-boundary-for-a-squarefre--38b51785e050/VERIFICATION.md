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

Run `python verify.py` with Python 3 and SymPy. A successful run prints `VERIFY_OK` and the exact finite counts. The accompanying `certificate.json` records the output from an actual invocation.

The program checks the local Hessian determinant \((-1)^{r+1}c^2\) in four independent sizes; the generic proof for arbitrary \(r\) is the block determinant argument in `RESULT.md`. It also checks the quartic's six coordinate-line restrictions and their simple cubic roots, their local Hessian determinants, and the exact critical-value argument on the remaining affine chart. The checker is a consistency test, not an exhaustive classification of all polynomials in the coefficient family.

The general infinite-dimensional parameter statement follows from the analytic Hessian criterion, the projective dimension theorem, Bézout and Bertini in `RESULT.md`; it is not inferred from a finite search. The first-public-source date comes from arXiv:2610.34641v1 (2026-10-25). The theorem's historical priority and mathematical proof have not undergone independent validation.
