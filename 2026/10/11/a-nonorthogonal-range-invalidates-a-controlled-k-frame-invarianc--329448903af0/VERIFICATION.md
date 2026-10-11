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

Set
\[
T=
\begin{pmatrix}
1&1\\
0&0
\end{pmatrix},
\qquad
K=
\begin{pmatrix}
0&-1\\
0&1
\end{pmatrix}.
\]
Exact multiplication gives
\[
T^2=T,\qquad TK=KT=0.
\]
Thus \(T\) has closed range and \(R(TK)=\{0\}\).

The adjoint is
\[
K^*=
\begin{pmatrix}
0&0\\
-1&1
\end{pmatrix}.
\]
For
\[
\psi=(-1,1)
\]
and
\[
x=(x_1,x_2),
\]
one has
\[
|\langle x,\psi\rangle|^2
=
|-x_1+x_2|^2
=
\|K^*x\|^2.
\]
Hence \(\{\psi\}\) is a Parseval \(K\)-frame.

But
\[
T\psi=0.
\]
For
\[
e_1\in R(T),
\]
\[
K^*e_1=(0,-1),
\]
so the required lower \(K\)-frame inequality fails.

The exact Moore--Penrose inverse is
\[
T^\dagger=
\begin{pmatrix}
1/2&0\\
1/2&0
\end{pmatrix},
\]
hence
\[
TT^\dagger=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
\]
Therefore
\[
(TT^\dagger)^*K^*e_1=0
\ne
K^*e_1.
\]
This is the precise projection error in the theorem proof.

The preprint theorem and the published theorem were inspected in their full text at the complete proof. No numerical approximation or finite experimental search is used as mathematical evidence.
