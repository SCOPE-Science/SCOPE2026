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

The claim concerns all paths with 0 through 15 edges, including the 0-edge and 1-edge boundary cases. The two source checkers independently enumerated complete inclusion-maximal matching classes and reproduced the exact minimax dimensions. The included `shattered_trees.json` contains all depth-optimal shattered-tree certificates, verified at every leaf against actual hypothesis masks. The 15-edge upper bound also has a separate three-query-level counting obstruction checked from all 65 hypotheses in `maximal_matchings_15.txt`. Reproduction: run `python3 verify.py` and `c++ -std=c++17 -O2 independent.cpp -o independent && ./independent` from this directory.

No dimension formula for paths with more than 15 edges, an independent external audit, or exhaustive historical-priority verification is claimed.
