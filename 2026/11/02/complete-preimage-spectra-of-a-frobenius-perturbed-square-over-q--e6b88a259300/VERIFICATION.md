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

# Verification record

The included `verify.py` enumerates finite-field targets using an explicit quadratic basis. It compares the observed multiplicity histogram to all five asserted formulas, for prime base fields and three genuine quadratic prime-power base fields. This uses an independently evaluated coordinate polynomial rather than the group-theoretic counting proof.

Run with `python verify.py` (Python 3, standard library). Executed result:

```
VERIFY_OK cases=19 total_inputs=19859 total_image_points=12419 four_fibers=749
TESTED_BASE_FIELD_ORDERS 3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,9,25,49
```

The proof treats every odd prime power and is not an extrapolation of this finite census. The literature comparison is nonexhaustive, and no independent scientific audit is claimed.
