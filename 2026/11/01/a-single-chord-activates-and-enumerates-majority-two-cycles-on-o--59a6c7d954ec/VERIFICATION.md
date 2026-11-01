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

# Verification of chorded-ring majority dynamics

The complete standalone file `verify_chord_majority.py` enumerates actual bit configurations, applies the exact local majority update (with tie retention), and forms unordered primitive two-cycle orbits only when the return after two synchronous updates is confirmed. For each orbit, its flipping mask determines the observed endpoint-only, one-path, or global class. Independently, path-endpoint run counts are calculated by the binomial composition formula and checked by direct enumeration of possible binary interior words. These counts are combined into the predicted class totals. All comparisons passed.

Executed command: `python verify_chord_majority.py`

Observed totals: 66 parameter pairs; 327,696 configurations; complete class comparisons passed; stable-path endpoint counts passed. The full output is embedded as `verification_output.txt`. The code uses no packages outside the Python standard library. It does not explore or certify infinitely many configurations, and it does not address other graph families. The general theorem is supported by the written combinatorial case proof.
