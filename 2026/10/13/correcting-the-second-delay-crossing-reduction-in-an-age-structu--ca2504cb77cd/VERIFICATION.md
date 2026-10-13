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

Starting from
\[
|a+be^{-i\theta}|^2-|c+H_1e^{-i\theta}|^2,
\]
with
\[
a=B_1-\omega^2+iA_1\omega,\quad b=L_1+iQ_1\omega,\quad c=C_1+iD_1\omega,
\]
direct expansion gives
\[
K_2-2U_2\cos\theta+2V_2\sin\theta.
\]

The bundled verifier evaluates the complex-modulus expression and corrected trigonometric expression at several angles. For the source's rounded coefficients at \(\omega=1.4\), it also checks that the corrected cosine ratio is less than \(1\) while the printed ratio is greater than \(1\).

Limits: no full stability-region recomputation and no nonlinear Hopf analysis are performed.
