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
The package reconstructs published AdaPlus Algorithm 1 on the scalar quadratic \(f(x)=h x^2/2\) with zero weight decay.

`verify.py` checks the exact first source update, the zero-state belief denominator, the limiting two-state matrix, the three Jury quantities, the \(-1\) boundary root, and the published-default numerical thresholds.

It also checks the \(h=10\) startup witness. Numerical evaluations are transcription guards only; the threshold identities are proved algebraically in `RESULT.md`.
