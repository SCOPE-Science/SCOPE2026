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

The complete analytic proof and the closed-form equality cases appear in `RESULT.md`. The accompanying `verify.py` was run from the supplied directory with Python 3 and NumPy, returning `PASS: 49319 exact-rational identities or deterministic numeric checks`.

Exact-rational calculations verify weighted Gram identities, cubic tensor contractions, exact Pearson-divergence remainder, partition-wise cubic bounds, fixed-smallest-mass envelope extrema, and interpolation for sampled finite-support probability profiles. Numerical tests use a 4096-point directional grid in dimension two and three resolutions of the Fourier weak-error limit. They are corroborations only: neither finite samples nor a grid proves a universal theorem or the continuum asymptotic.

The all-dimensional proof instead uses the weighted orthogonal projector, a two-valued Lagrange-multiplier reduction, Parseval's identity for one-step scalar representation, strict convexity of reciprocal weights, and a uniform finite-support characteristic expansion. No external independent audit has been performed.
