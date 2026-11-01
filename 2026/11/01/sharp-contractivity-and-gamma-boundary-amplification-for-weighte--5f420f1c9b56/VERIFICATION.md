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

# Mathematical verification

**Analytical checks.** The exact Poisson Fourier multipliers are diagonal in the normalized circle Hilbert space. The negative multiplier is an incomplete-beta survival tail. Negative-binomial convolution proves contraction at nonpositive weights; strict monotonicity of its tail-to-mass quotient gives the positive-weight spectral staircase. Elementary calculus establishes exactly one positive contractivity boundary. A uniform exponential bound on the beta-tail integral excludes escaping spectral modes; the Gamma hazard uniquely fixes the boundary scale and limit.

**Computational checks.** Running the accompanying `check.py` with SciPy tests the beta-tail identity against the elementary integer-weight formula, twenty exact modal transition radii, fixed-radius maximizing modes, sampled negative-weight contractions, positive-weight contraction radii, strict mode-ratio concavity, and the Gamma boundary profile. All 3,131 finite assertions passed. These checks cannot certify the theorem for infinitely many degrees, parameters or radii.

**Limits.** Boundary Gamma localization is proved at each fixed positive weight without a convergence rate and does not imply joint asymptotics as the weight tends to zero. Earlier unpublished or uninspected equivalent statements remain possible. Independent mathematical audit has not been performed.
