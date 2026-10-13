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
The bundled checker reconstructs the first Caputo coefficients symbolically.

For the stated model it uses
\[
A_S=\delta-q\beta K_1K_3-q\beta'K_1K_4-\lambda K_1,
\]
\[
A_{I_s}=(1-a)\sigma K_2+\rho_aK_4-(\lambda_s+\lambda+\phi_s)K_3,
\]
and
\[
A_R=\rho_hK_6+\tau_hK_5-\lambda K_7.
\]

It verifies
\[
A_{I_s}^{(5.9)}-A_{I_s}
=
\phi_s(K_3-K_4),
\]
\[
A_R^{(5.9)}-A_R
=
\rho_h(K_5-K_6),
\]
and
\[
A_S^{(5.10)}-A_S
=
q(\beta-\beta')K_1(K_3-K_4)+\lambda(K_1-K_2).
\]

For the exact positive witness, these differences are
\[
-1,\qquad -1,\qquad -\frac32.
\]

The checker also verifies that the correct susceptible and exposed infection terms cancel in their sum, as required for an internal infection transfer.

No trajectory simulation or finite parameter scan is used.
