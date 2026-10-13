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
The arbitrary-field proof is symbolic.

The packaged checker `artifacts/verify.py` exhaustively tests
\[
\mathbf F_2,\qquad \mathbf F_3,\qquad \mathbf F_5.
\]

For each field it enumerates every bilinear second product on the two-dimensional vector space and directly tests the pre-Lie identity for \(*\) and \(\cdot+*\) on all ordered basis triples.

It verifies that the solution set is exactly the displayed algebraic locus, independently enumerates all automorphisms of the first product, and constructs every conjugacy orbit.

The verified counts are
\[
(10,7,4),\qquad (33,21,9),\qquad (145,85,25),
\]
where each triple records compatible products, automorphism classes, and singleton classes for \(q=2,3,5\), respectively.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the arbitrary-field equations or the formulas for general prime powers.
