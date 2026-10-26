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

Execute `python3 verify.py` using Python 3 standard library. The exact rational checks completed with:

```text
exact covariance recursions vs full Bernoulli path sums: 1152
exact strict momentum spectral polynomial tests: 120
exact stability determinant signs: 48
exact zero-momentum optima: 3
PASS
```

The verification script separately computes complete finite Bernoulli path sums and the derived matrix recurrence. It also evaluates the polynomial root inequality and exact determinant signs. The infinite family is proved algebraically in `RESULT.md`; finite cases alone do not prove uniform correctness. No independent audit has been performed.
