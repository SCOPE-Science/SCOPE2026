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

A complete structural-induction proof is given in RESULT.md. `check.py` exhausts the three possible base-formula truth sets on each two-point model, checks preservation and common interpretations by all primitive connectives, checks both separating operations, and checks the singleton restriction. The executable test is a corroboration, not a replacement for unrestricted-formula induction. The arbitrary-formula result is proved from closure of the three truth sets under the operations; it is not extrapolated from bounded-depth samples. No general finite-model decision claim is made.
