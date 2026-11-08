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

# Reproduction notes

Execute `python verify.py` using Python 3 with NumPy and SciPy. It checks independent numerical integrations of the folded Poisson phase distribution, the reflected observation density, exact binomial count likelihoods, finite differences of likelihood derivatives, strict finite-population information growth on test grids, the weak- and fast-reset coefficients, and direct small-ensemble density-matrix quantum Fisher evaluations. The same package also compares the folded representation to a direct physical reset-age integral.

The program reports 320 passed deterministic numerical assertions. The limiting quantum Fisher optimum, martingale convergence, strict information-loss inequality for the reflected phase, and analytic asymptotic coefficients are established in the included mathematical proof, not inferred from finite numerical calculations. Numerical quadrature has its ordinary finite-precision limits. No independent scientific audit, external proof certification, or hardware validation has been performed.
