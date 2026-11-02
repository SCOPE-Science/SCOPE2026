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

# Reproducibility

Run `python3 verify.py` using Python 3.9 or later. It rebuilds the cycle prisms without third-party packages, tests the original initial-domination and subsequent unique-neighbor propagation rules on every singleton and unordered vertex pair for all cycle lengths from three through sixty, and checks both the cyclic-distance classification and exact counts. It prints `VERIFY_OK` on success. These exhaustive finite computations do not certify the infinite statement, whose mathematical proof appears in `RESULT.md`. Independent mathematical audit has not been performed.
