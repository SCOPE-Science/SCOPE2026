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

The accompanying `verify.py` was executed with Python 3 using only the standard library and returned `VERIFY_OK`. It independently enumerated all rank-two quotient kernels of binary vector spaces of ranks 2–5, giving 1, 7, 35, and 155. For ranks 2 and 3 it also enumerated all binary subsets of each group and checked that every index-four subgroup has exactly two exact-stabilizer translation orbits, each of size four and arising from weights one and three in the quotient.

The general double-coset and generation statements are established by the six-step analytic/group-theoretic proof, not by finite computation. Critical cited ingredients are finite-equivariant-map generation by elementary collapses, unit-double-coset rigidity for diagonal collapses, and the known lazy-generation exception classification. No computational test addresses every finite group or proves literature originality. Independent audit has not been performed.
