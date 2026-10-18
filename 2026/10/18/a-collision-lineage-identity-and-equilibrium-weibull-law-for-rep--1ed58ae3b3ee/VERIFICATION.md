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

# Computational verification

Run `python verification/birthday_lineage_verification.py` with Python and SciPy installed. It independently accumulates rational probabilities over all truncated labeled occupancy states, including an explicit state recording the first category to reach a threshold. It checks the finite-time survival-difference identity and its summed expectation identity for every category count from one through five and thresholds two through four. It compares the exact rational results against numerical Poisson-gamma integrals, and checks the derived two-scale asymptotic against direct quadrature at two large category counts.

Actual successful program output:

```
PASS exact finite-state identities: 165
PASS independent gamma-integral comparisons: 12
PASS sharp two-scale asymptotic checks: 6
```

All finite enumerations and numerical quadrature are checks, not a proof of the infinite-size statement. The theorem's unbounded quantifiers, density normalization, Riemann-sum passage, and error estimate are supplied analytically in `RESULT.md`. The verification does not independently certify scientific priority.
