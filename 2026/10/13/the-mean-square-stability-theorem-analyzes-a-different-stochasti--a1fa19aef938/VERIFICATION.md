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

For each coordinate, the abundance-proportional diffusion in Equation (2) is
\[
\alpha_iX_i.
\]
After translating
\[
X_i=X_i^*+U_i,
\]
it becomes
\[
\alpha_iX_i^*+\alpha_iU_i.
\]
The centered diffusion used in Equation (13) is instead
\[
\alpha_iU_i.
\]
The difference is the nonzero constant
\[
\alpha_iX_i^*.
\]

The packaged checker `verification/verify.py` replays these affine identities with exact rational arithmetic for positive representative values. It verifies that the centered model has zero diffusion at zero displacement, the translated Equation (2) does not, and the squared Frobenius norm of the latter's diffusion at the deterministic equilibrium is positive.

The universal theorem is algebraic and follows coordinatewise from the printed diffusion laws. The finite checker is a reproducibility aid, not a substitute for the proof. No numerical calibration or long-time simulation is used.
