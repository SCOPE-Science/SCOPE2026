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

# Reproducibility and scope

Install the dependency specified by `requirements.txt`, then run `python check_neighbor_augmentation.py` and `python check_leaf_block.py` from this directory. Both programs assert the unrooted counts `[1,1,2,4,9,23,63,188,596]` and failure counts `[0,0,0,0,0,0,0,0,1]`. The first enumerates by adding a new vertex with every possible nonempty neighbourhood and filters for cacti; the second attaches leaf edges and leaf cycles. A removable-vertex argument and a leaf-block argument, respectively, prove completeness. Both use exact isomorphism to deduplicate unrooted graphs, but the first tests root-preserving orbit membership by pointed graph isomorphism and the second by a separate exhaustive adjacency-preserving bijection search.

The captured outputs in the two `.txt` files were obtained by running these actual code files. The nine-vertex witness can also be verified directly from the three-cell equitable partition and the four rooted automorphism orbits in `RESULT.md`. The computer checks establish the finite result, not any all-orders extension. They do not certify bibliographic priority or constitute independent scientific audit.
