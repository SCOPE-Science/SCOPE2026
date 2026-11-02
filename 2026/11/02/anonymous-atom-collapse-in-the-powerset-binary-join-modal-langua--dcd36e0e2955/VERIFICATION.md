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

The proof is constructive and covers every finite \(n\ge1\) and \(0\le k\le n\). `checker.py` independently computes modal partition refinement and checks the back condition for every \(n\le5\). It does not constitute an independent mathematical audit or a proof for unbounded carriers. The source-comparison limits are described in `REVIEW.md`.
