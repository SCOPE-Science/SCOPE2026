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

For a boundary zero \(q\) of multiplicity \(\ell\), write
\[
f(z)=(z-q)^\ell g(z),
\qquad
g(q)\ne0,
\]
choose
\[
h=g^{1/\ell},
\]
and set
\[
\psi(z)=(z-q)h(z).
\]
Then
\[
f=\psi^\ell.
\]

The conformal-image curvature at the origin is
\[
\kappa
=
\frac{
1+\operatorname{Re}\!\left(q\psi''(q)/\psi'(q)\right)
}{
|\psi'(q)|
}.
\]
Using
\[
\psi'(q)=h(q),
\qquad
\psi''(q)=2h'(q),
\qquad
h'/h=(1/\ell)g'/g,
\]
gives exactly
\[
\kappa=\kappa_f(q).
\]

A real-analytic boundary germ of signed curvature \(\kappa\) occupies angular measure
\[
\pi-\kappa\rho+O(\rho^2)
\]
inside the radius-\(\rho\) circle. This follows by writing the rotated boundary as
\[
y=(\kappa/2)x^2+O(x^3)
\]
and solving for its two intersection angles with the circle.

On
\[
|w|=\rho,
\qquad
w=\psi(z),
\]
the level element satisfies the exact identity
\[
|f'(z)|\,ds_z
=
\ell\rho^{\ell-1}ds_w.
\]
For area,
\[
|f'(z)|^2\,dA_z
=
\ell^2|w|^{2\ell-2}dA_w.
\]
Thus the claimed level coefficient follows by multiplying the circular length
\[
\pi\rho-\kappa\rho^2+O(\rho^3),
\]
and the energy coefficient follows by integrating
\[
\ell^2t^{2\ell-1}
\left(
\pi-\kappa t+O(t^2)
\right)
\]
from \(0\) to
\[
\rho=\epsilon^{1/\ell}.
\]

The sign is independently checked by
\[
f(z)=z-1.
\]
The relevant arc inside the unit disk has angular measure
\[
\pi-\epsilon+O(\epsilon^3),
\]
so the first corrections are
\[
-\epsilon^2
\]
for the level integral and
\[
-\epsilon^3/3
\]
for the sublevel energy, exactly as the formulas predict with
\[
\ell=1
\quad\text{and}\quad
\kappa_f(1)=1.
\]

The proof establishes the continuum statement analytically. No finite sampling or numerical extrapolation is used.
