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

The proof is analytic and covers every \(n\ge3\). The finite checker is corroborative.

`artifacts/verify.py` enumerates all labeled surjective colorings using one, two, or three colors for \(C_n\), for each \(3\le n\le12\). It tests the FAT neighborhood equalities directly using exact rational arithmetic, canonicalizes color names to unlabeled set partitions, computes the refinement partial order, and compares the resulting complete list with the theorem.

The analytic degree-two argument proves separately that no FAT coloring with four or more colors can exist, so restricting the finite search to at most three colors loses no candidate in the checked range.

Replay output:

`ALL CHECKS PASSED; n_range=3..12; labeled_colorings_checked=805342; FAT_partitions=25`

The per-order output also confirms irreducible counts \(1,3,1,2,1,3,1,1,1,4\) for \(n=3,4,\ldots,12\), respectively.
