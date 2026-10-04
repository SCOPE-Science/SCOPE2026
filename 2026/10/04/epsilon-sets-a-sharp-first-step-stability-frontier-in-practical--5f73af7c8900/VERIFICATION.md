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
The package verifies the exact first practical MADGRAD update on diagonal positive-definite quadratics.

`verify.py` reconstructs Algorithm 1 directly, compares it with the closed coordinate formula over randomized parameters, checks both sides of the sharp frontier \(c\gamma L=2\varepsilon\), verifies the exact spike radius, and confirms the limiting worst objective amplification.

The numerical calculations are transcription guards. The if-and-only-if frontier and supremal factor are proved algebraically in `RESULT.md`.
