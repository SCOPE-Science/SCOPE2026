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

The theorem is proved symbolically from an explicit basis calculation, full classification of four-parameter products, and an exact three-to-two factor reduction. The standalone `verify.py` independently enumerates characteristic-two operators by actual \(2\times2\) matrix arithmetic, not by the four-parameter classification formula.

Command: `python verify.py`

Observed output:
```
GF(2): generators=8, twofold=30, monoid=34, ranks={2: 19, 1: 13, 4: 1, 0: 1}; VERIFY_OK
GF(4): generators=64, twofold=892, monoid=908, ranks={1: 123, 2: 783, 4: 1, 0: 1}; VERIFY_OK
```

The program verifies the rank counts and closure under multiplication by all generators in the checked fields; it does not verify the result for infinite fields or all finite fields by enumeration. Exact symbolic steps in RESULT.md establish the general claim. Independent external mathematical review has not been performed.
