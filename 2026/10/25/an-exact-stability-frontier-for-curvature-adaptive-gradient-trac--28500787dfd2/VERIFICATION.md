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

The exact symbolic check in `verify.py` confirms the characteristic polynomial of the linear update. The script verifies the Jury-condition identities and checks rational parameter points on both sides of each stability branch. It reports `VERIFY_OK` on success.

The convergence claim follows from the exact recurrence and the necessary-and-sufficient Schur criterion for a real quadratic. The extra eigenvalue 1 of the unconstrained state matrix is excluded by the invariant inherited from gradient-tracker initialization; the zero eigenvalue is a one-step disagreement transient. The result does not cover larger graphs, nonlinear objectives, multidimensional Hessians, or other stepsize rules.
