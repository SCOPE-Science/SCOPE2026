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

# Verification details

The included standalone Python 3 `verify.py` uses only the standard library. Execute `python3 verify.py` from the extracted artifact directory and compare with `verification.log`: it executes 1,371 deterministic assertions and prints the expected phase interval, mean factors and logarithmic rate at the stated rational parameter.

Verified calculations include: row-update reduction; finite sign-string enumeration and probability weighting; matrix recursion for multiple moments; analytic characteristic-polynomial expressions; critical-probability signs; and the leading small-relaxation scaling. Independent symbolic derivations of the log-growth law and critical martingale are presented in `RESULT.md`.

These checks do not exhaust infinitely many trajectories or certify an unreviewed prior-art universe. Almost-sure convergence, boundary oscillation, and moment growth depend on the analytic arguments in the proof. No independent audit has yet been performed.
