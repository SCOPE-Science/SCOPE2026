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
The main result is analytic.

The bundled checker uses exact rational arithmetic for
\[
A=1,\qquad
d=\frac15,\qquad
r=\frac3{10},\qquad
\lambda=\frac3{50},\qquad
h=10.
\]
It verifies
\[
\mathcal R_0=\frac35,
\qquad
E_0=(5,0),
\]
and
\[
J(E_0)=
\begin{pmatrix}
-1&-3\\
0&-1
\end{pmatrix}.
\]

It checks that the determinant of the two parameter-condition gradients is
\[
-10\ne0,
\]
so the two multiplier-\(-1\) conditions meet transversely.

It then evaluates the disease-free boundary map and verifies exactly
\[
(6,0)\longmapsto(4,0)\longmapsto(6,0).
\]
The two transverse one-step factors are
\[
-\frac25
\quad\text{and}\quad
-\frac85,
\]
so their product is
\[
\frac{16}{25}.
\]

Finite computation is not used to establish the continuum of two-cycles. That family follows identically from the boundary involution.
