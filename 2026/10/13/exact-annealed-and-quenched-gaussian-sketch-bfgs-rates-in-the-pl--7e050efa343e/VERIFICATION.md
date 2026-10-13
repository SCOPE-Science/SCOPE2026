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
# Reproducible checks

Run `python verify.py` using Python 3 and only the standard library. The program checks 500 direct inverse-BFGS update/projector identities, 100 exact-rational characteristic-polynomial coefficients and monotone Perron eigenvalues, a 16,384-point deterministic quadrature for each of four angular laws, and three independent 250,000-step seeded Gaussian-direction paths. The pathwise log factors are compared numerically with the analytical formula. The exact-rational coefficient checks have no floating-point tolerance; the numerical steps are diagnostic only.

The proof of the infinite-horizon claims is in `RESULT.md`: a pathwise projection identity, the explicit Poisson angular law, the stationary ergodic theorem, and the rank-three even transfer-operator reduction. The positive-eigenfunction argument confirms that the leading eigenvalue is attained by every deterministic nonzero symmetric initial error. Unpublished data, external proof services, or a separate certification channel are not required for reproducing the stated diagnostics. Independent audit has not been performed.
