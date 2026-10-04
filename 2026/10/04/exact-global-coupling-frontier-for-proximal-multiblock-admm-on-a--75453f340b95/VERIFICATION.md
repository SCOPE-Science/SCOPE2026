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

The proof reconstructs the source Gauss--Seidel proximal ADMM update on the scalar three-state identity-dynamics chain and reduces the resulting five-dimensional map to an exact characteristic factorization. Necessary-and-sufficient Schur conditions then give the stated frontier.

`artifacts/verify_multiblock_admm_frontier.py` uses only Python standard-library rational arithmetic. It builds the iteration matrix directly from the sequential block updates for rational parameter pairs, computes its characteristic polynomial by the Faddeev--LeVerrier recurrence, checks the quadratic-times-cubic factorization, and verifies the exact \(\chi=4,\ p=1/10\) boundary identities.

The finite replay is not the proof of the all-parameter statement. Unequal parameters, nonlinear dynamics, higher-dimensional noncommuting blocks, and inexact solves are outside scope.
