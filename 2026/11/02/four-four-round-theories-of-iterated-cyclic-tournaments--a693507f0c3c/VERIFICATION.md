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

# Computational and symbolic verification

`python3 verify/pair_matrix_types.py` enumerates pairwise first-disagreement/direction invariants and the exact sets of one-point-extension types, without orbit sampling. Its asserted root partition is `{1:1,2:2,3:3,4:4,5:4}` and it prints `FOUR_RANK4_CLASSES_AND_PUMPING_BASE_OK`.

`python3 verify/trie_orbits.py 4 5` independently canonicalizes ordered tuples under recursive ternary-child rotations rather than first-difference matrices. The five root class representatives agree and tuple-orbit counts agree at each tuple length. Both scripts and their scientific outputs in this package were executed from these exact paths with no external dependencies.

The all-height result is not inferred from scripts: the mathematical lexicographic-product congruence takes the finite equality at heights 4 and 5 to each pair of consecutive later heights. The lemma proving the pair-matrix code is a complete orbit invariant establishes the exhaustiveness of the finite calculations. No independent audit or external validation has been performed.
