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

The analytical argument derives the exact distributional identity, quantile sensitivity equation, global quadratic-mean displacement bound, and the sharp small-skew ratio. The included `check_quantile.py` was executed against its embedded source with NumPy and SciPy and completed 452 deterministic comparisons. Tests use numerical Gaussian integration, finite-difference sensitivity, and several skew parameters, including negative values. These finite checks do not certify the universal inequalities; the proof in RESULT.md establishes them. No independent audit has been performed.
