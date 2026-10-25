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

# Verification and limits

`python3 verify.py` uses only the standard Python library and enumerates each symmetric-group conjugacy class for graph orders three through six (26 classes). It computes the signed trace of each automorphism on the augmented simplicial Euler complex via edge orbits and compares with the formula for top homology. It also uses exact binary Gaussian elimination to check reduced mod-two homology for graph orders three, four and five. Successful output:

`SIMPLE_COMPLETE_HIGHER_MATCHING_EQUIVARIANT_VERIFIED 26 conjugacy_classes n_3_to_6 mod2_n_3_to_5`

The finite calculations do not prove the representation formula for arbitrary order or distinguish integral group lattices. That content follows from the equivariant integral nerve/dual proof in `RESULT.md`. No independent audit was performed.
