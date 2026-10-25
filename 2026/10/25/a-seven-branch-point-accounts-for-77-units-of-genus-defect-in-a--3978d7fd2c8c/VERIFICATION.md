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
The embedded `CHECK.py` uses SymPy and integer arithmetic. Executing it checks the polynomial reductions, finite-root values by exact remainders, degree bookkeeping, cubic-jet split, and the delta arithmetic. The analytic proof in `RESULT.md` supplies the nonfinite arguments: branch separation, exact order-four contacts, and genus normalization. This evidence does not constitute external certification. No independent audit has been performed.
