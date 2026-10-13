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
The package reconstructs the first paper-form FAdam update on the scalar quadratic \(F(\theta)=\theta^2/2\).

`verify.py` checks the first Fisher bias correction, the adaptive-epsilon branch, inactivity of source-default clipping, the exact default jump \(D=\eta_1/10\), and the one-step objective amplification on points approaching the minimizer.

It also checks that replacing the vanishing adaptive stabilizer by a positive lower floor makes the preconditioned terms tend to zero.

The numerical checks are transcription guards only. The singular point and punctured-neighborhood formulas are proved in `RESULT.md`.
