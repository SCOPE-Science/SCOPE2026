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
The package verifies the exact fixed-task-rescaling laws of source-form RotoGrad.

`verify.py` checks invariance of normalized task directions and relative-convergence weights, the weighted arithmetic-mean backbone multiplier and its bounds, linear scaling of abstract task-specific head and rotation gradients, and exact common-scale one-step compensation of both displayed learning rates.

The computations are transcription guards. The coupled transformation laws and common-scale trajectory equivalence are proved algebraically in `RESULT.md`.
