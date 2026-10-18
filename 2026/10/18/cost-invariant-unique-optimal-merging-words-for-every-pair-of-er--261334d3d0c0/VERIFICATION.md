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

Run `python3 verify_weighted.py`: direct construction of the pair transition graph, reverse Dijkstra shortest paths for all pairs and seven integer weight assignments for every size from 3 to 40, plus optimal-letter uniqueness and the unit-weight permutation of distances.

Run `python3 verify_bruteforce.py`: independent forward BFS from each pair for sizes 3 through 23, recording shortest-word multiplicities and witness letter counts.

Expected terminal markers: `WEIGHTED_VERIFY_OK` and `FORWARD_BFS_VERIFY_OK`. The arbitrary-positive-real-cost claim, exact all-size spectrum, and uniqueness for every size are proved algebraically in `RESULT.md`; finite replay cannot establish these universal statements. No independent external assessment is asserted.
