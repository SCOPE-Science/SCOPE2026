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

# Verification of the Gaussian–Marshall–Olkin crossover

The infinite theorem is proved in `RESULT.md` by Gaussian orthant analysis, Mills-ratio expansion, and strict conditioning monotonicity. The standalone file `checker.py` separately computes true bivariate Gaussian probabilities through one-dimensional Gauss–Laguerre integration and validates the sharp comparison on three values of \(\rho\). The numerical evaluation deliberately does not invoke the analytic two-dimensional orthant approximation from the proof.

Execute `python checker.py` with Python 3 plus NumPy and SciPy (specified in `requirements.txt`). The recorded execution was:

```
rho=0.20 critical constant c_rho=0.8019575667, ratios at L=1280: 1.255569, 0.792415
rho=0.50 critical constant c_rho=1.3955512665, ratios at L=1280: 1.571938, 0.627119
rho=0.80 critical constant c_rho=3.5373342210, ratios at L=1280: 1.803923, 0.533793
PASS: 63 independent quadrature/asymptotic sign checks
```

These are finite numerical tests of a limiting statement. They are not an exhaustive verification for every correlation or tail level. Historical priority has not been independently certified.
