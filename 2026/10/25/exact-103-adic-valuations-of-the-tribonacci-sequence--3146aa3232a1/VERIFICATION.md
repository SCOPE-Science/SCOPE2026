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

The reproducible script `verify.py` uses exact integer arithmetic modulo \(103^8\), verifies the seventeen-step companion-matrix congruence, the exceptional initial terms, negative-index zeros, and the stated valuations for all positive indices below \(30000\). Run `python3 verify.py` in the extracted package directory. The full proof is in RESULT.md; finite testing alone cannot establish the infinite claim. No independent audit is represented here.
