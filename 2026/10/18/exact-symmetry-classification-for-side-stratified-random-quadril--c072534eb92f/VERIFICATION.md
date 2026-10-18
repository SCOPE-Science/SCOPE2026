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

The `checker.py` file computes the exact coordinate shoelace area polynomial and integrates polynomial monomials over four unit intervals using rational coefficients. It verifies the mean, the vanishing third central moment, the fifth central-moment factorization and the two symbolic sign-reversal identities. Execute from the extracted directory with `python checker.py`; SymPy is required. These tests are exact polynomial identities; no Monte Carlo or timed computation is used in their acceptance. The theorem that the whole law is symmetric in the two claimed families follows from measure-preserving involutions, not a finite numerical test. Earlier moment calculations are used solely for prior-work comparison. The independent audit status is not performed.
