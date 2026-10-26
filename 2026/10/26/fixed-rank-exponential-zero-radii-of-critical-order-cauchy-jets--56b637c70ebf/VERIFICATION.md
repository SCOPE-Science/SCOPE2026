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
The standard-library code in `checks/check.py` checks exact integer coefficient identities, palindromicity, the forced boundary root, and 12 high-precision root brackets. Its actual stdout is embedded in `checks/OUTPUT.txt`. The general negative-root proof, Rouché argument, coefficient tail bounds and Stirling estimates are analytical and do not depend on finite computation. The checker does not certify publication novelty or substitute for an independent audit.
