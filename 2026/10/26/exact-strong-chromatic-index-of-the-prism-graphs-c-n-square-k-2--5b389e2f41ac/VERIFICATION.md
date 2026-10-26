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
# Verification of the strong-edge-coloring formula

All checks are local, deterministic, and reproducible using Python 3 standard library.

From the folder containing these files, run `python3 construct.py` and `python3 exhaustive.py`. Compare standard output with `construct_output.txt` and `exhaustive_output.txt`, respectively. The first uses integer-labelled vertices and direct endpoint-adjacency tests. The second rebuilds the graph with pairs `(layer,column)` and a distinct edge-conflict graph implementation; it exhaustively enumerates all induced matchings at orders 3, 5, 6 and separately searches for low-color colorings.

These checks certify finite tables and test the insertion construction through order 100. The statement for all orders additionally requires the symbolic period-four lower bound and repeated four-column insertion proof in `RESULT.md`, not extrapolation. No independent external audit has been performed.
