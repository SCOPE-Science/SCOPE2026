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

The standalone `check.py` was run against the embedded formulas. Exhaustive prime-field matrix enumerations verify all cells at dimensions and field orders (2,2), (2,3), (2,5), (3,2), (3,3), and (4,2), including ranks zero and full dimension as boundary checks. Further integer-only checks verify positivity and total rank-fixed idempotent counts for n=2..8 and q=2,3,4,5,7,8,9. For extension fields the computations check arithmetic consequences; the finite-field identity itself follows from the proof's field-linear argument and is not inferred from those computations. No external/independent audit has occurred.
