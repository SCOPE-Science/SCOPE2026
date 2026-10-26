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

# Reproducibility

The standalone script `verify.py` uses only the Python standard library. Run `python verify.py`; it prints `PASS: 1639 exact/numerical assertions`. Exact `Fraction` calculations check the nonstandard binomial-curvature cancellation for all group sizes 3–30 and their interior thresholds. Simpson quadrature checks finite positive-excess-cost hitting-time integrals for five group/quorum combinations at two excess costs. These finite checks do not certify the infinite-time limit; the proof in RESULT.md supplies the general reasoning.

The values of the update-rate parameters are fixed to the unit-time convention in the cited primary equation. No off-face convergence verification, no mathematical independent audit, and no supplementary-PDF reading is claimed.
