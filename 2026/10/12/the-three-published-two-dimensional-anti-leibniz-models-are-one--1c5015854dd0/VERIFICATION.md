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
The proof is symbolic.

The packaged checker `artifacts/verify.py` uses exact symbolic algebra to verify the full \(A_1(a,b)\) multiplication table after the basis change
\[
f_1=e_1,
\qquad
f_2=-a e_1-\frac{a^2}{b}e_2.
\]
It confirms
\[
f_1^2=f_2,
\qquad
f_1f_2=f_2f_1=f_2^2=0,
\]
and checks that the change-of-basis determinant is
\[
-\frac{a^2}{b}.
\]

It independently verifies the canonical automorphism matrices
\[
\begin{pmatrix}
s&0\\
t&s^2
\end{pmatrix}
\]
and derivation matrices
\[
\begin{pmatrix}
r&0\\
w&2r
\end{pmatrix},
\]
together with the affine relation
\[
[H,E]=E.
\]

The checker returns `VERIFY_OK`.
