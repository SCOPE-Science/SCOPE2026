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
The bundled checker reconstructs the source parameter set with exact rational numbers.

It verifies the disease-free levels
\[
S_h^0=10,
\qquad
S_v^0=\frac{1}{115},
\]
then computes
\[
a=\frac{\beta_1S_h^0}{q_h},
\qquad
c=\frac{\beta_2\beta_3S_h^0S_v^0}{q_hq_v},
\qquad
\mathcal T=a+c.
\]

Every normalized sensitivity of \(\mathcal T\) is checked from its exact symbolic dependence. In particular,
\[
S_{\lambda_h}^{\mathcal T}=0,
\qquad
S_{\delta_h}^{\mathcal T}<0,
\qquad
S_{\gamma_h}^{\mathcal T}<0.
\]

The checker also evaluates
\[
\mathcal R_{\mathrm{NGM}}
=
\frac{a+\sqrt{a^2+4c}}2
\]
at 60-digit precision and verifies its characteristic equation.

Centered finite differences independently replay the signs and magnitudes for selected sensitivities. These numerical checks support the algebra; they are not used to infer the general sign result.
