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
The packaged checker `artifacts/verify.py` reconstructs the complete Nijenhuis system directly from
\[
e_1^2=e_2,\qquad e_1e_2=e_2e_1=e_3.
\]

It derives the following necessary consequences in order:
\[
x_{13}=0,\qquad
x_{23}=0,\qquad
x_{12}=0,
\]
\[
x_{22}=x_{11},\qquad
x_{33}=x_{11}.
\]

It then substitutes
\[
N_{a,b,c,d}
=
\begin{pmatrix}
a&0&0\\
b&a&0\\
c&d&a
\end{pmatrix}
\]
back into every defining equation and verifies that all defects vanish.

The checker independently constructs the automorphism matrix from
\[
\phi(e_1)=u e_1+v e_2+w e_3
\]
and verifies
\[
\phi(e_2)=u^2e_2+2uv\,e_3,\qquad
\phi(e_3)=u^3e_3.
\]

Symbolic conjugation verifies
\[
(a,b,c,d)\mapsto
(a,ub,u^2c+v(2b-d),ud).
\]

Finally, exhaustive finite-field enumeration for
\[
q=2,\quad3,\quad5,\quad7
\]
gives respectively
\[
12,\quad27,\quad65,\quad119
\]
conjugacy classes, exactly matching
\[
q\bigl(2q+1+\gcd(2,q-1)\bigr).
\]

The checker returns `VERIFY_OK`.

The finite enumeration is a replay check and is not used in place of the symbolic proof.
