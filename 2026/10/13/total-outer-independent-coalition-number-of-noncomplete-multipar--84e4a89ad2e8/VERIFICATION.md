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
The analytic proof is the primary evidence. The accompanying `verify.py` reconstructs total outer-independent domination and coalition partitions directly from adjacency.

The checker exhaustively verifies every noncomplete complete-multipartite part-size profile of total order at most \(8\) with at least three parts. For each profile it checks the TOIDS characterization for every vertex subset and enumerates every set partition to confirm that the maximum valid TOI-coalition partition has exactly \(3\) blocks. It also checks the explicit three-block construction on all noncomplete profiles of total order at most \(30\).

These finite checks cannot prove the theorem for unbounded part sizes; the infinite result rests on the symbolic characterization and partner-case argument in `RESULT.md`.
