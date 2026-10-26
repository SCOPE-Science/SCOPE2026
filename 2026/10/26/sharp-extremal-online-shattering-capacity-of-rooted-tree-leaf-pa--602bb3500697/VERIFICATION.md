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

The all-order proof is in `RESULT.md`. Its key step is the distinctness of decision-query vertices across any shattered adaptive tree, due to nesting/disjointness of descendant-leaf sets. This yields a nonleaf-vertex count not furnished by the ordinary hypothesis-count bound.

The standalone file `verify_leafpath_extremal.py` uses an exact recursive game calculation on every unlabeled rooted tree up to twelve vertices and checks the maximum independently for each feasible parameter pair. It additionally constructs and checks full shattered-tree witnesses through depth five. Its recorded output is `verify_leafpath_extremal.out` and ends in `ALL_EXACT_CHECKS_PASS`. The exact game recursion was not used to prove all depths; the proof uses a laminar non-repetition lemma and recursive grafting.

Reproduction: `python3 verify_leafpath_extremal.py` using Python 3 and its standard library. Verified source and log are embedded alongside this document. The independent audit is not performed.
