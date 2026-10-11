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

For
\[
f_1=e_1,\qquad f_2=e_2,
\]
\[
g_1=(1,-1),\qquad g_2=(1,1),
\]
the mixed operator is
\[
T_FT_G^*
=
\begin{pmatrix}
1&-1\\
1&1
\end{pmatrix}
=
I+J,
\qquad
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]
Direct multiplication gives
\[
J^*=-J
\]
and
\[
\frac{T_FT_G^*+T_GT_F^*}{2}=I.
\]

For
\[
f=(x,y),
\]
\[
\langle f,g_1\rangle\langle f_1,f\rangle
+
\langle f,g_2\rangle\langle f_2,f\rangle
=
(x-y)x+(x+y)y
=
x^2+y^2.
\]
Thus the scalar condition for \(K=I\) holds for every vector.

Reconstruction is different:
\[
T_FT_G^*e_1=e_1+e_2\ne e_1.
\]
The Gram operator of \(G\) is
\[
2I,
\]
so \(G\) is a tight Riesz basis and the example is nondegenerate.

For the general repair, let
\[
D=K-T_FT_G^*.
\]
The dense-set scalar equality extends by continuity. Real polarization gives
\[
\langle Df,f\rangle=0\ \text{for all }f
\quad\Longleftrightarrow\quad
D+D^*=0,
\]
which, because \(K=K^*\), is equivalent to
\[
K=
\frac{T_FT_G^*+T_GT_F^*}{2}.
\]

For any bounded skew-adjoint \(J\), the construction
\[
g_j=(I-J)e_j
\]
has mixed operator \(I+J\). Also
\[
\|(I-J)x\|^2=\|x\|^2+\|Jx\|^2,
\]
and the adjoint \(I+J\) satisfies the same lower estimate, so \(I-J\) is boundedly invertible and the resulting \(G\) is a Riesz basis.

The complete primary article, including Remark 1.2 and its proof, was materially inspected. The matrix identities were independently replayed from the displayed data. No finite experiment is used to justify an infinite-dimensional statement.
