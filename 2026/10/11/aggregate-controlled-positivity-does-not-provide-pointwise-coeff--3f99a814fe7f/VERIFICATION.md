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

Use
\[
T=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix},
\qquad
U=
\begin{pmatrix}
2&1\\
1&1
\end{pmatrix},
\]
and
\[
A_1=\frac1{10}
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\qquad
A_2=
\begin{pmatrix}
2/5&-1/10\\
-1/10&9/10
\end{pmatrix}.
\]

First,
\[
A_1+A_2=
\begin{pmatrix}
1/2&0\\
0&1
\end{pmatrix}
=
T^{-1}.
\]
The matrix \(A_1\) is positive semidefinite. For \(A_2\),
\[
\det A_2=\frac7{20}>0,
\qquad
\operatorname{tr}A_2=\frac{13}{10}>0,
\]
so \(A_2\) is positive definite.

Define the two analysis maps by
\[
\Lambda_i=A_i^{1/2}.
\]
Then
\[
\sum_i
\langle\Lambda_iUf,\Lambda_iTf\rangle
=
\langle T(A_1+A_2)Uf,f\rangle
=
\langle Uf,f\rangle.
\]
The eigenvalues of \(U\) are
\[
\frac{3-\sqrt5}{2},
\qquad
\frac{3+\sqrt5}{2},
\]
which are the exact controlled-frame bounds.

For the first atom,
\[
M_1=T A_1U=
\begin{pmatrix}
3/5&2/5\\
3/10&1/5
\end{pmatrix}.
\]
At
\[
f=
\begin{pmatrix}
-3\\
5
\end{pmatrix}
\]
one gets
\[
M_1f=
\begin{pmatrix}
1/5\\
1/10
\end{pmatrix}
\]
and
\[
\langle M_1f,f\rangle=-\frac1{10}.
\]
Therefore \(M_1\) is not positive. Its unequal off-diagonal entries also show that it is not self-adjoint.

The primary source defines \(R^{1/2}\) as the positive square root of a positive self-adjoint operator and uses that notation in Proposition 3.3 and Theorem 3.4. Hence its prescribed coefficient vector is unavailable in this example.

The relevant source pages and the later discrete positivity assumption were inspected directly. No numerical approximation or finite search is used.
