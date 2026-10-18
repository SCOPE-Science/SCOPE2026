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

# Verification and its limits

`check_small.py` enumerates every unlabelled connected block graph of orders 1 through 9 by clique amalgamation and exact deduplication; all singleton-root placements have the same stable-colour partition as the explicit colour-preserving automorphism orbits. Random additional original colours with the root still unique also pass. Unmarked testing finds exactly one failing block-graph class up to order eight. Output is in `check_small_output.txt`.

`check_block_tree.py` independently constructs 1,200 random connected block graphs on 2 through 80 vertices, compares standard vertex-graph refinement to rooted block-incidence-tree refinement, and checks the induced vertex partitions coincide. Output is in `check_block_tree_output.txt`.

**Reproduction:** Install NetworkX 3.5 in a Python 3 environment, then run `python check_small.py` and `python check_block_tree.py` in the directory containing the scripts. Both programs have fixed seeds. The structural proof in RESULT.md covers the infinite theorem; no finite enumeration is asserted to be an exhaustive proof of it. Source precedence and literature completeness remain independent questions.
