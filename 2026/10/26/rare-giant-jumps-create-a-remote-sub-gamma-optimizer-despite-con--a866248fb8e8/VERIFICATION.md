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

# Reproducibility and limits

The complete proof is in RESULT.md. `verify_rare_jump.py` uses Python's standard library, checks 101 \(\operatorname{Beta}(1,2)\) MGF coefficient identities (with strict comparison at all verified indices above one), four exact negative-origin-slope inequalities, four high-precision interior witnesses, and finite-order cumulant identities for three exponents.

Run `python verify_rare_jump.py` in a directory containing that script. Results of finite checks do not establish the all-parameter asymptotic or onset theorem; those follow from the inequalities and compactness argument in RESULT.md. Uniqueness of positive stationary points or optimizer branches is not claimed. No independent audit or validation has been performed.
