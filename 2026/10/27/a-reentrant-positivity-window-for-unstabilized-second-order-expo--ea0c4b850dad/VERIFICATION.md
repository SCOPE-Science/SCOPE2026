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

The supplied `check_etdrk2.py` was executed directly from the candidate package path using Python 3 and SciPy and returned `PASS 261 deterministic checks`. It independently evaluates the two ETDRK2 stages and compares them with the closed-form multiplier across positive split ratios and step sizes, checks the energy-contraction range, brackets the two sign crossings, and tests the asymptotic predictions at progressively smaller ratios.

The exact identities and asymptotic deductions are proved in RESULT.md. Finite floating-point checks are diagnostic only; they do not establish universal positivity/negativity statements or prove the limits. The analytical proof assumes exact arithmetic. No independent external validation was performed.
