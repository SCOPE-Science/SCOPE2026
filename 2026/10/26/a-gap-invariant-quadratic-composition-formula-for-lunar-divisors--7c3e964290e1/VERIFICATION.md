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

The included `verify.py` enumerates every possible divisor support for small instances and checks whether the maximal admissible cofactor produces the target. It also independently computes the formula from bounded-part composition recurrences and checks the sharp exceptional \(h=2,n=2\) case.

To replay: `python3 verify.py`. Exact arithmetic only; no external packages. The proof of the universal identity is in RESULT.md; finite checks do not establish it for all \(h,n\).
