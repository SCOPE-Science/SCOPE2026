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

# Verification

The displayed covariance and asymptotic are proved analytically in RESULT.md for every integer \(m\ge2\). The independent exact-rational test in `checks/exact_replay.py` reconstructs the mixed moment using independent exponential order-statistic increments and third moments, not the translated-simplex integration. Execute with `python checks/exact_replay.py` from the finding directory, using Python's standard library only. It checks every integer \(m=2,\dots,30\), variance identities, and strictly positive covariance; the observed output was:

```
PASS: independent exponential-rank moment reconstruction for m=2..30
PASS: variance identities and strict covariance positivity for m=2..30
```

Exact finite verification is not an infinite proof. No external independent verification has taken place. The literature comparison leaves open potential equivalent general ordered-Dirichlet moment identities; the mathematical result concerns Pearson dependence under the uniform-spacing null only.
