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

## Exact checks
`CHECK.py` performs polynomial arithmetic modulo seven, verifies the quartic and dual equations on the parametrizations, checks the tangent cross product and ramification gcd, and computes the off-diagonal collision Gröbner basis. It confirms the uniqueness of the preimage at infinity. The test succeeds with `VERIFY_OK`.

## Mathematical limits
Formal analytic classification and completeness use the geometric injectivity, normalization theorem and arithmetic-genus formula in `RESULT.md`; no finite-field sample is asserted to be a proof over the algebraic closure. Full-text inspection of all classical literature was not possible. There has been no independent scientific audit.
