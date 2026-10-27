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

The included standalone `verify.py` uses only the Python 3 standard library. Replaying `python3 verify.py` performs independent two-dimensional Riemann-integral quadratures against all three closed-form Fourier formulas, checks the predicted coefficient signs over a finite range and computes two explicit finite negative Gram quadratic forms using direct discrete Fourier sums.

The numerical diagnostics do not certify the infinite-frequency statements. Those follow from the integration-by-parts/Riemann--Lebesgue argument, exact product-to-sum computation, and compact-group Fourier positivity criterion in `RESULT.md`. The general profile theorem requires two continuous derivatives and a nonzero derivative at the antipodal endpoint. No independent mathematical audit was performed.
