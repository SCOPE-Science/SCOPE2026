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

The printed incidence \(\beta e^{-mI(t-\tau)}S(t)I(t)\) was differentiated independently with respect to \(S(t)\), \(I(t)\), and \(I(t-\tau)\). The resulting current/delayed matrices were expanded to the characteristic determinant and simplified using the endemic balance \(cp\gamma v=CGL\).

For the published parameter set, the reconstructed equilibrium is
\[
(S_*,E_*,Q_*,I_*,J_*)=(3271.592615677488\ldots,11.94110466102479\ldots,238.8220932204958\ldots,13.64697675545690\ldots,12.40634250496082\ldots).
\]
The standalone checker verifies the equilibrium equations, characteristic coefficients, zero-delay Routh--Hurwitz determinants, the sign pattern \(+,+,+,-,-\) of the frequency polynomial, the positive root \(z_*=0.004425301028674292\ldots\), the phase equations, and the direct residual at \((i\theta_*,\tau_*)\). It also checks that the real crossing derivative is positive.

The unique positive frequency proves that no other imaginary-axis frequency can yield an earlier crossing. The result does not certify nonlinear Hopf direction, periodic-orbit stability, or global dynamics, and it does not claim stability or instability for every delay beyond the first crossing.
