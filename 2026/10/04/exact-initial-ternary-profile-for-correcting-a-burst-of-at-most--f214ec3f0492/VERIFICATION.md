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

Run `python3 verify.py` with a standard Python 3 interpreter. The script enumerates every ternary word of lengths \(2\) through \(5\). For each source word it constructs every one-deletion and two-consecutive-deletion output by two independent routines and requires equality. It then builds the full compatibility graph, verifies the supplied attaining code, and executes an exact branch-and-bound maximum-clique search. A greedy proper coloring of each candidate-induced graph is used only as an admissible upper bound for pruning.

The replay must print clique optima \(1,3,7,13\) and terminate with `VERIFY_OK profile=1,3,7,13`. No output for a larger length is required or used. The computation is finite and exhaustive for the claimed range; it is not evidence about \(n\ge6\).
