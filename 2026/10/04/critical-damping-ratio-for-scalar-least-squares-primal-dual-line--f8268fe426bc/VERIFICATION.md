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
The proof was checked by reconstructing the scalar fixed-step primal-dual update and its two-by-two iteration matrix, then computing its trace, determinant, and discriminant directly. The spectral-radius formula in the conjugate-root regime follows from the determinant. In the real-root regime the derivative of the larger root was checked symbolically and its sign proved analytically.

The accompanying checker verifies the matrix identities and tests the monotonicity around the critical value over a deterministic grid. These numerical checks are supporting evidence only; they are not used as a proof for the continuum of parameter values.

The source-side scope was checked against the 2016 Malitsky--Pock algorithm and fixed-step condition, and against the 2024 Fercoq quadratic PDHG spectral-radius formulation. Independent audit has not been performed.
