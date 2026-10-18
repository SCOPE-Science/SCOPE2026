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

# Reproducible finite checks

The complete proof of the lower bound and eight minimum-set classification is in `RESULT.md`. Both complete and separate deterministic checkers run on Python 3.10+ without nonstandard libraries.

- `check_edges.py`: integer vertex masks, xor-bit hypercube edges, union-find induced-forest certification, exhaustive enumeration over all 65536 subsets, adjacency graph and breadth-first connectivity/distance tests.
- `check_cartesian.py`: Gray-labeled Cartesian product of two 4-cycles, direct combinations of six to eight selected vertices, iterative leaf-pruning criterion for induced forests, independently constructed toggle graph, disjoint-set connectivity and breadth-first distances.

Recorded output files `check_edges.out` and `check_cartesian.out` are exact terminal standard outputs. Each contains the same JSON object and the final line `VERIFY_OK`. Both checkers explicitly validate the twelve-toggle representative path and verify that all states on that path satisfy the capacity and forest condition.

The checked finite universe includes every feedback set of sizes six, seven or eight on the sixteen labeled vertices; sets of cardinality at most five are ruled out by the analytic edge-count inequality. The programs do not claim any result for higher-dimensional hypercubes, and no independent external audit has been conducted.
