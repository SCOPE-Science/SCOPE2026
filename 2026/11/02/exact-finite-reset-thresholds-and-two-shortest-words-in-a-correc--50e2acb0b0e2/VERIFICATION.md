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

# Finite verification

For each integer parameter from 3 through 15, `forward_bfs.py` enumerated every distinct subset at each breadth-first layer until finding a singleton, counting all labeled paths of minimum length. `reverse_bfs.cpp` independently traversed the inverse-image graph from every singleton to the full state set, reproducing all thirteen thresholds and the multiplicity two. `witness_checks.py` confirmed that both distinct displayed words reset to state 2 at the minimal length in every case. The exact counts are listed in `counts.csv` and recorded in `verification_output.txt`.

These exhaustive checks cover a bounded finite family only; no extrapolation to larger parameters is justified. They do not constitute independent external auditing.
