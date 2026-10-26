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

The proof uses the exact word adjacency rule, base-clique domination, the unique bridge for a word with unequal last two symbols, and a block-by-block comparison. The lower-bound excess for a superblock with one empty base clique is exactly \(k-1\) above its nominal \(m(m-k)\) selected vertices. For the upper bound, negative-symmetric residues ensure linking-edge membership agreement.

Execute `python3 verify.py` from the directory containing this file. The standalone checker requires only the Python standard library. In the recorded execution it reported `VERIFY_OK construction_parameter_cases= 31 enumerated_candidate_masks= 263568 block_inequality_cases= 1225`. It reconstructs graph edges independently, tests explicit candidate sets in selected orders, and excludes strictly smaller solutions by exhaustive enumeration for the indicated small instances.

Finite enumeration does not establish the unbounded theorem, and the recorded checks do not enumerate all minimum configurations in arbitrary dimensions. No independent mathematical audit or formal proof assistant was used.
