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

# Reproducible verification
Execute `python verification.py` with SymPy installed. The program independently inverts the actual six-state stationary generator in exact rational arithmetic for 60 rational parameter instances, verifies the column-generator balance and normalization, compares every flux to the theorem's rational formula, reconstructs the three-by-three ON resolvent symbolically, and checks the derivative and strict optimizer window. In this package, all checks returned `PASS`. The identities and strict all-parameter bounds are proved in `RESULT.md`; finite checker instances are not substituted for general proof. No independent scientific audit or external validation has been performed.
