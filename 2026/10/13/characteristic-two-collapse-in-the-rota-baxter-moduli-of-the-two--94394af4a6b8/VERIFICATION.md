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
The packaged checker `artifacts/verify.py` reconstructs the complete weight-zero Rota--Baxter system from the single bracket
\[
[e_1,e_1]=e_2.
\]

For
\[
R=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\]
it obtains polynomial generators equivalent over a field to
\[
b=0,\qquad a(a-2d)=0.
\]

The checker then derives the automorphism family
\[
\phi_{u,v}
=
\begin{pmatrix}
u&0\\
v&u^2
\end{pmatrix},
\qquad u\ne0,
\]
and verifies the conjugation formula
\[
(a,c,d)
\mapsto
\left(a,\,
uc+\frac{v(a-d)}u,\,
d\right).
\]

Finally it exhaustively enumerates all operators and automorphism orbits over
\[
\mathbf F_2,\quad
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7.
\]
The operator/orbit counts are
\[
(4,3),\quad(15,6),\quad(45,10),\quad(91,14),
\]
matching the theorem.

The checker returns `VERIFY_OK`.

Finite enumeration is a replay check and is not used in place of the arbitrary-field proof.
