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

# Verification notes

The theorem is analytically certified using the nonsymmetric John-contact theorem and the explicit formulas for the lateral, lower-cap, and upper-cap weights. The proof verifies normalization, feasibility, positivity, all moments, contact geometry, sharp transition, dimensional endpoints, and affine equivariance.

A separate executable program, `verify_homothetic_frusta.py`, was run on the final source, and printed `ALL_FRUSTUM_JOHN_CONTACT_AND_OPTIMALITY_DIAGNOSTICS_OK 70`. It checks dimension \(2\) through \(8\), regular-simplex and cube contact systems, and five axis ratios per dimension. These are finite numerical diagnostics and do not establish all-dimensional correctness or historical priority. The analytical proof supplies the general statement.

Independent audit has not been performed. No claim of independent certification is made.
