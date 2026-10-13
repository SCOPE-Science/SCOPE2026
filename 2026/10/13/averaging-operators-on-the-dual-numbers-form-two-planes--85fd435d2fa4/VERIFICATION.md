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
The packaged checker `artifacts/verify.py` reconstructs the full averaging equations from the dual-number multiplication
\[
\varepsilon^2=0.
\]

For a general matrix
\[
T=
\begin{pmatrix}
a&c\\
b&d
\end{pmatrix},
\]
it derives exactly
\[
bc=0,\qquad b(a-d)=0,\qquad cd=0,\qquad d(a-d)=0.
\]

It verifies symbolically that the two claimed affine-plane families satisfy both averaging identities.

It then exhaustively checks
\[
\mathbf F_2,\quad\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7.
\]
For each field it enumerates every linear operator, tests the identity on all ordered basis pairs, enumerates every algebra automorphism, and computes every conjugacy orbit.

The observed counts equal
\[
2q^2-1
\]
operators and
\[
4q-1
\]
orbits for every tested \(q\).

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the arbitrary-field theorem.
