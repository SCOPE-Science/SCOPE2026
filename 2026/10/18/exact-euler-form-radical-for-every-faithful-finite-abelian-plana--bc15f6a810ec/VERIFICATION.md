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

The proof uses the precise signed translation formula and finite-character duality; it covers all nontrivial faithful finite abelian planar actions, with no finite-size assumption. The modular exact checker `verify.py`, run under Python 3 with SymPy, reported:

`VERIFY_OK faithful_action_profiles=31925 exact_matrix_rank_checks=30`

It independently constructs 30 integral Hessians and checks their exact rational nullity. The remaining finite tests compare two independently implemented descriptions: the closed group-order formula and enumeration of individual modular Fourier zero factors. Tested cases are evidence for detecting indexing mistakes, not a proof of the universal character-duality claim.

Independent audit is not performed. The claimed lack of indexed overlap is not a uniqueness certificate; previously unpublished or unindexed treatments of related signed Cayley graph forms could cover the result.
