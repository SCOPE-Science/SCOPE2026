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

Set
\[
\beta=\alpha+2,
\qquad
c=(p-1)\beta,
\qquad
a=(\beta+c)/2,
\qquad
d=(\beta-c)/2,
\qquad
s=1-|z|^2.
\]

With normalized weighted area, direct beta integration gives
\[
\|K_z\|_{p,\alpha}^p
=
{}_2F_1(a,a;\beta;|z|^2).
\]
Euler's identity then gives the exact transformed profile
\[
s^c\|K_z\|_{p,\alpha}^p
=
{}_2F_1(d,d;\beta;1-s).
\]

Gauss' boundary formula gives
\[
C
=
\frac{\Gamma(\beta)\Gamma(c)}
{\Gamma(a)^2}.
\]

For
\[
0<c<1,
\]
the connection formula at
\[
1-s
\]
has a regular branch and a
\[
s^c
\]
branch. Since
\[
s=o(s^c),
\]
the latter is the first correction, with coefficient
\[
\frac{\Gamma(-c)\Gamma(a)^2}
{\Gamma(c)\Gamma(d)^2}.
\]

For
\[
c>1,
\]
the transformed profile is differentiable at one. Its boundary derivative is
\[
C\frac{d^2}{c-1},
\]
which produces the linear defect.

For
\[
c=1,
\]
the derivative hypergeometric function is zero-balanced. Its logarithmic boundary divergence integrates to
\[
-Cd^2s\log(1/s)
\]
at first order.

Taking the positive
\[
p
\]
th root divides each relative first-order coefficient by
\[
p.
\]

At
\[
p=2,
\]
one has
\[
d=0
\]
and therefore
\[
{}_2F_1(d,d;\beta;1-s)=1
\]
exactly.

High-precision evaluations at subcritical, critical, supercritical, and Hilbert parameter values reproduce the displayed coefficients. They are consistency checks only; the proof is analytic.
