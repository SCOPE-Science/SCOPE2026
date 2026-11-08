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

# Verification record

The proof directly checks the boundary-value equation, continuity of its solution and derivative at the half-circle, its Laplace transform at zero, strict monotonicity, and the regenerative renewal equation. It then uses a nonarithmetic renewal theorem and a full-domain differentiable cumulant limit to derive the large-deviation principle. Explicit hyperbolic-function asymptotics yield the logarithmic correction and the leading factor-four effect.

Execute `python CHECK.py` after extracting the embedded files from the finding. This program uses an independently discretized piecewise backward equation, and tests a finite selection of reset rates, diffusivities, circumferences, Laplace variables and tilt values. Its finite checks do not constitute proof for all parameters or infinite-time statements. The scientific limitations and incomplete closest-source access are stated in `RESULT.md` and `REVIEW.md`. Independent audit has not been performed.
