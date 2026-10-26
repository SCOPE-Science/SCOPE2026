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

## Checks and limits
The standalone `verify.py` uses exact `fractions.Fraction` arithmetic. It independently intersects the initial time interval with the preimages of permitted intervals at each checked power; it does not reuse the two-branch proof recurrence. It verifies the odd single component, even two components, exact rational lengths, reflected endpoints, and empty strict critical-threshold sets for 11 tested bases and up to seven runners. The infinite statements require the analytic proof in `RESULT.md`; a finite check alone cannot establish them.

No independent audit has been performed.
