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

The analytical result follows from two complementary bounds: a Gaussian quadratic exponential-moment bound with a Toeplitz row-sum spectral estimate, and a Gaussian autoregressive path-density lower bound around a piecewise-linear evacuation profile. The latter includes the exterior sites by a uniform conditional Gaussian tail and summable union bound. The two cubic constants agree exactly.

To reproduce the finite algebraic checks, run `python3 check.py` with a standard Python 3 interpreter. The execution completed 15,353 exact-rational assertions covering covariance–precision inverse identities, row-sum bounds, interval-avoidance inequalities for finite blocks, and discrete energy identities. The code uses no third-party dependencies and has no stochastic tests.

The finite checks are not an exhaustive proof of the asymptotic theorem; the infinite-volume limit is justified in `RESULT.md`. Independent validation has not been performed. The asymptotic is pointwise for fixed \(0\le\rho<1\) and fixed \(\sigma>0\); it is not claimed uniformly over parameters.
