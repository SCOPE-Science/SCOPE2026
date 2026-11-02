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

# Verification and reproducibility
Run `python verification.py` in a folder containing this file and `verification.py` with Python 3. The check uses independent deterministic products and sums for the finite clock distributions, plus seeded exponential sampling for winner locations. The finite-distribution calculations and simulation are corroborating evidence, not a substitute for the full infinite limit theorem. The spatial limit, positive-rate hypotheses, tail truncation, and Poisson coupling are proved in `RESULT.md`. Independent mathematical validation has not been performed.
