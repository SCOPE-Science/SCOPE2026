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

The analytic proof establishes every positive rate, positive duration, and integer return-cycle count. `verify.py` uses only Python's standard library to perform composite Simpson integration of the conditional tilted-beta density. It checks the equal-rate exact moments, strict regression decreases for representative parameters at or below the threshold, and an eventual reversal above threshold. The finite set of numerical checks is not an infinite proof or independent audit.
