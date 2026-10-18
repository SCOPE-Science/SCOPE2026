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

# Reproducibility and limits

Run `python3 verify.py` with Python 3 and no external packages. The program enumerates all integer partitions representing complete multipartite graphs on \(2\) through \(8\) labeled vertices with at least two nonempty parts. It independently constructs their edge sets, enumerates disjoint-edge subsets, expands the corresponding products of linear differences, and obtains exact ranks modulo \(1000003\) through sparse Gaussian elimination.

Expected output:

```
VERIFIED_MULTIPARTITE_CASES 58
VERIFIED_DEGREES 217
VERIFIED_ZERO_DEGREES 20
MAX_RECORDED_SPECHT_RANK 28
VERIFICATION_OK
```

The finite modular computations corroborate the ranks and the maximum-matching cutoff in the specified finite window. A rank at the known upper bound modulo a prime guarantees the corresponding rational rank, but no modular computation for finitely many profiles proves the infinite theorem. The infinite argument is the within-part-edge induction and elementary multipartite matching construction in `RESULT.md`. The graded duality and complete-graph Specht dimension are established prior results, not independently certified by the script. No external independent audit has been performed.
