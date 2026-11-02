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

# Verification and scope

Run `python3 verify.py` using standard Python 3 only. The extracted program reports 71 deterministic assertions if all checks pass. The checks include:

- Gaussian quadrature of the Gamma density versus the exact Erlang survival polynomial for four factor counts and six log thresholds.
- Independent numerical integration of the rate Laplace transform and its slow-frequency leading form.
- Spectral kernel unit normalization for eight starting sites.
- Modified Bessel series comparison against the deterministic-rate spectral integral.
- Exact iid-rate epoch spectral quadratures for three multiplicative factor counts at three horizons, against the predicted slowly varying asymptotic.

Analytical justification is in `RESULT.md`; computational tests do not certify the full infinite-time theorem. The rate-law tail assumption and the iid block-resampling scope are essential. No independent mathematical or publication-priority audit has been performed.
