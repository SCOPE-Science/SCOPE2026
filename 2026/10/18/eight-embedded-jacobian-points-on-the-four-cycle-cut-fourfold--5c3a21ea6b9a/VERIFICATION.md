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

The algebraic proof uses the full, published three-quadric presentation of the four-cycle cut model. The 32 global maximal minors and 12 fixed-point-chart minors are independently re-enumerated in `verify.py`, checking their integral signs. The local square-zero class is established analytically from the exact quotient ring; a finite-field rank test is corroborative only. The accompanying code uses the Python standard library and does not require a proprietary computer algebra system.

Checks run: `python verify.py` produced `VERIFY_OK` after exhaustive tests in characteristics two and three. Limit: testing finite fields alone cannot establish the all-characteristic or scheme-theoretic assertions; the proof supplies these separately. The full global minimal resolution of the singular scheme was not computed.
