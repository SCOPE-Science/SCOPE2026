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

Run `python verify_pair_extremes.py` from a directory containing the supplied script. Dependencies are Python 3, NumPy and SciPy; no remote access is needed. The actual run printed: `PASS 4633 deterministic exact-rational and quadrature assertions`.

The checker independently constructs thinning rates from the discrete batch parameters, verifies the marked-Poisson two-point characteristic function against the published stationary transform by exact fractions, and matches the known squared-position covariance. It numerically evaluates the **exact** diagonal and off-diagonal stationary age integrals with scaled Gaussian log tails. Increasing thresholds show convergence of the joint-tail coefficient, conditional common-last-event probability and conditional age-gap Laplace transform to the proven limits. Assertions impose finite tolerances; these are diagnostics, not infinite proof certificates.

The result's proof establishes the rate and prefactor by the one- and two-dimensional Laplace method, including domination of the nonzero-age-gap boundary layer. It separately proves the independent-resetting Gaussian boundary regime. Fixed-rate asymptotics are not uniform in a vanishing co-reset rate. All displayed quantities concern two distinct labels in the stationary Brownian batch-resetting model.
