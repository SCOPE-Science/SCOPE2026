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

# Reproducibility and claim boundaries

Run `python3 check.py` with Python 3 standard library. The recorded console output is stored in `CHECK_OUTPUT.txt`. The checker carries out exact rational finite Markov hitting-time calculations against the integral-derived generating function, rational one-defect transforms, and numerical convergence of finite heterogeneous profiles to the product-chain Laplace transform.

The infinite result relies on the mathematical argument in RESULT.md: independent last-appearance marks, a stationary-target renewal convolution, uniform log-product convergence, a dominated limiting transform, and the coupon Gumbel theorem. Finite experiments do not certify these infinite steps, publication priority, or independence of evaluation. Only the explicitly stated domains and weak-convergence conclusions are proved. Independent audit was not performed.
