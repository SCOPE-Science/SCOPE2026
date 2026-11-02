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

# Reproducibility

Run `python3 verify.py` using Python 3.9 or later; it requires only the standard library. The code independently integrates the conditional Gaussian-noise probability defining the actual greedy update, checks the closed-form mean-square risks for seven parameter configurations, samples 721 orientations at 15 scale/noise pairs to test the stated sharp upper/lower envelope, and bisects the scalar boundary.

Observed output from the embedded script before packaging:

```
PASS: 10893 deterministic checks, Gaussian conditional integrals and sharp bounds
unique one-sparse crossover r/sigma = 1.240125266627191
zero-signal reuse penalty (sigma=1) = 0.636619772367581
```

The analytic proof of exactness and uniqueness is provided in RESULT.md; a finite quadrature grid or numerical root cannot certify a quantified continuous result. The test tolerances are explicit in the code. There is no independent external audit or generalization to correlated-noise, multiple-step or nonidentity systems.
