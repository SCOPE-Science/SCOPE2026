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

Run `python verify.py` with Python 3, `mpmath`, and `scipy`. The verifier proves the two critical opposite-sign inequalities using exact rational arithmetic for the truncated logarithm, exponential, and exponential-integral series with explicit remainder bounds. Its high-precision root approximations and independent gamma numerical integrations are diagnostics only. It also checks the second-moment transition formula.

The complete scalar proof and the large-probe analytic expansion appear in `RESULT.md`. Neither numerical quadrature nor a finite list of checked sample sizes is used as an infinite proof. The proof applies only to independent fresh real Gaussian two-point probes and exact arithmetic. An independent audit has not been performed.
