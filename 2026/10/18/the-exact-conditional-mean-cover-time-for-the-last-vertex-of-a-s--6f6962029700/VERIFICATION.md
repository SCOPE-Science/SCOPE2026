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
# Reproducibility and proof boundaries

`python verify_cycle_last_conditional.py` uses only Python standard-library exact rational arithmetic. It checks every direction-resolved probability and time-weighted formula for visited-arc lengths 2 through 60, compares aggregated conditional means, and checks the finite gambler's-ruin exit-time difference equation for paths. The script produces a PASS count upon success.

All finite checks supplement the universal inductive proof in `RESULT.md`. In particular, they are not evidence for an untested infinite step, an originality certificate, or independent validation.
