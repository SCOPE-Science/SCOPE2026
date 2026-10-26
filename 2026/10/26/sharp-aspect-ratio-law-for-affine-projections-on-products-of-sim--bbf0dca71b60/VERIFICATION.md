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

# Reproducibility and scientific limits

The standalone `verify.py` uses Python 3 standard-library exact rational arithmetic to check the moment matrix implications, kernel normalization, and explicit negative-mass integrations in small product domains. It evaluates closed-form asymptotic constants numerically for consistency, not as an infinite proof. Run with `python verify.py` in the directory containing the files. The main analytic proof is in `RESULT.md`; the checker does not certify all dimensions or all weight vectors.

Self-review covers factor-kernel reproduction, convex vertex reduction, the fixed-factor-count exponential limit with uniform integrability, strict pairwise balancing, and the equality cases. The remaining originality risk is equivalent coverage in older, unindexed multivariate projection literature. Independent audit has not been performed.
