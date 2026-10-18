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

# Reproducibility

Run `python3 quandle_medial_verify.py` with Python 3 (standard library only). The checker enumerates every marked permutation for sizes two through seven, forms explicit derived-group orbits by generators, checks orbit-splitting from pointed cycle decompositions and both closed count expressions, constructs the original quandle operation, checks representative-independence and the four-variable medial law on the quotient, and prints the resulting six cardinalities and `VERIFY_OK`.

The checker does not enumerate infinite groups or prove the general theorem. Those parts are proved by the displacement-orbit universal property and the stabilizer/Burnside arguments in RESULT.md. Exhaustiveness of each finite computation follows from the enumerator iterating all permutations and all distinguished points, not from sampling.
