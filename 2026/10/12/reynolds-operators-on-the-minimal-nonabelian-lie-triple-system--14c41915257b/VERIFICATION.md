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
The packaged checker `artifacts/verify.py` reconstructs the Lie triple product
\[
[e_1,e_2,e_2]=e_1
\]
and the Reynolds identity
\[
[Rx,Ry,Rz]
=
R([Rx,Ry,z]+[x,Ry,Rz]+[Rx,y,Rz]-[Rx,Ry,Rz]).
\]

It symbolically evaluates every ordered basis triple for
\[
R=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
\]
and confirms the polynomial system used in `RESULT.md`.

It exhaustively tests every \(2\times2\) matrix over
\[
\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7,\quad\mathbf F_{11}.
\]
The totals are
\[
27,\quad85,\quad175,\quad451,
\]
and the rank profiles are
\[
(1,20,6),\quad
(1,64,20),\quad
(1,132,42),\quad
(1,340,110).
\]

For every tested matrix, direct satisfaction of the Reynolds identity agrees exactly with membership in the claimed union of three affine planes and the square-zero cone.

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field result follows from the exact polynomial proof in `RESULT.md`.
