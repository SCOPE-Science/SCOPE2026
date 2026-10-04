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
The package reconstructs the practical Sophia momentum and Hessian-EMA update on an exact diagonal quadratic, with zero weight decay and constant learning rate.

`verify.py` checks the Hessian-EMA formula, limiting mode matrix, determinant and trace, exact Jury stability ceiling, exact complex-root plateau, low-curvature expansion, and the source-hyperparameter examples.

The finite computations are transcription guards. The local asymptotic theorem follows from the exact mode reduction and the geometrically convergent Hessian-state transient in `RESULT.md`.
