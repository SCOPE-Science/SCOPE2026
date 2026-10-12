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
The packaged checker `artifacts/verify.py` reconstructs the Nijenhuis torsion equations from the multiplication table
\[
[e_2,e_1]=[e_2,e_2]=e_1.
\]

For a general matrix
\[
N=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]
it verifies that the defining equations reduce over a field to
\[
c=0,
\qquad
(a-d)(a-b-d)=0.
\]

It separately derives the complete automorphism equations and verifies
\[
\operatorname{Aut}(L)=\left\{\begin{pmatrix}t&t-1\\0&1\end{pmatrix}:t\ne0\right\}.
\]
It checks the conjugation formula and both normal-form families symbolically.

Finally, it exhaustively enumerates all endomorphisms and automorphisms over
\[
\mathbf F_2,\quad\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7
\]
and computes every conjugacy orbit directly. In each case it obtains
\[
2q^2-q
\]
Nijenhuis operators and
\[
q^2+q
\]
conjugacy classes.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the arbitrary-field theorem.
