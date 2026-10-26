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

# Verification of the squared Gaussian ambiguity design law

The normalized Gaussian has \(\|g_a\|_2=1\). Completing the square in the ambiguity integral gives \(|\mathcal A g_a(X,\Omega)|^2=e^{-\pi(aX^2+\Omega^2/a)}\); rotations give the quadratic forms used in RESULT.md. The proof establishes the continuum minima and the global supremum by the largest-gap estimate, an equispaced two-neighbor boundary-layer calculation, and a comparison of their matched leading coefficients. Strict derivative and second-derivative estimates give the quantitative optimizer rigidity. The perturbation law follows by expanding at the two neighbors of each gap midpoint, taking the local hyperbolic-cosine minimum, and maximizing the cyclic gap increment.

The supplied standard-library checker at `checks/gaussian_design_check.py` was executed from that exact file path and returned `PASS: 86 finite analytic-identity and numerical assertions.` It checks the normalized exponential profiles, the two-channel case, the coefficient identities, and several finite-parameter near-asymptotic cases. Dense finite angular grids cannot establish the global continuous minimum or an infinite limit; those statements rely on the written proof.

All claims concern equal-precision *linear ambiguity inversion*. Neither nonlinear recovery of a signal from spectrogram magnitudes nor priority over all possible unindexed literature is established. No external independent audit or validation was performed.
