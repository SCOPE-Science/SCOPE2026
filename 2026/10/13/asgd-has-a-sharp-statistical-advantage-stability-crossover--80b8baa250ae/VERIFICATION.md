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
The package verifies the exact scalar Schur-stability law for the practical ASGD recurrence.

`verify.py` reconstructs the source two-state matrix, compares its characteristic roots against the closed stability ceiling over deterministic parameter grids, checks the \(-1\) boundary root, verifies the crossover at \(\xi=10/7\), and confirms convergence toward the sharp global lower envelope \(400/249\).

The finite checks are transcription guards. The if-and-only-if stability law and source-domain infimum are proved analytically in `RESULT.md`.
