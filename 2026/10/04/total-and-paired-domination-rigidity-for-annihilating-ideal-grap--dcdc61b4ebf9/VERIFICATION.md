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

The proof was replayed from the standalone `verify.py` artifact.

For each rank
\[
2\le r\le5,
\]
the checker constructs every nonempty proper support subset and joins two vertices exactly when the supports are disjoint. It verifies that every co-singleton has a unique singleton neighbor, then exhaustively enumerates all total dominating sets of size \(r\) and all paired dominating sets at the claimed minimum size.

Exact output:

```text
r=2 vertices=2 total_min_count=1 gamma_t=2 paired_min_count=1 gamma_pr=2
r=3 vertices=6 total_min_count=1 gamma_t=3 paired_min_count=3 gamma_pr=4
r=4 vertices=14 total_min_count=1 gamma_t=4 paired_min_count=1 gamma_pr=4
r=5 vertices=30 total_min_count=1 gamma_t=5 paired_min_count=25 gamma_pr=6
VERIFY_OK
```

The exhaustive checks corroborate the symbolic proof. The arbitrary-rank conclusion rests on the unique-neighbor forcing argument and explicit perfect-matching construction.
