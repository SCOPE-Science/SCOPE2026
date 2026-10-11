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
F=\{e_1\}.
\]
For every
\[
x=(x_1,x_2),
\]
\[
\sum_{f\in F}|\langle x,f\rangle|^2
=
|x_1|^2
=
\|K^*x\|^2.
\]
Thus \(F\) is Parseval relative to \(K\).

Its frame operator is
\[
S=KK^*=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
\]
Hence the eigenvalues are \(1\) and \(0\). The total frame energy is
\[
\sum_{f\in F}\|f\|^2=1.
\]
For the standard eigenbasis,
\[
2\|K^*e_1\|^2=2,
\qquad
2\|K^*e_2\|^2=0.
\]
This exactly contradicts both parts of Proposition 2.2.

In general, for an orthonormal eigenbasis of
\[
S=KK^*,
\]
\[
\lambda_k=\|K^*e_k\|^2
\]
and
\[
\sum_j\|f_j\|^2
=
\operatorname{tr}(S)
=
\sum_k\lambda_k.
\]
The source's eigenvectorwise equality for every \(k\) is therefore equivalent to all \(\lambda_k\) being equal, which is equivalent to
\[
KK^*=cI.
\]

The target proposition, its complete proof, and its immediate consequence were inspected in the open primary full text. All mathematical checks are exact and require no numerical experiment.
