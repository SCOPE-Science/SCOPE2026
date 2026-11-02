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

Run `python verify.py` with Python 3 and the standard library; the script enumerates \(\sum_{n=2}^{9}(n-1)!=46,233\) recursive trees and checks exact indicator probabilities, conditional regressions and covariances, and the aggregate covariance. The harmonic recurrence, exact summation and limiting profile are proved in RESULT.md. Numerical peak checks are sanity tests only. Independent audit has not been performed.
