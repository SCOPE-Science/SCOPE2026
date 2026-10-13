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

The proof uses three algebraic steps that do not depend on computation: recovering the unique floor/ceiling maps, excluding all other shapes of their common core, and constructing maps satisfying all five identities for the two shapes. The count uses independent subset choices and Vandermonde's identity.

The accompanying `farl_twochain_verify.py` evaluates the axioms directly on finite tables. It enumerates all possible core subalgebras for carrier sizes \((2,2),(2,3),(3,3),(3,4),(4,4),(3,5)\). It independently enumerates candidate left adjoints as join-preserving maps on axis generators for \((2,2),(2,3),(3,3),(3,4)\), then constructs the right adjoint from the Galois condition. The latter route enumerates 16, 108, 1296, and 12000 candidates. The two methods reproduce the predicted rectangle and diagonal counts and output `VERIFY_OK`.

These finite verifications do not prove the general theorem. The theorem's unrestricted quantification is justified by the separate symbolic proof. Independent audit and independent validation are not performed.
