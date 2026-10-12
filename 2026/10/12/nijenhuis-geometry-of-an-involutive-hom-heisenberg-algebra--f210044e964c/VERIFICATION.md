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
The bundled checker `artifacts/verify.py` reconstructs the Hom-Heisenberg bracket
\[
[e_1,e_2]=e_3
\]
and the involution
\[
\alpha=\operatorname{diag}(1,-1,-1).
\]

It verifies multiplicativity and the Hom-Jacobi identity on every ordered basis tuple.

For the complete twist-centralizer
\[
N=
\begin{pmatrix}
a&0&0\\
0&b&d\\
0&c&e
\end{pmatrix},
\]
it symbolically reconstructs all basis-pair Nijenhuis defects. They force
\[
d=0
\]
and then reduce exactly to
\[
(a-e)(b-e)=0.
\]

The checker exhaustively enumerates the whole five-parameter twist-centralizer over
\[
\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7,\quad\mathbf F_{11}.
\]
It obtains totals
\[
45,\quad225,\quad637,\quad2541
\]
and rank profiles
\[
(1,10,16,18),
\quad
(1,28,56,140),
\quad
(1,54,120,462),
\quad
(1,130,320,2090).
\]

It verifies zero-deformation counts
\[
15,\quad45,\quad91,\quad231
\]
and conjugacy-class counts
\[
24,\quad70,\quad140,\quad352.
\]
For \(\mathbf F_3\) and \(\mathbf F_5\), every Hom-Lie automorphism and every conjugacy orbit is constructed explicitly.

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field classification, orbit normal forms, and extension-field formulas are proved symbolically in `RESULT.md`.
