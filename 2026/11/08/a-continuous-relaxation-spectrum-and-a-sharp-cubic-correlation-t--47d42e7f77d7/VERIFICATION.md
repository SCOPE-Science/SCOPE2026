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

# Reproduction and verification

The executable `checker.py` is complete and needs only the Python 3 standard library. Execute `python3 checker.py` from the extracted file directory. Its output is `PASS: 40 numerical assertions; q=2 mean, spectral covariance, derivative signs, asymptotic coefficient; q noninteger positivity.`

The checker compares two independently parameterized integrals for the same stationary covariance: the exponential-age renewal integral and a double integral of Gamma spectral rates, at five lags. It independently checks the known stationary second moment and mean, tests four low-order derivative-sign families, verifies decrease of the effective relaxation rate, and checks long-time coefficient ratios. It also tests positive noninteger cooling exponents. Quadrature and finite differences are finite numerical evidence, not proofs of strict complete monotonicity at all orders or asymptotic results at infinite lag.

The mathematically decisive verification is the proof in RESULT.md: the explicit no-reset decomposition, positive kernel \(rsu/[(r+s+u)(r+s)(r+u)]\), dominated-convergence edge expansion, analytic exponential integral, and positivity of the tilted spectral variance. At the physical exponent \(q=2\), the coefficient can be verified by differentiation of the source's stationary mean. These calculations establish the theorem under exactly the stated idealized renewal assumptions.
