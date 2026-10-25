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

## Analytic check and reproducibility

The stationary renewal identity, Brownian covariance integrals, Gaussian regression coefficients, Mills-ratio saddle asymptotics and bridge-residual maximal bounds are derived explicitly in `RESULT.md`. The nonstandard claim is the joint conditional law of the entire path, excursion age and transverse endpoint. The leading longitudinal marginal tail agrees with the known random-acceleration class; that alone is not asserted to establish novelty.

Execute `python CHECK.py` with Python 3, NumPy and SciPy. The checker evaluates the exact age-mixture tail, its conditional first and second moments, the Gaussian projection of trajectories, and independent covariance-kernel quadratures. Expected deterministic output: `PASS: 177 deterministic assertions`.

The numerical verification is performed at finite thresholds, so it is not a proof of the asserted infinite-threshold limits. The proof relies on a unique nondegenerate Laplace saddle, uniform Gaussian tail bounds, and conditional Gaussian bridge estimates. No independent audit has been performed.
