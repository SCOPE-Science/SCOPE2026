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

# Reproducible verification

The accompanying `verify.py` uses the exact seven-vector coordinates, generates all twelve triangular-edge/apex-sign facets, checks the facet determinant magnitudes and initial volume, computes the full \(21\times21\) constrained Hessian in \(\mathbb Q(\sqrt3)\), and verifies its exact factored characteristic polynomial. It also checks that six explicitly constructed skew-generator rotation vectors span the nullspace. A separate floating-point convex-hull comparison tests the predicted second-order coefficient along randomized tangent perturbations, across several step sizes.

To replay, install the dependencies specified in `requirements.txt` and run `python verify.py`. A successful exit indicates the finite identities and numerical checks passed on that installation. The extension from negative transverse Hessian to sharp local stability uses the normal tubular-neighborhood and Taylor argument in `RESULT.md` and is not an assertion of computer-certified infinite mathematics.

No independent scientific audit has been performed.
