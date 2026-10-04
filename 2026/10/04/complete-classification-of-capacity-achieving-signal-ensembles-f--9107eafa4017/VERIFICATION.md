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

The proof is analytic and rests on four checks: the output determinant identity; strict monotonicity of qubit entropy in determinant; strict convexity of \(g_p\); and the planar polygon closure criterion for weighted unit phasors. The recent capacity theorem is used only to identify the true capacity and its unique average input.

`verify.py` numerically corroborates the determinant formula and strict-convexity expression, locates \(q_*\) for representative damping probabilities, verifies that balanced binary, triangular and square phase constellations have the predicted Holevo value, and verifies that a mixed signal with the same excitation has strictly larger output entropy. These finite checks are not substitutes for the all-parameter proof.

Run:

`python3 verify.py`

Expected output:

`VERIFY_OK`

Unproved limits: no statement is made for endpoint damping, generalized amplitude damping, infinite signal measures, finite-error exponents, or decoder uniqueness.
