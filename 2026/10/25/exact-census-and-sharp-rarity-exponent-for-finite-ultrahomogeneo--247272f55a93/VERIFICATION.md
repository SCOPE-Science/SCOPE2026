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

Run `python verify.py` with Python 3 and the standard library. The program recomputes the exact rational generating-function coefficients through degree 12, then enumerates all labelled unary maps on 1–6 vertices independently using the one-generated ultrahomogeneity criterion; it asserts equality and prints `UH_ENUMERATION_OK`. Expected positive coefficients are `1, 4, 15, 100, 575, 5526, 43967, 511064, 5396967, 73824130, 928413959, 15140851452`. Brute force covers 1+4+27+256+3125+46656 individual maps, not arbitrary finite size. The general classification is an explicitly cited mathematical input and is not independently proved by this checker. The analytic partition-majorant argument provides the infinite asymptotic bound and is explained in the proof; code is corroborative only. No external independent audit has been performed.
