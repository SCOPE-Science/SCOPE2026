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

# Verification

The proof is analytic and applies to every finite nonnegative row-stochastic matrix. Its essential steps are the scalar comparison squeeze at the unique logistic cusp; cubic and quintic expansion of the scalar field; integrability of the inverse-square residual; the irreducible Perron-mode decomposition and exponential suppression of transverse components; and the exact time-integrated, commuting linearized matrices. None is inferred merely from a finite simulation.

The included `verify.py` checks the exact rational expansion coefficients and uses high-tolerance integrations on two irreducible and one reducible stochastic network, with positive and negative one-sided starts. It separately checks convergence of the renormalized integrated tangent factor on a homogeneous orbit. Execution requires the dependencies in `requirements.txt`.

Only the Taylor coefficients are established by symbolic computation. Numerical results corroborate, but cannot certify, the asymptotic statements over infinite time or enumerate all networks. The Perron–Frobenius spectral argument is a standard mathematical theorem applied analytically. No independent audit has been performed.
