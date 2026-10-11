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
\Lambda_1=
\begin{pmatrix}
\sqrt2&1/\sqrt2\\
0&\sqrt{3/2}
\end{pmatrix},
\]
direct multiplication gives
\[
\Lambda_1^*\Lambda_1=
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix}.
\]
The characteristic polynomial is
\[
(\lambda-1)(\lambda-3),
\]
so the frame operator is positive with lower eigenvalue \(1\) and upper eigenvalue \(3\).

With
\[
K=P_{\operatorname{span}\{e_1\}},
\]
the \(K\)-\(g\)-fusion lower inequality follows from
\[
\langle S_\Lambda f,f\rangle
\ge
\|f\|^2
\ge
\|K^*f\|^2.
\]

The restricted map
\[
C=S_\Lambda|_{R(K)}
\]
sends
\[
e_1\longmapsto2e_1+e_2.
\]
Using the normalized vector
\[
q=\frac{2e_1+e_2}{\sqrt5},
\]
one obtains
\[
C^{-1}q=\frac1{\sqrt5}e_1
\]
and therefore
\[
(C^{-1})^*e_1
=
\frac{2e_1+e_2}{5}.
\]
Applying \(S_\Lambda\) yields
\[
S_\Lambda(C^{-1})^*e_1
=
e_1+\frac45e_2,
\]
which is not \(Ke_1\).

For the general obstruction, let
\[
R=R(K),\qquad C=S_\Lambda|_R.
\]
Since \(K\) maps onto \(R\), the source identity is equivalent to
\[
S_\Lambda(C^{-1})^*|_R=I_R.
\]
Because
\[
C^*=P_RS_\Lambda|_{S_\Lambda(R)}
\]
and \((C^{-1})^*=(C^*)^{-1}\), this is equivalent to
\[
S_\Lambda^2(R)\subseteq R.
\]
The subspace \(R\) then reduces the self-adjoint operator \(S_\Lambda^2\), and functional calculus for its positive square root gives
\[
S_\Lambda(R)\subseteq R.
\]
The converse follows because the restricted positive operator is then self-adjoint and invertible on \(R\).

The source theorem and the later journal reproduction were inspected directly, and the related \(K\)-fusion reconstruction was checked in full text. No numerical approximation is used.
