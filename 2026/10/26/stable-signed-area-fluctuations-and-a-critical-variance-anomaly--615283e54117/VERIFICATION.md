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

# Verification record

Reproduce the finite checks with `python checker.py`, requiring Python 3 and `mpmath`. The accompanying `checker_output.txt` records the actual completed run: `PASS 106 deterministic analytical-numeric assertions`.

The code checks (i) the explicit stationary covariance against its renewal-age integral at seven exponents and seven lags; (ii) the explicit integrated variance against independent quadrature at five horizons; (iii) the leading small-frequency cycle-area characteristic-function constants; (iv) critical Gaussian scaling at finite large cycle counts; (v) all three asymptotic variance coefficients; and (vi) the exact critical factor three. The infinite-time probability laws require the analytic Laplace-tail, renewal functional-limit, and boundary-excursion arguments in `RESULT.md`; finite checks are supplementary rather than a proof of those limits. In particular, the critical Gaussian weak-limit variance differs from the limit of normalized second moments, so a moment-convergence assertion would be false.

Independent audit: not performed.
