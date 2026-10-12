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
The bundled checker replays the algebra and the motivating article's Example 1.

The proof itself is analytic. Its key exact identities are
\[
eu^p=dv^{1-m}+qv^{r-m}
\]
at a positive equilibrium and
\[
G_v=-(1-m)d-(r-m)qv^{r-1}.
\]

For the source values
\[
m=0.6,\quad
r=1,\quad
a=3,\quad
b=0.2,\quad
p=0.5,\quad
e=1.1,
\]
the checker obtains
\[
K=15
\]
and
\[
(eK^p)^{1/(r-m)}
=
37.4624163930\ldots.
\]

It solves the exact equilibrium equations at several large finite values of \(q\), verifies residuals, and checks
\[
\operatorname{tr}J<0,
\qquad
\det J>0.
\]
The dimensionless quantity
\[
\frac{qv_q^{r-m}}{eK^p}
\]
moves toward one across the replayed sequence, consistent with the proved asymptotic law.

These finite calculations are verification examples only; they are not used to establish the theorem for arbitrarily large \(q\).
