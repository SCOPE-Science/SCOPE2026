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

Run `python3 verify.py` in this directory with standard Python 3. It checks all 105 published-normal-form candidates against all seven proved identities in words of length at most ten and verifies exactly 35 connected congruence classes; it checks all 35 proposed normal forms are present as distinct classes. It then validates two explicitly encoded four-world birelational frames and checks that all 35 representative operators have distinct semantic signatures across their 24 admissible valuations.

Expected output:

```
UPPER_NORMAL_FORMS=35
FINITE_WITNESSES=35
VERIFY_OK
```

A separate small-size enumeration performed as a stress test checked 457 admissible ordered three-world frame pairs and all upward-closed valuations for all seven word equations. The construction of the infinite-model upper bound uses sound equations and Pacheco's published reduction. Finite tests alone would not establish an infinite-frame theorem. No independent audit has been performed.
