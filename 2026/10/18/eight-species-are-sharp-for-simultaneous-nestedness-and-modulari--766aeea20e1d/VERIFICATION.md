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

# Exact checks and limits

Execute `python verify.py` (Python 3.9+, no additional dependencies). The script enumerates all labeled binary incidence matrices for two nonempty guilds with total vertex count from three through seven, retains connected graphs and connected outcomes of degree-preserving two-by-two swaps, and computes exact normalized NODF and maximum Newman–Girvan modularity.

The modularity maximization recurrence considers every set partition: fix the least vertex in the current subset and enumerate its complete block. The proof of this recurrence is in `RESULT.md`. At the only nontrivial small guild sizes, it identifies 205 connected three-by-three matrices with 216 directed valid swaps and 1795 connected three-by-four matrices with 4320 directed valid swaps. No swap raises both metrics; 576 directed three-by-four swaps strictly change both in opposite directions.

For the three-by-five witness, exact NODF values are `5/13` and `11/26`; exact maximum modularities are `9/32` and `39/128`. An independent restricted-growth-label enumeration evaluates all 4140 partitions for each eight-vertex witness, confirming optimality. No probabilistic trials or floating-point comparisons are used.

The classification is limited to the exact graph sizes, metric definitions, and connectedness conditions specified; no independent review of proof or source novelty is asserted.
