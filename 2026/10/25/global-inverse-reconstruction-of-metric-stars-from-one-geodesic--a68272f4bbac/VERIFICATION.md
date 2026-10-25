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
# Reproducibility and scope

Run `python check_star.py` (Python standard library) to reproduce the exact rational arithmetic and independent sampling checks. The test executes deterministic cases with length coincidences, 360 reproducibly generated rational stars, and four stochastic forward-law comparisons using 100,000 independently sampled pairs per example. Exact checks verify inversion, density integral one, and the small-distance intercept and slope; the sampled comparisons are numerical diagnostics only. A formal all-real-parameter proof is contained in RESULT.md, including the inductive sign argument for the first atom of every residual signed measure. This material constitutes an internal self-review, not an independent certification.
