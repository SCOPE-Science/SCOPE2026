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
# Reproduction and limitations

Run `python VERIFY.py` with Python 3.9 or later. The standalone script uses only the standard library. It reconstructs the exact numerical recurrence, certifies the rational-and-square-root bounds in the explicit trapping example, and tests several large-step trajectories and their asymptotic coefficient. It does not certify the infinite-time claims by finite iteration: those follow from the proof's invariant interval and explicit geometric series. No independent scientific audit has been performed.
