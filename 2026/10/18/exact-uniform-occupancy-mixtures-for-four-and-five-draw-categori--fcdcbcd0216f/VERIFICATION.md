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

The accompanying `verify_occupancy.py` recomputes the complete exact-rational certificate. For four draws, it checks all 35 degree-four weak compositions; for five draws, all 126 degree-five weak compositions, across every inverse-uniform-matrix weight. Every coefficient is nonnegative. The script independently enumerates labeled draw tuples for 13 rational test profiles and verifies the matrix reconstruction, total probability and nonnegative weights. Those finite test profiles are corroboration only; exhaustive polynomial-coefficient positivity is the proof of the continuum statement. Python 3 standard library is the only dependency. The argument does not cover a larger alphabet, more than five draws or joint partition processes. No independent audit has been performed.
