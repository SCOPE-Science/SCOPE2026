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

The included standalone `verify.py` was executed with Python 3. Its output was:

```
EXTERIOR_SPLIT_PROFILE {11: 72, 14: 648, 16: 2052, 17: 864, 18: 432, 26: 12}
ON_CURVE_SPLIT_PROFILE {39: 72, 40: 9}
LINE_SECTION_PROFILE {0: 1080, 1: 1953, 2: 72, 3: 1056}
F4_OUTSIDE_EXTREMALS 12
VERIFY_OK
```

The program asserts field irreducibility, group-law-independent geometric incidence counts, line-intersection root counts, equality of two exhaustive per-center implementations, incidence double counts and the exact pointwise subplane characterization. Its validity is for the particular finite field only. Independent audit has not been performed.
