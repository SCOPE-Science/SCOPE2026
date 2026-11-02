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

# Reproducibility and scientific limits

Run `python3 verify_direct.py` with Python 3. The script constructs each finite simple theta graph, enumerates every oriented edge-sign mask, rejects cyclic directions by an independent topological sort, and checks every one-edge reversal with the same DAG test. For 64 small admissible path-length vectors, compare the full degree histogram against the symbolic product formula and the exact minimum-degree multiplicity. A successful run prints `GENERAL_THETA_DIRECT_CHECK_PASS cases= 64`.

Run `python3 verify_word_and_trees.py`. This separate program enumerates words with no contradictory full terminal paths, counts blocked edges by word patterns, and enumerates spanning trees using deletion edge-subsets and union-find. It checks the asserted polynomial and simple-vertex/spanning-tree identity in 11 cases, including a direct terminal edge. A successful run prints `WORD_AND_SPANNING_TREE_PASS cases=11`.

The finite tests do not certify the infinitely quantified theorem; the written mathematical proof does that. They also cannot establish historical priority. The referenced sources substantiate foundational definitions and comparisons, not independent verification of the proposed claim.
