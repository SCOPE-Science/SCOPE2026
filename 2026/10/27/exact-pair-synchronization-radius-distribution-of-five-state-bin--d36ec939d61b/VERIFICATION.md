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

The source files `forward_levels.cpp` and `reverse_bfs.cpp` each enumerate the complete \(5^{10}\)-element space of ordered binary transition tables on five labeled states. They use different shortest-path computations: successive predecessor levels versus multi-source reverse breadth-first search. `reproduce.sh` compiles the two programs, checks all ten frequencies in `pair_radius_counts.csv`, checks the nonsynchronizing total, and verifies the radius-ten relabeling-and-letter-swap orbit. `check_witness.py` independently checks all ten prescribed-pair distances, a length-ten witness, and its stated state relabeling.

Actual replay from the packaged source directory returned `WITNESS_OK` followed by:

`VERIFY_OK: two complete enumerations agree with the exact distribution and orbit check`

Both implementations returned \(8{,}063{,}385\) synchronizing and \(1{,}702{,}240\) nonsynchronizing automata. The extremal orbit equals the full set of \(240\) radius-ten automata. The finite proof consists of the exact ten-pair recurrence and complete coverage of every pair of five-state maps; no sampled search or timeout is treated as an infinite proof. Independent external validation has not been performed.
