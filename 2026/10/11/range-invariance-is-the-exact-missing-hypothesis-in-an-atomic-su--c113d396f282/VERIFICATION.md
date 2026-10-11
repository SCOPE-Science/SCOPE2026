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
K=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
U=
\begin{pmatrix}
1&1/2\\
1/2&1
\end{pmatrix},
\qquad
A=I+U=
\begin{pmatrix}
2&1/2\\
1/2&2
\end{pmatrix}.
\]
The eigenvalues of \(U\) are \(1/2\) and \(3/2\), so \(U\) is positive and invertible.

For the one-component family \(\Lambda_1=K^*=K\),
\[
\|\Lambda_1f\|^2=\|K^*f\|^2,
\]
hence it is a Parseval \(K\)-\(g\)-fusion frame. With
\[
f=(1,-4),
\]
direct multiplication gives
\[
Af=(0,-15/2),\qquad KAf=0,\qquad K^*f=e_1.
\]
Therefore the transported family has no positive lower \(K\)-bound.

For the universal criterion, if \(S_\Lambda\ge\alpha KK^*\), then
\[
AS_\Lambda A^*\ge\alpha AKK^*A^*.
\]
Douglas factorization gives
\[
R(K)\subseteq R(AK)
\]
if and only if there exists \(c>0\) such that
\[
KK^*\le c\,AKK^*A^*.
\]
This proves sufficiency. Necessity follows by using the one-component Parseval family whose frame operator is exactly \(KK^*\).

The source theorem and proof were inspected in the open full text, including the displayed step \(AS_\Lambda A^*\ge S_\Lambda\). No numerical approximation or finite-search inference is used.
