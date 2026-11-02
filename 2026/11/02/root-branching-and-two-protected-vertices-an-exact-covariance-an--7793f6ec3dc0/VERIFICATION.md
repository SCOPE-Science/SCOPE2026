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

# Reproducible checks

Run `python verify_protected_covariance.py` with Python 3's standard library. The program implements the coefficient formula with exact fractions. It compares complete independent parent-array enumeration of all \((n-1)!\) recursive trees for each \(3\le n\le9\) against the first moment, root-degree mean, mixed moment and covariance. It checks the known closed protected-node mean and root-degree harmonic mean through \(n=90\), and finite asymptotic-remainder examples at larger orders, printing `PASS: 297 independent exact/finite checks` when all succeed.

All-size correctness is supplied by the generating-function and coefficient argument in `RESULT.md`. The finite checks cannot establish asymptotic bounds or general finite-size covariance signs. No independent audit or external certification has been performed.
