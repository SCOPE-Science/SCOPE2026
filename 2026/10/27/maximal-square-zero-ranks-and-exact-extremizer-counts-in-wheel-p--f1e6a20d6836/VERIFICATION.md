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

The general statement is proved by disjoint-domain/image geometry and cyclic path-run enumeration in RESULT.md. The standalone script `wheel_squarezero_checker.py` enumerates domain/image pairs and directly tests all graph-metric isometries of the required ranks, rather than using the run formula to generate examples. Recorded exact output is in `wheel_squarezero_check_output.txt`.

The direct checks cover all wheel rim sizes \(4\le n\le12\), with \(20{,}936\) maximum-rank square-zero elements in total, and independently rule out rank \(3\) for \(n=5\) and rank \(4\) for \(n=7\). Coefficient-formula evaluations additionally cover \(13\le n\le25\), but these last computations are **not** independent proof checks. No finite experiment alone establishes the result for unbounded \(n\). No independent audit has been performed.
