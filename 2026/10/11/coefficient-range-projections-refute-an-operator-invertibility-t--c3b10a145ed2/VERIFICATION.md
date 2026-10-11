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
\Lambda_1=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
\Lambda_2=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
T=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
\]
For \(f=(x,y)\),
\[
\|\Lambda_1f\|^2+\|\Lambda_2f\|^2
=
|x|^2+|y|^2
=
\|f\|^2.
\]
Thus the family is Parseval for \(K=I\).

Direct matrix multiplication gives
\[
T\Lambda_1=\Lambda_1,\qquad
T\Lambda_2=\Lambda_2.
\]
Since \(T=T^*\), the same holds with \(T^*\). Therefore both transformed families are exactly the original Parseval family.

Finally,
\[
TT^*=T,
\qquad
Te_2=0,
\]
so \(TT^*\) is not invertible.

The structural extension uses only the identity \(P_M\Lambda_j=\Lambda_j\) when \(R(\Lambda_j)\subseteq M\). The sufficient repair for the ordinary \(g\)-frame case follows by factoring transformed analysis operators as \(D_TC_\Lambda\) and \(D_{T^*}C_\Lambda\) and using the bounded inverse of an onto \(g\)-frame analysis operator.

The target theorem and its proof were checked against the actual source text. No numerical experiment, partial enumeration, or approximate computation is used.
