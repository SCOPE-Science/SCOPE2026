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

Let
\[
K=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
f_1=
\begin{pmatrix}
1\\
1
\end{pmatrix},
\qquad
f_2=
\begin{pmatrix}
1\\
0
\end{pmatrix}.
\]
Then
\[
S_J=f_1f_1^*+f_2f_2^*
=
\begin{pmatrix}
2&1\\
1&1
\end{pmatrix}
\]
and
\[
S_J^{-1}
=
\begin{pmatrix}
1&-1\\
-1&2
\end{pmatrix}.
\]

For \(I=\{1\}\),
\[
S_I=
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\qquad
S_{J\setminus I}
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}
=
KK^*.
\]
Hence the erased family is a Parseval \(K\)-frame.

But
\[
S_J^{-1}S_I
=
\begin{pmatrix}
0&0\\
1&1
\end{pmatrix}
\]
and therefore
\[
I-S_J^{-1}S_I
=
\begin{pmatrix}
1&0\\
-1&0
\end{pmatrix}.
\]
Its determinant is zero.

Moreover,
\[
R(K)=\operatorname{span}\{e_1\},
\]
while
\[
\left(I-S_J^{-1}S_I\right)e_1=e_1-e_2\notin R(K).
\]

The preprint theorem and the revised published theorem were inspected in their complete proofs. The corrected condition
\[
S_{J\setminus I}\ge aKK^*
\]
is exactly the lower \(K\)-\(g\)-frame inequality written in operator form. Douglas' theorem gives the equivalent range condition
\[
R(K)\subseteq R\!\left(S_{J\setminus I}^{1/2}\right).
\]

All calculations are exact symbolic identities; no numerical experiment or partial enumeration is used.
