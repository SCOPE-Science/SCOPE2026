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

# Verification record

The analytic argument in `RESULT.md` establishes the theorem in all product dimensions and for every positive real dilation. It proves the translated-simplex overlap identity, the exact missing-translate supremum, product factorization, the strictly convex factor-dimension envelope, and the complete median-set inequalities. At exclusion boundaries, the supremum is evaluated by approaching excluded translates; it is not falsely asserted to be a maximum.

The embedded `verify_product_depth.py` was executed using Python 3 with standard-library exact rational arithmetic. It passed **434 exact assertions**, including independent planar polygon clipping of translated triangles, direct interval intersections, algebraic overlap identities, approach-to-supremum witnesses for triangular prisms (including outside-support and boundary points), exact phase-formula checks, and extreme-factor-envelope checks for several products of simplices. These tests are finite diagnostics and are not proofs in arbitrary dimension. No external proof assistant, independent mathematical audit, or certification was performed.

Scientific limitations are the fixed product geometry, common dilation and uniform probability measure. Residual literature risk concerns equivalent formulations in historical work on translated product covariograms or depth tensorization.
