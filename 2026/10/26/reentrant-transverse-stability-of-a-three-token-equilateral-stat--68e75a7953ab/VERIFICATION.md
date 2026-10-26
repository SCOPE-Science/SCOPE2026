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
# Verification of the three-token equilateral stability boundary

Run `python3 verification/check.py` using only the Python standard library. The checker evaluates the actual three-token softmax/normalization update with positive self-edges, estimates angular derivatives along two independent zero-sum shapes and the neutral rotation, and compares to the exact analytic multipliers. It also brackets the unique maximum of the scalar stability function and its two threshold intersections, checks the sign patterns for several residual steps, and verifies a rational form of the factorization used in the proof.

The checked finite parameter samples and numerical difference quotients do not certify the universal mathematical theorem. That theorem is proved by the full softmax derivative, scalar factorization and monotonicity argument in RESULT.md. The critical boundaries are not classified nonlinearly. Independent audit: not performed.
