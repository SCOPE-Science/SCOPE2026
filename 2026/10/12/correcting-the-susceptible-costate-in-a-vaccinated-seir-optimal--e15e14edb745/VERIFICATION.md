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
The bundled checker reconstructs the Hamiltonian symbolically.

It confirms
\[
-\frac{\partial H}{\partial S}
=
\lambda_1\left((1-u_2)\theta(I)E+\mu+z_0u_1\right)
-
\lambda_2(1-u_2)\theta(I)E.
\]

It confirms that the printed first-costate right-hand side differs by
\[
-(\mu+z_0u_1)\lambda_2.
\]

The second and third printed costates are checked against direct Hamiltonian differentiation and agree.

The terminal expansion is checked at coefficient level:
\[
\lambda_3(T-\tau)=C_3\tau+O(\tau^2),
\qquad
\lambda_2(T-\tau)=\frac{\alpha C_3}{2}\tau^2+O(\tau^3).
\]

An exact interior arithmetic witness also gives a printed-minus-correct first-costate derivative of \(-7\).

The correction is analytic; the checker is a replay of the algebra, not a numerical optimal-control experiment.
