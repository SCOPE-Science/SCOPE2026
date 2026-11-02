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

The standalone `verify.py` enumerates every exponent-injection state using integer subset masks, and independently `verify.cpp` iterates every permutation of ten exponents. Both compute the five distribution counts and check equality with 3,628,800 total assignments. Both were run successfully against these packaged source files. No assumption concerning higher moduli was tested or claimed.
