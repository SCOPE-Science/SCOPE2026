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

# Reproducibility checks and scientific limits

Run `python verify.py` with installed Python 3, `sympy` and `mpmath`. The checker reports `PASS: 176 symbolic and high-precision deterministic checks`. It tests the three-site exact hyperbolic factorization, the two root values and the sign on each of three intervals, the renewal-normalized endpoint probabilities, and high-precision examples of strict hyperbolic-sine minors and cofactor interpolation for several matrix dimensions.

The general determinant positivity, arbitrarily many prescribed reversal thresholds and unbounded-domain-in-parameter zero count are established in the mathematical proof, not by these finite experiments. No stochastic trajectory simulation or asymptotic extrapolation is used to certify an infinite statement. No independent audit has been performed. Full text of two conceptually nearby later spectral-response works was not available during the literature comparison.
