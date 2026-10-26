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

# Reproducibility

Run `python3 CHECK.py` in the same directory as this document. The script has no nonstandard dependencies, enumerates 96 rational parameter/mode configurations, and checks two explicitly calculated rational fourth cumulants. It checks all displayed stationary filter moments, the covariance matrix, the mean volatility, the rational matrix resolvent, strict-sign predictions, and an independently set up augmented-generator moment recursion. A successful run prints `PASS: 96 rational parameter/mode tests, 2 regression identities`.

The theorem for all admissible parameters follows from the symbolic generator, covariance, and positivity arguments in `RESULT.md`, not the finite sample of exact rational cases. No independent audit or independent external validation has been performed. Source comparison cannot establish exhaustive historical priority.
