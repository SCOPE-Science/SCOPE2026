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

The complete standalone script `verify_beta_sketch.py` was executed with Python, NumPy, and SciPy and returned:

```
PASS: 34813 checks (complement projection, law, moments, boundaries).
```

It compares sketched normal equations with the complementary Gaussian-plane formula on independent nonorthogonal test designs; performs two-sample Kolmogorov–Smirnov and quantile checks against the independent Beta/chi-square representation; tests exact moment existence thresholds and the established real expected-error identity; and checks the strict mean Beta contraction over many dimensions. A floating-point test of the nearly singular minimally sampled case uses a relative accuracy threshold to account for conditioning.

The proof in `RESULT.md` provides the infinite-distribution and asymptotic assertions. Finite experiments cannot establish distributional equality, universal stochastic ordering, power-law asymptotics, or global originality. No independent audit has been performed.
