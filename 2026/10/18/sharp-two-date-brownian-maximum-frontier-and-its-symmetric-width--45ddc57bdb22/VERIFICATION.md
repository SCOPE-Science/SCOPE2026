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

Run `python verify.py` with Python 3 and `mpmath` installed. Its fixed parameter grid independently integrates the conditional future-gain kernel against the exact drawdown density and compares with the closed-form expression. It also checks the derivative of that expression, half-normal distribution normalization, quantile constraints, upper/lower integral representations, strict envelope inequalities, a uniform benchmark and the numerically evaluated width.

The reference run yielded **291 high-precision identity assertions passing** and strict inequalities across **42 parameter pairs**. These are finite numerical consistency tests, not exhaustive verification over the theorem's continuous parameter space. No external certificate, independently authored assessment, or automated mathematical proof is claimed.

The infinite-domain result is supported by the analytic steps in `RESULT.md`: Brownian reflection and independent increments; strictly monotone conditional gain; equal-mass threshold rearrangement; elementary antiderivative; continuous quantile-window interpolation; and strictly signed curvature. Priority against potentially unlocated special-case formulas remains open to independent literature review.
