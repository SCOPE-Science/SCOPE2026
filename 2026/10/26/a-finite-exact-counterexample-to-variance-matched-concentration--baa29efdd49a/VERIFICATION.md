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

The included verification script uses only the Python standard library and exact fractions. It checks the definition of each finite mixture, verifies that the total variances are equal to \(299\), exhaustively convolves the finite support, and asserts the two exact concentration values and their strict ordering.

Limits: the check is for the stated finite example only. It does not classify all parameters, prove a replacement concentration inequality, or constitute an independent audit.
