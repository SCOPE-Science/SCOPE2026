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
The central identity is checked symbolically.

For the source model
\[
w_{n+1}
=
\left(
\frac{r_n+\mu_n\eta_nw_n}{1+\eta_nw_n}
\right)w_n
\]
and
\[
z_n=\eta_nw_n,
\]
the exact update is
\[
z_{n+1}
=
\frac{\eta_{n+1}}{\eta_n}
\left(
\frac{r_n+\mu_nz_n}{1+z_n}
\right)z_n.
\]

The bundled checker uses the admissible rational values
\[
a_1=a_2=\frac{7}{10},
\quad
k_1=k_2=1,
\quad
\mu_1=\mu_2=\frac12,
\quad
\eta_1=\frac14,
\quad
\eta_2=\frac34.
\]
It verifies
\[
r_1=r_2=\frac65,
\qquad
\alpha=\frac{36}{25},
\qquad
z_*=\frac25.
\]

The source-implied back-scaled second phase is
\[
\frac{8}{15},
\]
whereas direct evaluation of the original first-season map gives
\[
h_1\left(\frac85\right)=\frac85.
\]
The correct normalized second value is
\[
\frac65.
\]

The checker also reconstructs the two-step return map and verifies that its positive fixed points are governed by
\[
225x^3+2960x^2+4480x-5632=0.
\]
Its derivative is strictly positive on the positive axis, so the positive root is unique. Numerical root evaluation is used only to report the phase amplitudes after the exact uniqueness proof.
