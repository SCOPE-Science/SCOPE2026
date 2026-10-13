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
The general inconsistency is analytic.

For the source-family witness
\[
\alpha\equiv1,\qquad
g(t)=t,\qquad
\tau=1,\qquad
a=1,\qquad
b=2,\qquad
t=3,
\]
the shifted-gamma kernel is
\[
\beta(s)
=
\begin{cases}
0,&s<1,\\
(s-1)e^{-(s-1)},&s\ge1.
\end{cases}
\]

The bundled checker evaluates the continuum limit of the printed sum as
\[
\frac{\widetilde f(3)}{\kappa}
=
3-9e^{-2}
\]
and the intended convolution as
\[
\frac{f(3)}{\kappa}
=
4e^{-2}.
\]
Their exact gap is
\[
3-13e^{-2}>0.
\]

The checker also verifies directly that the gap equals
\[
\int_0^3s\beta(s)\,ds.
\]

No finite-grid experiment is used to infer inconsistency. The nonzero continuum-limit gap proves it.
