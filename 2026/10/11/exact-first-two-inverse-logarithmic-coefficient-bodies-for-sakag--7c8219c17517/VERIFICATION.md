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

For a Carathéodory function
\[
p(z)=1+c_1z+c_2z^2+\cdots,
\]
write
\[
p=\frac{1+\omega}{1-\omega}
\]
with
\[
\omega(z)
=
uz+(1-|u|^2)vz^2+\cdots,
\qquad
|u|\le1,
\quad
|v|\le1.
\]
Then
\[
c_1=2u,
\qquad
c_2
=
2\left(u^2+(1-|u|^2)v\right).
\]

For
\[
\mathcal S_S^*,
\]
the source identities give
\[
\Gamma_1=-\frac u2,
\qquad
\Gamma_2
=
\frac14u^2
-
\frac12(1-|u|^2)v.
\]
Hence
\[
\left|\Gamma_2-\Gamma_1^2\right|
\le
\frac12\left(1-4|\Gamma_1|^2\right).
\]

For
\[
\mathcal K_S,
\]
they give
\[
\Gamma_1=-\frac u4,
\qquad
\Gamma_2
=
\frac1{48}u^2
-
\frac16(1-|u|^2)v,
\]
and therefore
\[
\left|
\Gamma_2-\frac13\Gamma_1^2
\right|
\le
\frac16\left(1-16|\Gamma_1|^2\right).
\]

The converse Schur map
\[
\omega(z)
=
z
\frac{u+vz}
{1+\overline u\,vz}
\]
realizes every
\[
|u|<1,
\qquad
|v|\le1.
\]
The even--odd differential constructions in the result lift the resulting positive-real-part function to the defining Sakaguchi classes, so the fibers are exact.

For the starlike class, a fiber over
\[
r=|\Gamma_1|
\]
has center modulus
\[
r^2
\]
and radius
\[
\frac12-2r^2.
\]
Its smallest possible
\[
|\Gamma_2|-r
\]
equals
\[
\max\left(0,3r^2-\frac12\right)-r,
\]
whose minimum is
\[
-\frac1{\sqrt6}.
\]

For the convex class, the analogous expression is
\[
\max\left(0,3r^2-\frac16\right)-r,
\]
whose minimum is
\[
-\frac1{3\sqrt2}.
\]

Symbolic substitution and independent numerical sampling of Schur parameters were used only to check the algebra. The proof of exactness and sharpness is analytic.
