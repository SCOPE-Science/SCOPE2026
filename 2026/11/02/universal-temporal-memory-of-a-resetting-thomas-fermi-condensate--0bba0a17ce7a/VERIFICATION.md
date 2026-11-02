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

The accompanying `verify_edge.py` was executed from its actual file path. Its exact-rational tests checked exponential factorial moments, covariance polynomials, the integrated covariance values 28 and 2304, and the \(7/5\) leading and \(-88/25\) next coefficient. With NumPy and SciPy installed, it solved the deterministic expansion ODE and tested numerical integration at \(r/\omega=20\) and \(40\): measured dimensionless correlation times were about \(1.391906924\) and \(1.397849257\), against two-term predictions \(1.3912\) and \(1.3978\). The fast-reset normalized covariance at dimensionless lag \(u=1\) was checked against \(7e^{-1}/5\). All enabled assertions passed.

This executable checker verifies finite algebraic identities and numerical consequences only. The statements for all reset rates, strictness for all lags, the global long-lag limit and asymptotic remainders depend on the mathematical proof in `RESULT.md`, not on numerical sampling. Microscopic quantum edge fluctuations and independent publication-priority checks were not performed.
