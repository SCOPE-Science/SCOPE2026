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

The exact symbolic checker `artifacts/verify.py` reconstructs the representative block-circulant doubly stochastic matrix and the three naive orthostochastic octics. It verifies that one restriction is zero, the other two are equal, and their common equation has the claimed degree-four plus degree-six decomposition. It checks the determinant of the four normal linear forms, confirms squarefreeness by a derivative gcd equal to one, and verifies an explicit orthogonal square root for the real balanced line.

The checker proves only the packaged algebraic statements. It does not certify the endpoint singularities at \(p=0,1\), the local geometry of the full \(Z_4\), or analytic branch decomposition.
