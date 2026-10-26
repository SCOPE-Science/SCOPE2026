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

# Verification and limitations

Run `python3 verify.py` with the standard Python 3 library, in a directory containing this file's accompanying standalone source. The checker reproduces independently the exact counts for \(3\le n\le12\) by enumerating Eulerian tours of the full edge-labeled overlap graph and by computing integer cofactors of the contracted digraph. It also computes original-graph cofactors for \(3\le n\le10\) and independently enumerates all raw binary circles for \(3\le n\le6\). Each tour is checked against the exact allowed factor dictionary. A passing execution ends with `VERIFY_OK`.

These finite calculations are cross-checks only. The all-length claim is proved by the contraction, BEST theorem, directed matrix-tree theorem and a Fourier factorization, including the \(n=3\) boundary case, in `RESULT.md`. The earlier literature comparison leaves an unindexed-priority risk. No independent audit or validation is claimed.
