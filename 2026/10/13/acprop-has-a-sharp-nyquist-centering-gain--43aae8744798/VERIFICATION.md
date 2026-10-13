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
The package verifies the paper-form ACProp response to a persistent alternating gradient.

`verify.py` checks the exact first-moment and centered-residual formulas, the exact unrolled centered second moment, convergence to the stated denominator floor for several decay pairs, the matched uncentered control, and the high-signal gain factors.

The finite calculations are transcription guards. The closed forms and asymptotic gain are proved algebraically in `RESULT.md`.
