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

The proof's necessary steps are the stopped-martingale renewal-variance identity, the orthogonal reward–duration variance decomposition, the explicit Bernoulli reversal divergence, and strict monotonicity of the integral quotient \(g(m)\). Those steps appear in RESULT.md and require no computed certificate. The global threshold cannot be inferred from checking a finite grid.

Run `python3 verify.py` using a Python 3 standard-library installation. The script checks direct finite-support second moments against the asserted decomposition, derives cost-adjusted precision by independently assembled components, searches maxima by both the proved implicit stationary equation and numerical golden-section optimization, tests regimes around the \(2/3\) boundary, and checks a separately seeded finite-cycle simulation. At preparation it returned:

```
PASS: 424 deterministic assertions; simulated ratio=1.0054558
Representative b=0.2: m*= 0.9637617920163861 gain= 1.8790513868798364
Representative b=0.5: m*= 0.7637340003082846 gain= 1.0726925403424359
```

The sample-based numerical test has finite statistical variability. No computer experiment proves the all-bias derivative sign; the integral representation and endpoint argument prove that claim. The efficiency concerns exact asymptotic completed-cycle current and the defined Bernoulli sign-reversal information. No physical heat-dissipation identity, correlated-cycle extension, or independent validation is asserted.
