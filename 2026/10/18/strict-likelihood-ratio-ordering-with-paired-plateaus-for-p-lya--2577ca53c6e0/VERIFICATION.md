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

The package contains `verify_polya_runs.py`, run with `python3 verify_polya_runs.py` and Python standard library only. The exact rational checker passed 11,202 comparisons. It tests every binary word through sample length 11, the conditional run kernel through 35, positive concentration grids through 28, all stipulated adjacent equality and strictness positions, and the moment identity. These finite checks corroborate but cannot certify the theorem for all sample sizes and real concentration parameters; the analytic TP2 proof supplies the unrestricted quantifiers. No independent audit has been performed.
