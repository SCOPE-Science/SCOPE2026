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

# Verification details

The analytical proof works for arbitrary compact operators on real or complex infinite-dimensional \(\ell_p\) with \(2<p<\infty\). The key steps are exact: the two-coordinate \(p\)-sum normalization, duality-map decomposition, compact adjoint limit, scalar one-variable maximum, and rank-one witness. The attached `CHECKER.py` independently replays finite-dimensional identities at representative exponents; that is a consistency check, not a certificate for the infinite-dimensional theorem.

The proof does not claim extension to \(1<p<2\) or to arbitrary noncompact operators. Earlier exact-solution classification has been acknowledged and does not constitute the new result. Literature comparison does not certify historical uniqueness. No independent audit has been performed.
