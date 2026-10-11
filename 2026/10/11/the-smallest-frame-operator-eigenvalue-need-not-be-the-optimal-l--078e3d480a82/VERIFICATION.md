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

Take
\[
K=\begin{pmatrix}2&0\\0&1\end{pmatrix},
\qquad
\Phi=\{2e_1,e_2\}.
\]
The frame operator is
\[
S=\begin{pmatrix}4&0\\0&1\end{pmatrix}=KK^*.
\]
For \(x=(x_1,x_2)\),
\[
\sum_{\phi\in\Phi}|\langle x,\phi\rangle|^2
=4|x_1|^2+|x_2|^2
=\|K^*x\|^2.
\]
Thus the optimal lower \(K\)-frame bound is \(1\). Since
\[
\lambda_{\min}(S)=1,
\qquad
\|K\|^2=4,
\]
the published formula gives \(1/4\).

For positive definite \(S\),
\[
A\|K^*x\|^2\le\langle Sx,x\rangle\quad\text{for all }x
\]
is equivalent to
\[
A(S^{-1/2}K)(S^{-1/2}K)^*\le I.
\]
Therefore
\[
A_{\mathrm{opt}}=\frac{1}{\|S^{-1/2}K\|^2}.
\]

The source estimate follows by composing
\[
\langle Sx,x\rangle\ge\lambda_{\min}(S)\|x\|^2
\]
with
\[
\|K^*x\|^2\le\|K\|^2\|x\|^2.
\]
In finite dimension, equality in the resulting optimal-bound estimate occurs exactly when one nonzero vector saturates both inequalities, namely when
\[
E_{\lambda_{\min}(S)}(S)\cap E_{\|K\|^2}(KK^*)\ne\{0\}.
\]

The primary proposition and its proof were inspected in the publisher full text, and the later repetition was inspected in its open full text. All mathematical checks are exact symbolic calculations.
