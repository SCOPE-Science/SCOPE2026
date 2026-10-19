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

# Reproducible computational checks

Run `python check.py` with NumPy and SciPy installed. The standalone checker completed 109 deterministic comparisons successfully. Its checks cover exact fixed-path conditional variance identities, endpoint-Laplace estimates with nonconstant prescribed stiffness, Cauchy characteristic-function and tail evaluations, general-power Gaussian-ratio tail coefficients and finite sampled Brownian-path variance scaling.

The median relative error in the finite sampled-path test was 0.0084 over 44 paths. These numerical tests are deliberately supplemental: a finite stochastic sample cannot prove an asymptotic theorem or exact distributional identity. The analytical proof in `RESULT.md` controls both the endpoint neighborhood and all earlier times, and derives moment divergence from weak convergence of bounded truncations.

The motivating 2026 paper's full text was inaccessible for detailed scientific comparison; only its accessible abstract was read. Independent audit and independent validation have not been performed.
