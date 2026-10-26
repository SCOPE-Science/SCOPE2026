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

# Algebraic and analytic verification

The standalone `curvature_phase_check.py` checks with exact SymPy arithmetic the coefficient curvature formula, its strictly positive parameter derivative, the center/boundary comparison, the rational fourth-power-weight metric and curvature, the degree-twelve polynomial coefficients, endpoint signs, and rational root bracket. All checks returned `PASS`.

For \(t>-1\), the proof separately derives the outer-boundary limit by differentiating the closed kernel expression, with control of the lower-order term \((1-s)^{t+2}\). The all-real-parameter conclusion is analytic, not a finite enumeration. The uniqueness proof uses a strict derivative sign for the explicit integer-weight polynomial; high-precision root approximations are reported only for orientation. No independent validation or external certification has been performed.
