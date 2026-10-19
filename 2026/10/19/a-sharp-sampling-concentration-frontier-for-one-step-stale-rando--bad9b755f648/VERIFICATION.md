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

# Verification of the exact delayed-coordinate stability frontier

The attached standalone `verify_stale_rgs.py` uses the Python standard library's exact rational arithmetic. Running `python verify_stale_rgs.py` produced `PASS: 1366 exact conditional/recurrence checks`.

It calculates, by direct enumeration over the next independent coordinate, the conditional expected change of the positive quadratic energy and checks its equality with the analytical drift formula. It tests both equal and unequal fixed sampling probabilities and positive diagonal weights, as well as short exhaustive update histories against the three-moment recurrence. It also numerically checks the stated closed-form uniform threshold at representative finite dimensions. These computations do not certify the infinite time horizon or all real parameter values; the positive quadratic identity in the written proof establishes those claims.

No independent validation or external audit was performed.
