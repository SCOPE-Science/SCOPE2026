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

Executed `python verify.py` with SymPy available on the evaluated package contents. Output:

```
PASS: 229 exact symbolic and rational identity checks
```

The checker constructs the two-state stationary Markov weights, second moments, fourth moments, and full covariance characteristic polynomial independently from the stated stochastic generator. It checks, as symbolic rational-function identities, the variance, factorized one-exponential condition, positive-rate parametrization, effective decay rate, and fourth-cumulant formula. It separately confirms a grid of admissible rational parameters, the symmetric example, and a non-resonant control.

Symbolic identities certify the algebraic steps over parameter domains where denominators are nonzero. The analytic proof supplies those denominator and positivity hypotheses, stationary existence, spectral-rate distinctness, and ODE uniqueness; no finite sampling is used in their place. External literature novelty and independent scientific replication are not certified. No simulation or numerical approximation is required for the main theorem.
