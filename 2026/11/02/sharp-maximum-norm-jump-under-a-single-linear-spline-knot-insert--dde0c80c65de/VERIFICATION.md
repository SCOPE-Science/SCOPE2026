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

# Verification and reproducibility

Run `python verify.py` with Python 3 and SymPy installed. No downloaded inputs or external data files are needed. The script reconstructs the piecewise residual and symbolic orthogonality moments, calculates exact integrals, and constructs a separate three-hat mass-matrix kernel and affine Gram kernel. For rational interior knot positions it checks 905 exact identities and inequalities, including all three knot-evaluation row norms and an explicit quadratic-input witness.

The infinite continuum of knot positions is established by the exact algebra and monotonicity arguments in `RESULT.md`, not by a finite sample or a numerical solver. Equality of operator norms uses an actual measurable extremizing sign function. The older spline-stability preprint appeared publicly on 2006-11-19; the principal motivating projection-supercloseness preprint first appeared on 2014-08-18. The remaining publication-priority risk concerns possible older Franklin-function formulas under different terminology.
