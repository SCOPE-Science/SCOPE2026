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

Run `python verify_ashbm.py` after installing the dependencies from `requirements.txt`. The verifier computes the two-step ASHBM update using the direct gradient/momentum formula and independently using orthogonal Gaussian-frame formulas, with a fixed integer seed. It checks 1,000 stage identities in dimensions 2, 3, 4, 8, exact two-dimensional termination up to numerical precision, and six independent Gaussian fractional-moment comparisons.

The proof of moment divergence is analytical: the density of a one-dimensional standard normal is positive at the origin, so negative moments of its absolute value diverge from order one onward; the other factors are positive and independent. The finite moment formulas use spherical directions and gamma-integrals, not Monte Carlo extrapolation. Exact arithmetic is assumed in the theorem; floating-point checks are noncertifying corroboration.
