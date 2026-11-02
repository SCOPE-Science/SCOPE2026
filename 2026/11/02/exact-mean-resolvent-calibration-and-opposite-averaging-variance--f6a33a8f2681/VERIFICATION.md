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

# Reproducibility and evidence limits

Run `python verify.py` with SymPy as specified in `requirements.txt`. At packaging time it produced `ALL CHECKS PASS` after ten symbolic identities, 275 distinct exact-rational parameter instances, and three independently generated seeded chains with stationary mean, variance, and lag-one covariance comparisons. The exact formulas are proved in `RESULT.md`; simulation and symbolic checking do not replace their analytical justification.

The statistical simulations use a fixed pseudo-random seed, a 400-iteration burn-in, and 159600 retained observations per chain. Sampling variability is allowed in comparison tolerances. No independent audit or external proof certification has been performed. Historical priority is qualified by the inspected sources and is not claimed conclusively settled.
