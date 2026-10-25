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
# Verification

The `verify.py` program uses NumPy linear algebra to construct regular simplices in dimensions 2–6, forms the product-sphere Gram matrix of symmetric trace-free velocities, calculates the Hessian from the analytical bilinear formula, and solves generalized eigenvalue problems. It checks exactly the predicted multiplicities and values within numerical tolerance. Six independent random geodesic perturbations per dimension are checked by central differences of \(-\log V\) against their analytic second variations; the program fails on any mismatch.

To reproduce: `python -m pip install -r requirements.txt` and then `python verify.py`. This program is a numerical consistency test only and is not an exhaustive proof for arbitrary dimensions. The proof of the universal spectrum and sharp distance coefficients is in `RESULT.md`. Independent assessment has not been conducted.
