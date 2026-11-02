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

The complete algebraic derivation is contained in RESULT.md. The standalone checker verify.py independently constructs both multiplication matrices, computes the common kernel in each homogeneous degree over GF(2), GF(4), GF(8), and checks every parameter tuple for the dimensions listed in RESULT.md. Observed output: `SPLIT_ALTERNATING_PENCIL_COMMON_KERNEL_OK 698` (10 field/size configurations, 698 tuples). This finite census is a regression check, not a proof for arbitrarily large dimensions or for fields not tested. No independent mathematical audit was performed.
