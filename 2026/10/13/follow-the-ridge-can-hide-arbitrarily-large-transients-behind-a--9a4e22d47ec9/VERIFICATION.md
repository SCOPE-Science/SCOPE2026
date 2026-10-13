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
The package verifies the exact scalar-quadratic Follow-the-Ridge transient law.

`verify.py` reconstructs the original player-coordinate FR update, verifies its exact triangularization in the ridge error, compares direct iterations with both the distinct-root and repeated-root closed forms, and checks that resonant one-step Euclidean amplification diverges while the two eigenvalues stay fixed.

It also verifies that the defining paper's quadratic \(f(x,y)=-3x^2+4xy-y^2\) has follower curvature and Schur-complement curvature both equal to \(2\), so equal player steps lie on the repeated-eigenvalue resonance.

The finite computations are transcription guards. All identities and the unboundedness statement are proved algebraically in `RESULT.md`.
