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
P_1=
\begin{pmatrix}
1&-1\\
-1&2
\end{pmatrix},
\qquad
P_2=
\begin{pmatrix}
1&-1\\
-1&3
\end{pmatrix},
\qquad
R=
\begin{pmatrix}
1&1\\
0&2
\end{pmatrix}.
\]
Then
\[
Q_1=P_1R=P_2,
\qquad
Q_2=P_2R=
\begin{pmatrix}
1&-1\\
-1&5
\end{pmatrix}.
\]
The determinants of \(P_1,P_2,Q_2\) are \(1,2,4\), respectively, and all have positive trace, hence all are positive definite.

Because \(R\) is invertible,
\[
\{(Q_1x,Q_2x):x\in H\}
=
\{(P_1x,P_2x):x\in H\}.
\]
Thus the representation spaces used by the source coincide.

Direct multiplication gives
\[
A=P_1Q_1=
\begin{pmatrix}
2&-4\\
-3&7
\end{pmatrix},
\qquad
B=P_2Q_2=
\begin{pmatrix}
2&-6\\
-4&16
\end{pmatrix},
\]
and
\[
K=A+B=
\begin{pmatrix}
4&-10\\
-7&23
\end{pmatrix}.
\]
Therefore the dual condition
\[
T_\Lambda T_{\widetilde\Lambda}^*=K
\]
holds exactly.

At
\[
f=(1,i),
\]
exact complex arithmetic gives
\[
\langle Af,Bf\rangle=152-24i,
\qquad
\langle Bf,Af\rangle=152+24i
\]
for the conjugate-linear-first convention. The opposite convention conjugates both values and therefore still leaves them unequal.

Finally,
\[
\operatorname{Re}\langle Af,Bf\rangle
=
\operatorname{Re}\langle Bf,Af\rangle
\]
identically, proving the repaired formula.

The actual published theorem page and complete proof were inspected, as were the representation-space synthesis/analysis definitions in the precursor paper. No numerical approximation or experimental extrapolation is used.
