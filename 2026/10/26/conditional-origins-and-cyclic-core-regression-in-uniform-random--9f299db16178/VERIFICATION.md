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

# Reproducibility and limits

The attached standalone standard-library script `verify_random_mapping_origins.py` was run from the extracted scientific package and returned `PASS 1086 checks`. It exhaustively enumerates 4, 27, 256, 3125, 46656, and 823543 mappings at dimensions 2 through 7, respectively; verifies the exact conditional factorial moments and a fixed-origin deletion identity independently, checks finite closed-form identities through dimension 40, and tests the asymptotic coefficient numerically at dimensions 500, 2000, and 10000. The printed asymptotic approximations were -0.2303813170783325, -0.23049593792521866, and -0.23052657810912933, compared with -0.23053425222394727.

All mathematical quantifiers and exceptional cases are proved symbolically in `RESULT.md`. A finite exhaustive census does not certify an infinite theorem or prove novelty. No independent audit has been performed.
