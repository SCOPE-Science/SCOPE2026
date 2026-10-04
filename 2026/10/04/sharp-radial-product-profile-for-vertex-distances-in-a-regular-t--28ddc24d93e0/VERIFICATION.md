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

The analytic proof establishes the infinite theorem. The bundled `verify.py` is a deterministic consistency replay using a unit-circumradius coordinate model of the regular tetrahedron. It checks a fixed radial grid plus seeded random directions against the two sharp bounds, checks every vertex and opposite equality ray, and checks the three branch-difference polynomial identities exactly using rational arithmetic.

The packaged run reports:

- `VERIFY_OK`
- `checks 49384`
- `max_normalized_bound_violation 7.772e-16`
- `max_normalized_equality_error 1.928e-15`
- `max_normalized_branch_factorization_error 0.000e+00`

Finite samples are not used to prove the global extrema. The global step is the Lagrange-multiplier classification plus exact factor comparison in `RESULT.md`. No higher-dimensional claim is verified or asserted.
