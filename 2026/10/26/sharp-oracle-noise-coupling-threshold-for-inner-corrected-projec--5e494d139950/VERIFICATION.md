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

# Reproducibility and verification

The plain Python 3 standard-library program `verify_ipfe.py` is embedded next to this file. Run `python3 verify_ipfe.py` in an ordinary working directory after extracting the embedded files. It tests 1,680 exact rational four-stage implementations against the theorem's closed-form recurrence, tests the covariance-polynomial identity over multiple rational microstep ratios and correlations, and checks limiting coefficients at diminishing microstep scales. Recorded output:

`VERIFY_OK exact four-stage recurrence: 1680 fractional stage inputs; covariance polynomial and coupling limits`

The proof in RESULT.md separately establishes, for all \(0<\lambda<1/2\), the exact update, strict deterministic contraction, exact all-time second moments, necessary/sufficient correlation scaling, and sharp limits. The finite exact arithmetic program validates algebraic consistency but is not a complete enumeration of real parameters, a symbolic proof of all quantified cases, or an independent audit. Correlated final noises are a stipulated oracle model; a particular real implementation might not achieve correlation one. Full-text literature access was incomplete for the older variance-reduction article, leaving a residual priority risk.
