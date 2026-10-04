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

The mathematical proof works in the scaled time \(s=e^{b_t}\). It derives the invariant \(sx-z_\lambda\), reduces feasibility to a scalar forced oscillator, and applies an explicit energy estimate. Sharpness is proved separately on the zero-invariant family by a positive lower bound for the oscillator energy.

`artifacts/verify_elr_scalar_invariant.py` numerically integrates the transformed full system and the reduced oscillator for representative positive penalties and initial conditions. It checks invariant conservation, representation agreement, bounded scaled feasibility, and a nonvanishing scaled amplitude in the sharp family.

The numerical replay is not an infinite proof. Multiple coupled constraints, non-Euclidean mirror maps, nonlinear constraints, and nonzero Rayleigh friction are outside the final claim.
