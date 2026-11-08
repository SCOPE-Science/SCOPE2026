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

# Reproducibility

Run `python3 verification/verify_split_direct.py` to reproduce the direct labeled-state checks and `python3 verification/verify_split_occupancy.py` to reproduce a second enumeration using the exact occupancy inequalities. The corresponding files `verification/split_direct_output.txt` and `verification/split_occupancy_output.txt` are the recorded standard outputs. The first checker iterates over the full binary state space for every graph size it reports, examining 1,206,956 states in total. The second checks 500 integer pairs by exact binomial arithmetic. Neither finite computation replaces the universal classification proof in RESULT.md. All reported checks concern fixed states at time zero and do not claim independent mathematical validation.
