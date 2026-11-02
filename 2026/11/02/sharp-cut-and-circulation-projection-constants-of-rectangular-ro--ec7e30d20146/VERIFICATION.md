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

The accompanying self-contained `check.py` was executed with Python 3. It used exact fractions on all thirty-six integer pairs satisfying \(2\le m,n\le7\), reconstructed full projection columns, verified both claimed optimal operator norms, checked the divergence of every circulation output column, and tested idempotence and generator identities in smaller instances. Reported output: `CHECK_OK: 36 parameter pairs, 27780 exact rational component checks; cut/circulation images, idempotence and norms`.

The algorithm checks finite cases only. Global norm optimality for every pair of positive integer sizes in the stated range follows from signed-permutation averaging, the full invariant-operator parameterization, and the affine absolute-value lower bounds in `RESULT.md`. Equivalent earlier results under other terminology cannot be categorically excluded.
