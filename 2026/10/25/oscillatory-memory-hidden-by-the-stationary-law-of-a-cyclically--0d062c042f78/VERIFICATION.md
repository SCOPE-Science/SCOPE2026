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

# Reproducibility and limits

Run `python verify.py` with Python 3 and the standard library. The script has no external data dependencies. It evaluates the exact time covariance by a complex-valued closed expression, independently by Simpson quadrature of the unintegrated last-reset-time formula, and independently by fourth-order numerical integration of the finite three-state Markov moment equations. Parameters span rate ratios above, below, and on the critical boundary. It checks the critical amplitude identity, positivity of the below-threshold asymptotic coefficient, and signs of late oscillatory lags.

Recorded outcome: `PASS 601 independent and boundary checks; max numerical error 2.2147333966771043e-10`.

The calculation is finite and numeric. The infinite-lag and all-parameter conclusions rest on the explicit renewal identity and analytic comparison of decay exponents and sinusoidal envelopes, proved in `RESULT.md`. Some related switching-diffusion primary text could not be inspected in full; historical originality remains subject to independent verification.
