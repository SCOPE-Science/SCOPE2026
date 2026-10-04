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

The proof was checked from the exact OPCGM--Lipschitz QP equations on the stated disk witness. The key identities are the radial full-step form \(x^+=ch\), strict return of the full iterate to the unit disk, strict escape of the next half-step, and the contraction recurrence for \(d_t=\|h_t-(0,-1)\|^2\).

`artifacts/verify_opcgm_disk.py` uses Python standard-library rational arithmetic to replay representative exact trajectories and check the same identities. The finite replay does not prove the all-iteration theorem; the induction and contraction proof in `RESULT.md` does. Inexact QP solves, nonconstant steps, and other constrained variational inequalities are outside scope.
