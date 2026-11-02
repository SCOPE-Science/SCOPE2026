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

The accompanying Python 3 standard-library `verify.py` performs direct synchronous Rule-184 evolution on every nonconstant indexed cyclic word of lengths 2 through 16 (131038 states), separately computes gap-process first minima and strict extremal cuts, checks the exact Catalan counts at every density, enumerates Catalan strict-negative-prefix paths at small dimensions, and tests 5600 additional seeded random configurations on rings through length 101. The expected output begins with `VERIFY_OK`.

This is a finite numerical cross-check. The all-size proof is the min-plus/path/tree bijection in `RESULT.md`. The script is deterministic and needs no external files or third-party packages. The historical novelty assessment is a literature comparison, not an independent priority certificate.
