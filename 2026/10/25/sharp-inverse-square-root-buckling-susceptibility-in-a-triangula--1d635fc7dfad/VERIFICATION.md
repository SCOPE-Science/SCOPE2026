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

# Verification scope

The analytical proof is in `RESULT.md` and comprises an exact two-by-two determinant identity, the stationary colored-noise covariance, and a singular integral argument controlling all three soft lines and their common crossing. `verify.py` uses only Python 3's standard library and runs 1,808 finite regression assertions. It independently constructs the dynamical matrix, compares its determinant and inverse trace to the compact identities, and checks midpoint quadrature against the predicted limit and soft-line Fourier markers.

Run `python3 verify.py` with the script in the same directory. The observed pressure-gap values for the purely thermal unit-strength case are approximately 1.547708309 at 0.001 and 1.604868226 at 0.0001 for the product of square-root gap and bond variance; the analytical limit is approximately 1.632993162.

Neither a finite grid nor successful assertions establish uniform asymptotics. The proof excludes zero pressure gap and nonlinear rearrangement at or after instability. No independent audit has been performed.
