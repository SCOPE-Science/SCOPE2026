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

The proof is analytical. The standalone standard-library script `verify.py` independently solves the three stationary covariance equations using exact rational arithmetic, computes the finite-time cross covariance by matrix-exponential power series rather than the claimed closed form, and checks the coefficient, sign, peak, and both inverse reconstructions for sampled positive parameter choices. It performs finite checks only and is not a computer-assisted proof of all parameters and lags.

The stochastic dynamics assumes known physical time and thermal-length calibration. Stationarity is ensured by a common-noise contraction and a coercive quadratic Lyapunov function. Independent scientific auditing and experimental validation have not been performed.
