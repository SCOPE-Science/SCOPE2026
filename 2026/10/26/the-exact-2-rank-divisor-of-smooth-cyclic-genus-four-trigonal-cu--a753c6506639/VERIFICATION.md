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
Run `python verify.py` with Python 3 and SymPy. The code confirms the coefficient-square decomposition and verifies two squarefree examples independently through finite-field counts up to degree eight, Newton identities, and the reductions modulo \(2\) of their zeta numerators. It prints `VERIFY_OK` on success.

## Proof-dependent limits
The examples do not establish the theorem for all coefficients: that assertion rests on the exact Cartier identities and tame-cover genus calculation given in `RESULT.md`. The script checks formal polynomial identities, not the existence of an external independent mathematical audit. It does not compute the Newton polygon on the entire parameter space or resolve potential equivalence to unexamined literature.
