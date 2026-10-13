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
The package verifies the exact two-client FedSplit recurrence from the proximal subproblem, centering step, and server average.

`verify.py` compares direct source-form FedSplit rounds with the closed cross-reflection map for random positive curvatures and centers, checks the unique fixed-point average, verifies \(A_s^2=r_1r_2I\), and checks the exact spectral radius.

It also verifies two-round termination for both curvature-matched choices and the exact rational witness with curvatures \(1\) and \(9\).

Finite computation is used only as a transcription guard. The finite-communication theorem follows algebraically from nilpotency.
