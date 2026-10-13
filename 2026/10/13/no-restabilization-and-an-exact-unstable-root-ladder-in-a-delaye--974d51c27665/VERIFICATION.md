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
The analytic verification uses the characteristic factor
\[
D(z,\tau)
=
z^2+az+ah+(b-2h)(z+a)e^{-z\tau}.
\]

For
\[
0<h<\frac b3,
\]
the frequency equation has exactly one positive solution because its polynomial in \(\omega^2\) has negative constant term. The phase equations then yield
\[
\tau_n=\frac{\phi+2\pi n}{\omega_H}.
\]

The crossing-direction factor is
\[
2\omega_H^2+\kappa
=
\sqrt{\kappa^2-4\zeta}>0,
\]
so every critical pair moves from left to right.

The bundled checker evaluates the source example
\[
a=0.03,\qquad b=1,\qquad h=0.1.
\]
It verifies the characteristic residual at the first several \(\tau_n\), reproduces
\[
\tau_0=1.9546057932\ldots,
\]
and checks the spacing
\[
2\pi/\omega_H=7.8175576438\ldots.
\]

The numerical replay is corroborative only; the all-delay classification follows from the analytic frequency, phase, and crossing-count proof.
