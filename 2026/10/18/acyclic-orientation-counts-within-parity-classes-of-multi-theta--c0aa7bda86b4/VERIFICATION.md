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

# Reproduction notes

Execute `python3 verify.py` in the extracted package folder. This uses only Python's standard library and enumerates every orientation of each named test graph. It builds graphs independently of the closed expression, computes parity signatures by indegree accumulation, checks directed acyclicity by topological sorting, and compares the entire histogram with the formula.

Recorded check: 30 graph cases with three through eight internally disjoint paths; 159168 orientations considered, all comparisons passed. It also checks the global number of feasible signatures for each graph.

This is finite consistency testing, not proof for unbounded path lengths or widths. The unrestricted argument appears in `RESULT.md`. No independent audit was performed.
