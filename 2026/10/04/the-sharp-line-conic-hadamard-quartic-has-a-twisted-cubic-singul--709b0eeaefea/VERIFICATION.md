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

Run `python3 artifacts/verify.py` in an environment with SymPy. The checker uses exact integer and rational arithmetic and prints `VERIFY_OK` on success.

It verifies the two source parametrizations against the defining line and conic equations; substitutes the Hadamard parametrization into the complete quartic equation; substitutes the proposed twisted-cubic parametrization into all three quadrics; checks that its four coordinate cubics have rank four as binary cubics; verifies explicit linear-combination identities placing every quartic partial derivative in the three-quadric ideal; and computes an exact Gröbner basis of the Jacobian ideal to verify that the cube of each quadric reduces to zero.

These checks prove equality of radicals for the Jacobian ideal and the prime twisted-cubic ideal. The verification does not determine the nilpotent structure of the Jacobian scheme or classify local analytic types along the curve.
