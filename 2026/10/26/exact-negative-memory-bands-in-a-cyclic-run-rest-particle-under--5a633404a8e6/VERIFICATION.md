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

Run `python verify_covariance.py` with NumPy and SciPy. The program constructs the four-state clockwise Markov generator, solves stationary mixed-position moments, and propagates a separate five-variable mixed-moment linear system. Its output is compared against the analytical scalar covariance for 26 independent confinement ratios and 30 lags (780 comparisons). It also checks numerical onset bracketing, representative negative-band counts, critical lobe signs and the predicted asymptotic count. This independent numerical route agrees to at most \(1.34\times10^{-15}\) absolute error at the tested points.

The proof of the infinite-time and continuum-parameter classification is analytic and depends on the explicit Green-kernel convolution and exact kernel-composition identity; no finite computational experiment is interpreted as proof of uniqueness or of infinitely many sign changes. Independent scientific validation has not been conducted.
