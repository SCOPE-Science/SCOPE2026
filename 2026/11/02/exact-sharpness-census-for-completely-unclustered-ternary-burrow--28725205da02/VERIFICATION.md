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

# Verification of finite sharp unclustered BWT images

The self-contained exhaustive enumerator `verify_enumeration.cpp` enumerates all `3*2^(n-1)` adjacent-unequal ternary images for every chosen `n` and applies the cited necessary parity condition, exact sorted-word Hamming comparison, and one-cycle standard-permutation test. Its run for lengths 13–30 yielded the counts in `witness_table.tsv`. Its input and output have no dependence on prior result packages.

A second independently written generator `verify_bitmask.cpp` chooses the starting symbol and a binary mask selecting one of the other two symbols at each step, then constructs the inverse stable permutation. It does not apply parity pruning, and its exact results matched every primary count for lengths 13–26. Its direct exhaustive recount was not completed for lengths 27–30.

`verify_witnesses.py` separately reconstructs a primitive source via sorted-row inversion and recomputes the ordinary BWT from all its cyclic rotations; it also tests the cyclic input run count. All 18 displayed witnesses passed. A third small direct enumeration gave exactly four length-14 witnesses as listed in `n14_four.txt`.

This is exhaustive verification only for finite lengths. There is no proof for lengths outside 13–30 and no independent mathematical audit.
