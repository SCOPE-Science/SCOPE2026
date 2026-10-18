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

A self-contained deterministic finite-state certificate is in `verify.py`; execute `python3 verify.py`. It checks the exact recurrence for multiplication by 289 in base three, the reachable 32 carry states, the closed 12-state trap, the 20 live carry-to-history assignments, every live transition, the 26 safe edges, and an explicit nontrivial polynomial identity. It also checks 187 bounded accepted walks through 24 transition steps as supplementary regression tests.

The all-degree proof uses finite-state closure and local transition invariants; the bounded-walk tests are not used to infer an infinite claim. Checks were run using Python 3 without external mathematical libraries. Independent audit: not performed.
