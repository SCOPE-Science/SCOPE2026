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

# Verification

The mathematical argument in `RESULT.md` covers all integers at least three and all permitted nonnegative real length weights. Independently, run `python3 check_weighted_cyclic.py` with Python 3 standard library to enumerate every proper cyclic subset at dimensions 3 through 9 using exact rational arithmetic. The observed output is:

```text
PASS: 770 exact profiles across n=3..9
PASS: 333 positive profiles have exactly n maximal subset ratios
PASS: all discrete filtration values and final-step anomaly
```

This checker recomputes subset-minimum supports from the individual tube generators and compares them with the claimed formula; it does not prove any assertion about arbitrary dimensions or weights. The analytical proof separately establishes global optimality and center uniqueness. Full priority searching and independent mathematical auditing have not been performed.
