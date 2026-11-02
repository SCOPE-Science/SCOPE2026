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

The exact recurrence and boundary formula were checked with the companion `verify.py` in standard Python 3. The run evaluated the divisor recurrence through \(16384\), checked the original defining floor recurrence through \(512\), verified \(563\) positive boundary cases and \(624\) zero-tail cases.

```
VERIFY_OK limit= 16384 floor_crosscheck=512 odd_parts_with_boundary= 563 exact_boundaries= 563 zero_tail_checks= 624
EXAMPLE 1 omega= 0 boundary= 4 value= 2 next= 0
EXAMPLE 3 omega= 1 boundary= 24 value= 8 next= 0
EXAMPLE 9 omega= 2 boundary= 144 value= 32 next= 0
EXAMPLE 15 omega= 2 boundary= 240 value= 128 next= 0
EXAMPLE 27 omega= 3 boundary= 864 value= 128 next= 0
EXAMPLE 45 omega= 3 boundary= 1440 value= 768 next= 0
EXAMPLE 105 omega= 3 boundary= 3360 value= 4608 next= 0
```

The infinite assertion is justified by the formal Dirichlet-convolution proof and its support restriction, not by finite enumeration. No independent validation is claimed.
