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

Run `python verify.py` with Python 3 and SymPy installed. The checker verifies the constant-period trace/determinant and Jury expressions, the period-two trace/determinant and both Schur expressions as symbolic identities, and the exact rational instability witness. It prints `VERIFY_OK symbolic_matrix_identities=10 exact_witness=1`. The proof of the universal statement is the symbolic derivation in `RESULT.md`, not finite parameter testing. No independent audit or external validation has been performed.
