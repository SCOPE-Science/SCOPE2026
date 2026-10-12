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
The bundled checker reconstructs the threshold from the treated weak-Allee scalar equation.

It verifies
\[
\phi'(x)
=
\frac{Kc-x^2-2cx}{K(x+c)^2},
\]
the critical density
\[
x_*=\sqrt{c(K+c)}-c,
\]
and
\[
\phi(x_*)
=
\frac{(\sqrt{K+c}-\sqrt c)^2}{K}.
\]

It verifies the positive-equilibrium polynomial
\[
r x^2-K(r-g)x+gKc=0
\]
and the exact root formula below threshold.

For
\[
K=2,\qquad c=1,\qquad r=\frac3{25},
\]
it checks
\[
g_c=r(2-\sqrt3).
\]
At
\[
g=\frac1{25},
\]
one has \(g_c<g<r\) and no positive equilibrium. At
\[
g=\frac1{50},
\]
the positive equilibria are
\[
\frac{5-\sqrt{13}}6
\quad\text{and}\quad
\frac{5+\sqrt{13}}6.
\]

The universal classification is analytic; the exact examples are only replay checks.
