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

The exact statement and proof are in `RESULT.md`. Run `python3 check.py` in a standard Python 3 environment, with no external dependencies or network access. The direct run returned:

```
PASS 97272 checks; imaginary-axis boundary 1.179959679570986
```

The script compares Schur–Cohn inequalities with independently computed complex quadratic roots on a deterministic grid and random samples, tests that stability at any sampled convex weight implies stability at \(q=1/3\), verifies the derivative and secondary-critical-point identities over rational inputs, and checks strictness witnesses and the sharp real and imaginary endpoints.

These finite checks cannot certify the continuum of complex multipliers. The universally quantified statement follows from the analytic derivative factorization, the exact nonpositive alternative stationary value, and the scalar-to-matrix companion determinant identity. The original source paper's later sections were unavailable for a full bibliographic overlap comparison, and no independent external audit or verification has occurred.
