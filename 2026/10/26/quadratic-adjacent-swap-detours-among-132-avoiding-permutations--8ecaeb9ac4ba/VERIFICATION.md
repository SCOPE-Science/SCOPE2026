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

# Verification notes

Run `python3 verify.py` using only the Python 3 standard library. The code constructs all \(132\)-avoiders recursively at each parameter, checks brute-force three-index avoidance for small sizes, computes every legal swap and its connected component, and compares the exact start-to-target BFS distance against the proved formula.

Executed full-graph checks for every integer \(2\le n\le10\) returned `VERIFY_OK`. At \(n=10\) the graph has \(16{,}796\) vertices and \(43{,}758\) edges; BFS finds canonical distance \(81\). The local move predicate is checked independently through \(n=7\).

These are finite consistency checks only. The proof in RESULT.md establishes the stated theorem for all \(n\ge2\) through the local legality criterion, the pair-crossing lower bound, the explicit attaining path, and the Catalan generating-function recurrence. Neither a full graph diameter formula nor all-pair distances are asserted.
