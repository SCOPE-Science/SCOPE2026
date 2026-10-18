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

Run `python3 VERIFY.py` using Python 3 standard library. The program uses exhaustive distinct-output testing and an independently coded rotation-orbit criterion for each of the 65,536 possible Boolean functions, decomposes every reversible map into cycles, computes algebraic degree by Boolean Möbius inversion, checks rotation equivariance, and replays all representative truth tables through a second interpreter. The bounded five-site result is proved by exhaustive finite checking combined with the analytic rotation argument in `RESULT.md`; it does not extend to other ring lengths. No independent third-party audit was performed.
