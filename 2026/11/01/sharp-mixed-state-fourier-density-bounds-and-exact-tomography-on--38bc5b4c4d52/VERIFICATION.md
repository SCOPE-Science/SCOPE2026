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

# Verification record

The proof is self-contained in `RESULT.md`. The finite checks in `CHECK.py` require only Python 3 standard library and cover primes 3, 5, 7, 11, 13, 17, 19 for the difference map; primes 3, 5, 7, 11 for finite positive semidefinite examples and projector endpoints; and primes 3 and 5 for the exact Hermitian-to-real Gram spectrum. The checker produced `CHECK_OK assertions=1915` after extraction from the saved finding package.

The finite tests are supplementary only. Field-uniform validity follows analytically by finite-field difference inversion, additive-character orthogonality, and orthogonal decomposition. The results do not extend to characteristic two without a separate argument. Equivalence or priority relative to all unindexed literature has not been independently established.
