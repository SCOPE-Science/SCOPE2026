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

# Mathematical verification and limits

The checker `nil_clean_fibers_checker.py` was run with Python 3 from its actual package contents; it finished with `NIL_CLEAN_FIBER_EXHAUSTIVE_OK`. Complete matrix/idempotent enumeration was performed over finite fields of orders \(2,3,4,5,7,8,9,11\); examples include nonprime fields constructed as explicit irreducible-polynomial quotients. Each \(h_q(A)\) and the coefficient histogram were compared with the theorem, and each conic point count was independently enumerated. These tests are exhaustive only for the eight displayed fields, not for all finite fields.

The proof applies to all finite fields because it uses only trace, determinant, rank-one idempotent structure, the elementary classification of two-dimensional characteristic polynomials, rational points on a smooth conic, and quadratic splitting counts. Its critical conditions include the scalar exception when trace is one, the disjoint zero-/identity-idempotent branches, and the degeneration at determinant zero. All characteristics, including two, are covered by the stated calculation.

The result does not assert a higher-size nil-clean-index formula, nonfield generality, or strong/weakly nil-clean counts. Some publication-priority sources remain only partially accessible. Independent mathematical audit and external validation have not been performed.
