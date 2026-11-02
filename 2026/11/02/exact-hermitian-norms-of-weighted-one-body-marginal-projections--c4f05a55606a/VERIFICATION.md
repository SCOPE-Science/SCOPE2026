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

The analytic proof is in RESULT.md. The accompanying checker.py tests rational binomial identities, exact matrix witnesses, mixed local dimensions, negative weights, finite random Hermitian inequalities, and both asymptotic regimes. Reproduction command: `OPENBLAS_NUM_THREADS=1 python checker.py` (requires NumPy).

The finite checker neither establishes an all-dimensional theorem nor substitutes for independent mathematical assessment. The theorem applies to Hermitian inputs only; its complex-linear and completely bounded analogues have not been assessed.
