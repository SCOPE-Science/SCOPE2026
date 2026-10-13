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

The public `verify.py` checks exact symbolic identities for the second moment of the affine boundary diffusion, the Gaussian variance, the sharp negative-correlation floor, and the rational parameter example; executing `python verify.py` with SymPy prints `VERIFY_OK`. The proof also independently derives the exact logarithmic infection decomposition from the SDE, controls the nonlinear coupling error, and applies the ergodic and martingale limit theorems under finite second moments.

No finite experiment proves an infinite-time limit; the algebraic verifier certifies only the displayed identities. The source paper's near-endemic Gaussian approximation is a different statement. Strict negativity of the extinction exponent and the finite-second-moment noise inequality are required. No independent scientific audit has been performed.
