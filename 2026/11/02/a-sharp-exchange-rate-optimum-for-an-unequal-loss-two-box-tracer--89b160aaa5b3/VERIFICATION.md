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

# Verification and reproducibility

The explicit matrix exponential was reconstructed from the stated two-compartment initial-value problem. The logarithmic-derivative test reduces all stationary points to one rational-algebra identity with a strictly negative numerator and a strictly positive denominator. The sign of the contrast derivative follows from a globally positive hyperbolic series, providing non-computational proof of the monotone optimizer.

The standalone `checker.py` requires Python 3, `sympy` and `mpmath`. Execute `python checker.py`; it yielded `PASS 1444 checks` and printed the numerical parameter examples. It independently compares 100 computed two-by-two matrix exponentials with the closed-form solution; checks 81 contrast settings for a unique numerical optimum, derivative signs and decreasing optimal exchange; and verifies the critical-point algebra and 16 exact Taylor coefficients. Tests are finite corroboration, not a substitute for the analytic theorem.

The published water-quality and compartment-model comparisons remain subject to the explicitly documented historical-priority limitations. Independent scientific validation has not been performed.
