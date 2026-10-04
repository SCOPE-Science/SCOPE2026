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

The claim was checked from the published quadratic-kernel recurrence by direct algebra. For the scalar quadratic, the local curvature quantities reduce to \(\ell_k=L_k=\lambda\). The identities \(r^3=r+1\), \(2ra^2-2a-r=0\), and \(2b(b-1)=r^2\) determine which branch of the minimum is active at each alternating state and yield the exact period-two orbit.

`verify_cycle.py` performs a separate high-precision numerical replay using only the Python standard library. It checks the polynomial residual, the interval \(1<a<b<2\), both branch choices, thirty recurrence updates, and the closed-form iterate identities. The replay is a consistency check, not a proof of the infinite statement.

The result is limited to the stated scalar quadratic and specially chosen initial stepsizes; no attraction claim is made.
