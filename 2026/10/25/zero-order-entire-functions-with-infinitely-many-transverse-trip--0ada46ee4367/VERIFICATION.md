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

## Finite algebraic verification

Run `python verify.py` (standard Python library only). It reconstructs the rational-cubic identity, critical angular derivatives, transverse radial slope, and the degree-gap recurrence. It does not enumerate or certify the infinite induction; the analytic proof supplies that reasoning. The construction deliberately makes only existential choices of large radii, and no external validator is claimed.

The independently checkable finite seed certificate is

\[|P(e^{i\theta})|^2=81/4-16(1-\cos\theta)(\cos\theta+1/2)^2.\]

The normalized transverse gap has derivative \(27\), forcing a crossing under sufficiently small real-symmetric perturbations. The full result requires the compactness, implicit-function, and coefficient-growth arguments in RESULT.md.
