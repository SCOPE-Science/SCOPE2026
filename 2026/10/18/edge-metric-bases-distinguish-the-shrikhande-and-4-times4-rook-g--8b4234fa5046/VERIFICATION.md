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

## Reproducibility
Execute `python3 verify_edge_metric.py` with a standard Python interpreter. The script must finish with one `VERIFY_OK` line for each of the Shrikhande and rook graphs, and must raise no failed assertion. It reconstructs exactly the labeled 16-vertex graphs, their 48 edges and distances, and every edge-pair separator. For each candidate landmark set below and at the winning cardinality, it compares two independently implemented edge-resolution tests. It then constructs the full graph automorphism groups (with a separately checked upper-bound argument), partitions bases into orbits, and checks all swap-neighbor relationships, degrees, component sizes and representative masks.

## Verification boundaries
All statements proved by the program are finite equalities or exhaustive graph properties at order 16. It does not certify any uniform result for an infinite graph family. The original finite certificate is the runnable code and its computations, not a previous run log. External independent audit has not been performed.
