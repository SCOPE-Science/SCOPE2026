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

For the unit-edge regular octahedron
\[
O=\operatorname{conv}\{\pm e_i/\sqrt2:1\le i\le3\},
\]
central symmetry and the support function give
\[
W=\sqrt2\,M,
\qquad
M=\max_i|U_i|.
\]

The support bound
\[
1/\sqrt3\le M\le1
\]
is immediate from
\[
U_1^2+U_2^2+U_3^2=1.
\]

For
\[
m\ge1/\sqrt2,
\]
the six caps
\[
\{\pm U_i>m\}
\]
have pairwise disjoint interiors. Each has area
\[
2\pi(1-m),
\]
so
\[
F_M(m)=3m-2.
\]

For
\[
1/\sqrt3\le m\le1/\sqrt2,
\]
triple overlap has zero area and there are exactly twelve congruent pair overlaps. In the spherical triangle determined by two orthogonal cap centers and one lens vertex,
\[
\alpha=
\arccos\!\left(\frac{m}{\sqrt{1-m^2}}\right),
\]
and
\[
\beta=
\arccos\!\left(\frac{m^2}{1-m^2}\right).
\]
Sector subtraction gives
\[
A_2(m)=2\beta-4m\alpha.
\]
Therefore
\[
F_M(m)=3m-2+\frac{3A_2(m)}{\pi}.
\]

Substitution
\[
m=w/\sqrt2
\]
gives the packaged CDF.

The checker verifies exact endpoint relations symbolically and uses deterministic numerical quadrature only as an independent consistency test. No finite sampling is used to prove the continuum statement.
