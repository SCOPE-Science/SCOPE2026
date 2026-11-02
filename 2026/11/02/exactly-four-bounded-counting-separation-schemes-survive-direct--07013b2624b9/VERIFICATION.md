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

Run `python3 checker.py` using Python 3. No third-party packages are required.

The checker exhaustively tested all 1,016 Boolean truth tables for counting cutoffs two through eight; 988 generated a finite nonrectangular mixed-corner witness and 28 were the four admissible tables at each of seven cutoffs. It further verified 1,728 three-coordinate cardinality configurations and three explicit four-member counterexamples.

Observed terminal lines:

```
CUTOFFS_2_TO_8_OK masks= 1016 witnessed= 988
THREE_FACTOR_OK tuples= 1728
EXPLICIT_4_MEMBER_WITNESSES_OK
ALL_CHECKS_OK
```

These tests certify the stated finite calculations only. The universal theorem follows from the separate product-box and multiplicative-eventual-constancy proof in `RESULT.md`. The argument is conditional on a set-sized model of ZFC. Historical literature not completely inspected may contain equivalent results. Independent audit has not been performed.
