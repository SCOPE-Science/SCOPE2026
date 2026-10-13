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
The bundled checker reconstructs the constrained optimization symbolically.

It verifies
\[
\gamma
=
\frac{pc}{q}
\left(
\frac{\beta_1+p\beta_2}{1+p}
\right)^2,
\]
the feasibility boundary
\[
\beta_1+p\beta_2
<
(1+p)\sqrt{\frac{q}{pc}},
\]
and
\[
\mathcal R_{0,a}'(\beta_2)
=
\frac{q(1+p)^2}{c}
\frac{\beta_1-p\beta_2}{(\beta_1+p\beta_2)^3}.
\]

For the exact witness
\[
p=q=\frac12,\quad
c=1,\quad
\beta_1=1,\quad
\delta=\frac12,
\]
it verifies
\[
0<\beta_2<1
\]
as the admissible interval,
\[
\gamma(2)=\frac{16}{9},
\]
and
\[
\mathcal R_{0,a}
=
2+\frac{9\beta_2}{2(\beta_2+2)^2}.
\]
The derivative is positive throughout the admissible interval and the boundary supremum is
\[
\frac52.
\]

The proof is analytic and does not infer a universal claim from a finite parameter scan.
