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

# Mathematical and computational verification

The proof in `RESULT.md` is self-contained conditional on standard Brownian Gaussian tails, marked-Poisson void probabilities and basic convexity; no external certification is asserted. The stationary construction uses finite positive reset intensity for every label. The age-sum moment bound is derived from the exact joint survival formula and checked at its divergent endpoint. Upper and lower excursion bounds are optimized analytically and match for every fixed positive \(D,r\) and legal integer \(N,m,k\). The strict marginal-normalized batch-size ordering uses an explicit falling-factorial telescoping identity.

Execute `python verify.py` with NumPy and SciPy to reproduce two independent formulas for reset-hit probabilities, exact pair-age exponential-moment formulas and numerical pair-orthant Brownian mixtures. The checker confirms the finite-domain algebra and illustrates the asymptotic approach for representative thresholds, but finite checks are not infinite proofs.

Verification limits: no proof or numerical estimate is claimed for a pre-exponential factor, uniform growth in the number of particles, or arbitrary reset-time laws. Independent scientific audit has not been performed.
