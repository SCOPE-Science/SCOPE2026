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

The proof is analytic and does not depend on numerical certification. The bundled checker performs the following finite-precision replay:

- bisects the strictly decreasing scalar equation on \((R^2/8,R^2/4)\);
- reconstructs the three center-to-side distances and verifies the area identity;
- checks that the half-chord ratios are \(2:\sqrt3:1\);
- compares the resulting center with the published decimal benchmark;
- verifies that all three triangle vertices lie outside the equal-area disk;
- evaluates the three circular caps and reproduces the stated Fraenkel asymmetry.

The finite calculation does not prove the existence, uniqueness, or global-optimality statements. Those follow from the derivative formulas, strict monotonicity, positive-definite cap Hessian, and Brunn--Minkowski concavity given in `RESULT.md`.
