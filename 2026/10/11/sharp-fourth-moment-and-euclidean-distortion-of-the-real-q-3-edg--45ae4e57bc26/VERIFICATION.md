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

# Verification of the cube-edge fourth-moment theorem

Invoke `python3 verify_cube.py` using a standard Python 3 interpreter; there are no additional dependencies.

The checker reconstructs the unique twelve cube edges and six square faces, enumerates every degree-four monomial in twelve coefficient variables by exact integer coefficients, and verifies the claimed deficit equality coefficient by coefficient. It then exhausts the \(4095\) nonempty coefficient supports, carries out exact rational \(LDL^{\mathsf T}\) positivity checks and stationary-point solves, and checks the absence of any negative interior stationary value. It verifies that the only zero-valued positive-definite stationary supports are the six square faces, that each has uniform weights, and that distinct face zeros have strictly positive mutual quadratic coupling.

The step from finite support checks to the universal inequality on the continuous simplex is the proved minimal-support convexity argument in RESULT.md. The same Hessian-null-direction argument plus positive face cross-coupling supplies a complete equality classification. The Euclidean-distance calculation follows from a separate exact symmetry-averaging argument and does not depend on a finite optimization grid.

This is a reproducible finite certificate and a same-model scientific review, not an independent audit.
