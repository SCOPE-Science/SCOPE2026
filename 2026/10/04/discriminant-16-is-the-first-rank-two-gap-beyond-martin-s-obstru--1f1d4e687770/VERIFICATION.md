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

The exact verifier checks the boundary lattice
\[
U(4)=
\begin{pmatrix}
0&4\\
4&0
\end{pmatrix}.
\]
It confirms
\[
\det U(4)=-16,
\]
that its pairing image is
\[
4\mathbf Z,
\]
and hence contains \(12\).

For every lattice vector \((x,y)\), the self-intersection is
\[
8xy.
\]
Therefore none of
\[
2,\ 4,\ 6,\ 12
\]
is represented, while the primitive vector \((1,1)\) has positive square \(8\).

The verifier also reconstructs the embedding into \(U^3\):
\[
a\mapsto e_1,
\qquad
b\mapsto4f_1+e_2.
\]
The two images are isotropic, have pairing \(4\), and the coordinate minor on \(e_1,e_2\) equals \(1\), proving the embedded rank-two sublattice is primitive.

For the lower-discriminant range, the mathematical proof establishes
\[
m^2\le\Delta.
\]
The verifier checks the exact integer consequence
\[
1\le\Delta<16
\quad\Longrightarrow\quad
m\le3.
\]
Thus an even rank-two Néron--Severi lattice below the boundary primitively represents self-intersection \(2\), \(4\), or \(6\).

The period-theoretic existence step and the degree-of-irrationality classification are theorem inputs rather than finite computations. The replay output ends in `VERIFY_OK`.
