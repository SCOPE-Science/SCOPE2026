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

The analytical proof is in `RESULT.md`. The companion self-contained Python 3 script `verify.py` requires only the Python standard library and uses `fractions.Fraction` arithmetic to avoid floating-point ambiguity. Run `python3 verify.py` to repeat 7006 rational checks of the parameter grid, special equality thresholds, two-step return identity, and critical/subcritical inequalities. Exact finite tests cannot certify an infinite real-parameter statement; that conclusion is established by the affine branch proof. No independent audit or external validation was performed.
