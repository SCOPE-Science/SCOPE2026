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

The exact characteristic-five identity checker `verify_symbolic.py` reconstructs the Cartier coefficient matrix, all displayed factors, the elimination resultants, and the transverse intersections. The second checker `verify_fields.py` independently constructs the Cartier matrix from a convolution of the defining octic over all 625 coefficient pairs in \(\mathbb F_{25}\), iterates the semilinear operator, and compares its rank with the exact closed-form formula. Both checkers completed successfully.

The finite-field census is verification evidence only. The infinite-field assertions follow from the explicit factorizations, elimination resultants, exclusion of singular parameters and nonvanishing Jacobians in `RESULT.md`. The statement classifies marked parameters, not abstract isomorphism classes; an external independent mathematical audit has not been conducted.
