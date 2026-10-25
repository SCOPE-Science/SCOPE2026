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

The parameter theorem is proved analytically in `RESULT.md`; its verification is not reduced to finite sampling. Run `python3 verify_rectangle.py` using Python 3 standard library only. This reruns a rational exact-value certificate, 500 deterministic independent angular discretization comparisons against the implicit optimum, and three small-shape cube-root checks. The grid is a numerical diagnostic and cannot certify arbitrary real parameters. The exact rational case gives \(53/16\) for the stated nonsquare rectangle. Independently examine the density convolution, fixed-product monotonicity, and uniqueness of the scalar root before assigning external validation.
