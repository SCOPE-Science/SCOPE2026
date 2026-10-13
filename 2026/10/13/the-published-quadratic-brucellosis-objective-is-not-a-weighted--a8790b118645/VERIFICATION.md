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
The bundled checker verifies the algebraic distinction without solving the optimal-control boundary-value problem.

For two nonnegative unit-interval running costs it confirms
\[
\int\ell_A\,dt=\frac12<\frac35=\int\ell_B\,dt
\]
but
\[
\int\ell_A^2\,dt=\frac12>\frac9{25}=\int\ell_B^2\,dt.
\]
Thus pointwise squaring before integration can reverse objective ordering.

Symbolic differentiation of the genuine weighted-sum Hamiltonian gives
\[
\frac{\partial H_{\rm WS}}{\partial\theta}
=S(\omega_3B_0-\lambda_1+\lambda_3),
\]
\[
\frac{\partial H_{\rm WS}}{\partial\varphi_1}
=S_1[\omega_4B_1+\beta I(\lambda_4-\lambda_5)],
\]
and
\[
\frac{\partial H_{\rm WS}}{\partial\varphi_2}
=S_2[\omega_4B_2+\epsilon\beta I(\lambda_7-\lambda_8)].
\]
These are control-independent switching coefficients.

For the source's quadratic vaccination term, symbolic differentiation gives an interior stationarity condition proportional to
\[
\theta=\frac{\lambda_1-\lambda_3}{2\omega_3B_0^2S},
\]
matching the structural form of equation (19).

The checker therefore verifies the claimed change in objective and in first-order control structure. It does not infer any particular numerical trajectory.
