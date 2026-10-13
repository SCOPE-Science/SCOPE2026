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

The universal stability statement is analytic and uses no finite sampling of memory distributions.

The source-specific computation was independently reconstructed from the printed baseline model. The equilibrium identities reduce the endemic state to a scalar equation in total population \(N\). Bisection on \(902<N<903\) yields
\[
N^*\approx902.955757473,
\]
and then
\[
(X^*,H^*,Y^*,Z^*)\approx
(362.377257655,84.479329039,131.439986279,324.659184500).
\]

The analytic Jacobian at this state gives the monic characteristic polynomial
\[
z^4+0.5786699091z^3+0.08810770448z^2
+0.004035626673z+0.00003990077566.
\]
All coefficients are positive. The remaining quartic Routh-Hurwitz checks give
\[
a_1a_2-a_3\approx0.04694965067>0
\]
and
\[
a_1a_2a_3-a_3^2-a_1^2a_4
\approx0.0001761101341>0.
\]

The bundled `verification/verify.py` recomputes the equilibrium, all four equilibrium residuals, the Jacobian, characteristic coefficients, and both Routh-Hurwitz margins using only the Python standard library. It prints `VERIFY_OK` on success.

Unproved limits: no global endemic stability theorem is asserted; no claim is made for compartment-specific memory operators, distributed orders exceeding one, or epidemiological parameter changes that move the ordinary Jacobian out of the Hurwitz class.
