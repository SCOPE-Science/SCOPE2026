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

Execute `python verify_paired_prisms.py` with Python 3.8 or later. The script constructs each graph on \(2n\) vertices with two cliques and the \(n\) matching edges. For \(2\le n\le7\), it independently enumerates all candidate subsets of every even size, tests domination directly using graph neighborhoods, tests perfect matching in the induced subgraph with recursive backtracking and memoization, and compares each coefficient with the closed expression. The completed execution printed `VERIFY_OK`.

The mathematical proof is independent of the checker: it characterizes matchable dominating sets by layer parities and matched-column intersections; then counts all nonqualifying subsets by disjoint cases. The exhaustive check covers finite orders only and does not establish the theorem for arbitrary \(n\). External independent mathematical and priority audits are not performed.
