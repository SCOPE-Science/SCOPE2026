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

# Analytical and executable verification

The proof in `RESULT.md` is self-contained: derive the one-sided occupation probability \(1-e^{-u}\), the probability \(e^{-u}\) of an unoccupied near neighbor up to the central acceptance time, and the conditional occupancy parameter \(1-(1-u)e^{u-t}\). Mixing two conditionally independent Bernoulli indicators over \(h_t(u)=2e^{-2u}/(1-e^{-2t})\) yields the covariance. At saturation the two nearest gaps are restricted to lengths \(2\) and \(3\); the resulting matrix is also implied by previously known pair correlations and is a consistency check, not an originality claim.

Run `python checker.py` using Python 3's standard library. The checker recomputes integrals numerically for twenty time values, verifies the exact probability matrix and its normalization, and independently generates random greedy packings of 350-site periodic rings for 1100 trials to test the predicted probabilities. Its observed statistics and assertion count are recorded in `checker_results.txt`.

All floating-point quadrature, finite-ring sampling, and finite assertions are corroborative. They are **not** proofs of infinite-lattice existence, an exact joint probability, a universal sign, or uniqueness of a scholarly result. Those mathematical assertions rest on the explicit analysis in `RESULT.md`; independent audit has not been performed. 
