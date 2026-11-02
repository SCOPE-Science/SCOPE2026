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

The proof uses finite-dimensional exact operator inequalities and covers every positive integer power. The following reproducibility check is separate from the analytic proof:

```sh
python3 verify.py
```

Observed output: `OK: 5602 exact-rational assertions passed.` The verifier uses Python 3's standard-library `fractions` module, not floating-point tolerance tests. It checks every partition in multiple small positive directed circulants; exact weighted stationarity and normality; the all-time quantitative gap and strictness; an exact nonnormal compressed four-cycle; a positive, nonuniform-stationary normal product chain; the general nonnormal time-two commutator criterion; and exact equality in the coefficient-sharp refresh construction.

The checker is finite and cannot establish the full theorem, the novelty claim, or mixing time order at arbitrary dimensions by itself. Analytical proof steps and all quantifiers are given in RESULT.md. Independent audit was not performed.
