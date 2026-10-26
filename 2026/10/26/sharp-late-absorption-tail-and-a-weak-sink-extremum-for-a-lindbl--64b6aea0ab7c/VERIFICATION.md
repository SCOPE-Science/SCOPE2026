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

# Verification record

Run `python verify.py` with Python, NumPy and SciPy from this package. The executed checker reported `PASS: 66 analytic-identity and finite-amplitude checks.` It evaluates both exact Bessel propagator forms, selected parameters on either side of the unit-loss transition, the analytic tail coefficient and stationary point, and the sign of the independently derived total-absorption derivative. The exact formulas, analysis of both spectral branch endpoints, nonoscillatory tail integration, and positive-coefficient moment argument are in `RESULT.md`.

Finite numerical checks are corroborative, not proof for all site indices, all positive loss strengths, or arbitrarily long times. The result is conditional on eventual absorption for its moment assertions; the absorption time also has positive mass at infinity. No independent audit or experimental validation has been performed.
