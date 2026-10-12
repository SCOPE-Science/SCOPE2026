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

The general proof uses only degree bookkeeping in the source's exact reconstruction:
\[
\deg r_i\le1,\qquad
\deg\Delta\le2,\qquad
\deg N_i\le2.
\]
After clearing \(\Delta\), every term in \(P_G\) has degree at most three.

The bundled checker uses exact rational polynomial arithmetic at
\[
\mu=1,\quad
\gamma_1=2,\quad
\gamma_2=3,\quad
\beta_1=3,\quad
\beta_2=2,
\]
\[
\eta_1=\eta_2=\sigma_1=\sigma_2=
\theta_1=\theta_2=\theta_{12}=1,
\qquad
\Lambda=10.
\]
It reconstructs
\[
P_G(s)=s^3+53s^2-356s+260
\]
exactly, proving that the universal upper bound can be attained.

At rational test values away from \(\Delta(s)=0\), the checker separately evaluates the source's rational \(F_G(s)\) and verifies
\[
P_G(s)=-\Delta(s)F_G(s)
\]
with exact fractions. These point checks validate the implementation; the all-parameter degree theorem is the symbolic argument in `RESULT.md`.
