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

Use the matrices
\[
K=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
U=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
U^*=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
\]
With one block \(W=H\), unit weight, identity controls, and \(\Lambda=K\),
\[
\|\Lambda f\|^2=\|K^*f\|^2,
\]
so the original family is Parseval.

For \(f=(x,y)^T\),
\[
U^*f=(0,x)^T,
\]
hence
\[
\|U^*f\|=|x|=\|K^*f\|.
\]
Also
\[
R(U)=R(K)=\operatorname{span}\{e_1\}.
\]

The transformed fusion subspace is
\[
UW=\operatorname{span}\{e_1\},
\]
so
\[
U^*P_{UW}(x,y)^T=(0,x)^T
\]
and
\[
KU^*P_{UW}(x,y)^T=0.
\]
Therefore the transformed analysis energy is zero for every vector, while \(\|K^*e_1\|=1\).

For closed-range \(K\),
\[
(K^\dagger)^*K^*=P_{R(K)}.
\]
Thus the source equality
\[
U^*f=(K^\dagger)^*K^*U^*f
\]
holds for all \(f\) exactly when
\[
R(U^*)\subseteq R(K).
\]
Under that extra condition,
\[
\|U^*f\|
\le
\|K^\dagger\|\|K^*U^*f\|,
\]
and the published scalar lower condition yields the corrected transformed lower bound
\[
A_{CC'}\delta^2\|K^\dagger\|^{-2}.
\]

The publisher PDF theorem statement, proof, and page image were inspected directly. All computations above are exact symbolic calculations.
