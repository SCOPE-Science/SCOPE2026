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

# Verification of the scalar two-use ordering theorem

The proof is self-contained in `RESULT.md` and relies on exact algebra and a positive-parameter AM–GM minimization. A reproducible, dependency-free `checker.py` validates both separately implemented Kalman schedules against the independent factored precision identity on 5,000 fixed-seed rational parameter draws. Each draw also checks the sign comparison with the quadratic ordering criterion. It additionally evaluates exact rational three-regime witnesses and numerical endpoints. The checker completed **10,016 assertions** successfully.

The exact-rational identity tests are evidence of a correct algebraic implementation, not substitutes for the proof of the full real-parameter claim. No complete enumeration of continuous parameters, independent scientific audit, finite-precision implementation test, or exhaustive publication-priority certification was performed. Relevant earlier published work includes general finite-horizon sensor scheduling and scalar ordering with unrestricted reuse; these do not explicitly supply the once-only sharp noise frontier.
