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

The finite diagnostic is `check.py`, executable with `python3 check.py`. Its 367 assertions comprise 101 exact coefficient-ratio equalities, 100 exact monotonicity inequalities, a boundary value, numerical optimizer comparisons on both sides of the sharp noise threshold, and checks of the large-variance trend. On successful execution it prints `PASS 367 checks`.

The all-degree monotonicity is established algebraically by formula (5) in `RESULT.md`; finite coefficient checks alone would not justify it. The full \(s\to\infty\) rate and constants follow from the explicit optimizer equation and Lévy support bounds, not extrapolation of finite numerical tests. Reproducibility does not confer independent validation or a priority guarantee.
