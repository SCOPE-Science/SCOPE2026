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
The packaged checker `artifacts/verify.py` reconstructs the ternary bracket from
\[
[e_1,e_2]=e_2
\]
using
\[
[x,y,z]=[[x,y],z].
\]

For a general matrix
\[
R=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\]
it expands the weight-zero Rota–Baxter defect on all eight ordered basis triples and verifies the four defining polynomial equations.

It independently reconstructs the affine Lie algebra's binary Rota–Baxter equations and checks that those operators form exactly the two pieces \(\mathcal B\cup\mathcal C\).

The checker derives the automorphism conditions and verifies conjugation preservation.

It then exhaustively tests every \(2\times2\) matrix over
\[
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7
\]
directly against the ternary identity.

The total counts are
\[
21,\quad65,\quad133,
\]
the rank profiles are
\[
(1,20,0),\quad
(1,64,0),\quad
(1,132,0),
\]
and the automorphism-class counts are
\[
7,\quad11,\quad15.
\]

The checker also verifies the exact orbit-size distribution:
one singleton, one orbit of size \(q-1\), \(2(q-1)\) orbits of size \(q\), and one orbit of size \(q(q-1)\).

The checker returns `VERIFY_OK`.

Finite enumeration is a replay check. The arbitrary odd-prime-power result is proved symbolically in `RESULT.md`.
