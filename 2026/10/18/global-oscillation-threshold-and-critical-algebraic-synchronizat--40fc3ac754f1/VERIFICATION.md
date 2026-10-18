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

# Verification

The standalone `verify.py` executes exact integer-algebra checks of the quartic difference identity, sample-based checks of the strictly monotone nonlinear remainder, linear eigenvalue calculations, and numerical integration at parameter values below, at, and above the sharp threshold. The exact polynomial certificate tests the cubic constant directly. No finite trajectory integration proves an infinite-time assertion; these checks are corroboration of the proof in `RESULT.md`.

The full mathematical proof supplies the strict rearrangement inequality, boundedness, planar equilibrium exclusion, Poincaré–Bendixson argument, and the critical inversion-asymptotic. All claims are restricted to the stated model and parameter domain.
