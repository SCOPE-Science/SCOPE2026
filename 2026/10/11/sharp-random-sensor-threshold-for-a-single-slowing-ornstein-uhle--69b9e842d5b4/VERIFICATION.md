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

# Reproduction and verification

Run `python check_sensor_extremes.py` with Python 3 and SciPy installed. The shipped checker was executed from its packaged source path and printed `PASS: 208 finite diagnostics; no claim of numerical proof for infinite limits`.

The finite checks include the exact \(n=3\) beta CDF \(\Pr(W\le w)=\sqrt w\), the \(n=2\) arcsine-beta CDF, the independent-sensor maximum law, the exact slow-versus-fast variance threshold, elementary variance/ACF algebra, and finite Gumbel-tail comparisons. They do not prove a Poisson or Gumbel limit.

The infinite argument rests on the explicit Gaussian sphere representation, a union-bound concentration estimate valid for polynomially many directions, Mills' ratio for the square of a standard normal, and the elementary binomial-to-Poisson limit. Every displayed probability is over the independent random sensor directions; for a fixed sensor, the variance and ACF are *population quantities conditional on that sensor*. No finite-sample inferential coverage, nonlinear bifurcation theorem, or correlated-noise extension has been verified.

The original source arXiv:2609.01164v1 was first publicly posted 2026-09-01, not assigned the date of a later journal publication.
