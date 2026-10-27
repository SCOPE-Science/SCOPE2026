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

# Verification performed
The standalone `verify.py` is the complete reproduction program and uses only the Python standard library. Execute `python3 verify.py` from this directory. It compares the previously known Stirling joint-count identity to an independent 3-state occupancy recurrence, verifies every reverse second-order minor across the stated finite test rectangle, and checks exact small-word enumerations. It also compares truncated stopping-time moment sums to the analytic harmonic identity.

The analytic coefficient and generating-function derivation in `RESULT.md` is required for all unbounded statements. The verifier is not a computer-assisted infinite proof. No independent audit was conducted.
