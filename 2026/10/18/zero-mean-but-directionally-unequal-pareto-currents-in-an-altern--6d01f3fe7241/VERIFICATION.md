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
# Reproducibility and verification

Execute `python verify.py` in an environment with NumPy and SciPy. The standalone program evaluates the exact Bessel current with two independent expressions, checks Pareto renewal normalization, solves the exact zero-mean cutoff equation numerically, compares deterministic-age tail coefficients, and constructs an independent finite-state exclusion generator to test nonpositive covariances and a current-variance bound. It passed 81 checks for the indicated settings.

Critical analytic steps, not inferred from numerics, are the forced two-particle covariance equation, its positivity-preserving semigroup, the infinite-lattice current concentration, the short-age moment bound in the Pareto tail integral, and the strictly monotone mean-calibration functional. The numerical tail proxy uses the deterministic mean current and is deliberately not called an exact simulation of infinitely many exclusion particles. Finite-state tests are not exhaustive; standard double precision quadrature does not certify the decimal cutoff or constants.

The published comparisons are to arXiv:1906.11801v1, arXiv:2004.00951v1, and arXiv:2211.14120v1, plus SSEP foundational literature; priority still requires independent examination. The result specifically excludes instantaneous reset mass relocations from the measured within-cycle current.
