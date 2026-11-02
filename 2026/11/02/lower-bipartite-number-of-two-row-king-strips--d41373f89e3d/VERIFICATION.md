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
Execute `python3 verify_kings_strip.py`. It uses only the Python standard library. The expected final marker is `VERIFY_OK graph_orders=8 graph_subsets=87380 occupancy_orders=12`. The code constructs king-graph adjacency directly and exhaustively checks 87,380 vertex subsets over lengths one through eight. A separate occupancy-word enumerator checks all words through length twelve. The unrestricted result rests on the proof and no independent audit has been performed.
