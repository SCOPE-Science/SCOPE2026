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

Use
\[
T_\Lambda=
\begin{pmatrix}
1&0&0\\
0&1/\sqrt2&1/\sqrt2
\end{pmatrix},
\qquad
K=
\begin{pmatrix}
1&0\\
0&1/2
\end{pmatrix}.
\]
Then
\[
T_\Lambda T_\Lambda^*=I.
\]

For real \(c\), set
\[
V_c=
\begin{pmatrix}
1&0\\
0&(1/2+c)/\sqrt2\\
0&(1/2-c)/\sqrt2
\end{pmatrix}.
\]
Exact multiplication gives
\[
T_\Lambda V_c=K
\]
and
\[
V_c^*V_c=
\begin{pmatrix}
1&0\\
0&1/4+c^2
\end{pmatrix}.
\]
Therefore
\[
\|V_c\|=1
\]
for
\[
|c|\le\sqrt3/2.
\]

For any solution \(V\) of
\[
T_\Lambda V=K,
\]
submultiplicativity gives
\[
1=\|K\|\le\|T_\Lambda\|\,\|V\|=\|V\|.
\]
Thus all displayed \(V_c\) are global norm minimizers.

The synthesis kernel is
\[
N(T_\Lambda)=\operatorname{span}\{(0,1,-1)\}.
\]
The member
\[
V_0=T_\Lambda^*K
\]
has range in
\[
R(T_\Lambda^*)=N(T_\Lambda)^\perp,
\]
whereas
\[
(V_c-V_0)(x_1,x_2)
=
\frac{cx_2}{\sqrt2}(0,1,-1).
\]
Hence \(c=0\) is the Douglas reduced solution and nonzero \(c\) are equal-norm kernel perturbations.

The target proposition, its complete proof, the source's Douglas lemma, and later canonical-dual characterizations were materially inspected. No numerical approximation or finite experimental extrapolation is used.
