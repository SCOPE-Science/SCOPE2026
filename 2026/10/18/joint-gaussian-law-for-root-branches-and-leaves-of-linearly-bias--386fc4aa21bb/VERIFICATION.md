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

The accompanying `verify_hoppe.py` runs with standard Python 3 and no optional packages:

```
python3 verify_hoppe.py
```

It enumerates all parent-choice histories through seven vertices at three rational root weights, computes history probabilities exactly as fractions, and verifies normalization, the exact expected root-branch count, expected leaf count, and exact branch/leaf covariance. Eighteen finite-model enumerations pass. It also evaluates the six deterministic finite covariance sums for \(n\in\{1000,10000\}\) and \(c\in\{1/4,1,3\}\) and compares them with the three closed limiting coefficients. The output `VERIFY_OK` confirms all programmed finite checks.

The proof's infinite statement additionally uses a bounded-increment triangular-array martingale central limit theorem: finite enumerations and numerical Riemann sums by themselves cannot establish this theorem. The limiting regime is strictly \(\theta_n/n\to c\in(0,\infty)\). No independent scientific audit has been performed.
