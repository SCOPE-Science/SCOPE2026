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

# Reproduction of exact computational checks

Run `python3 verify_johnson_cut.py` using the Python 3 standard library. The script independently builds the adjacency of the actual Johnson graph and the two-coordinate cut, rather than reusing the exterior-algebra proof's incidence operators. It checks all 75 instances with \(4\le n\le13\) and \(1\le k<n\), using finite-field bitset elimination. It also builds graph-state amplitudes from the graph edges in seven small instances, exactly traces out one subsystem, and checks the integer-scaled idempotence and normalization of the reduced matrix. The correct final sentinel is `VERIFY_OK`.

Successful execution prints `CUT_RANK_TESTS 75`, `EXACT_GRAPH_STATE_DENSITY_TESTS 7`, and `VERIFY_OK`. The all-parameter statement is proved algebraically in `RESULT.md`; finite enumeration cannot validate unbounded values by itself. Historical priority against inaccessible older rank literature remains uncertain. No independent audit or external certification was performed.
