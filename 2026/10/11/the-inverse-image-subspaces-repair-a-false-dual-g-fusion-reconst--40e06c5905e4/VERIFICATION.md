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

## Exact finite counterexample
Set \(H=\mathbb C^2\), \(P_1=\operatorname{diag}(1,0)\), and \(P_2=\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}\). Use \(W_j=\operatorname{Ran}P_j\), \(\Lambda_j=P_j\), unit weights and \(T=T_1=T_2=I\). Then
\[
S=P_1+P_2=\begin{pmatrix}3/2&1/2\\1/2&1/2\end{pmatrix},\qquad
U=S^{-1}=\begin{pmatrix}1&-1\\-1&3\end{pmatrix}.
\]
The exact checks are
\[
P_1UP_1=P_1,\qquad P_2UP_2=P_2.
\]
Thus both published reconstruction operators equal \(S\), not \(I\). On \(e_1\) the output is \((3/2,1/2)\). The original family and alleged dual are nevertheless genuine frames, so no failed-frame shortcut is used.

## Structural correction
Let \(C=\sum_j v_j^2P_{W_j}\Lambda_j^*L_j\Lambda_jP_{W_j}\) and \(U=C^{-1}\). Since \(P_{W_j}UP_{UW_j}=P_{W_j}U\), the corrected family with supports \(U W_j\) satisfies
\[
\Delta_jP_{UW_j}=\Delta_j,
\qquad
\sum_jv_j^2P_{W_j}\Lambda_j^*\Delta_jP_{UW_j}=CU=I.
\]
The adjoint gives the second reconstruction identity. Uniform local operator bounds yield positive lower bound \(m^4 A/\|C\|^2\) and upper bound \(M^4B\|C^{-1}\|^2\). This proves an infinite-index statement using bounded synthesis/analysis operators rather than treating the finite test as an infinite proof.

## Independent symbolic algebra checks
A symbolic rational two-dimensional instance used \(T=\begin{pmatrix}1&1\\0&1\end{pmatrix}\), \(T_1=2I\), \(T_2=3I\), and the two projections above. Direct exact computation gave
\[
C=\begin{pmatrix}17/2&9/2\\9/2&9/2\end{pmatrix},\qquad
U=C^{-1}=\begin{pmatrix}1/4&-1/4\\-1/4&17/36\end{pmatrix}.
\]
The reconstruction sum supported on \(U W_j\) evaluated to \(I\), whereas the sum supported on \(T W_j\) evaluated to \(\begin{pmatrix}7/5&1/5\\2/5&1/5\end{pmatrix}\ne I\). The general proof does not rely on these computations.

The 2020 journal PDF and the open manuscript were materially inspected at Theorem 3.5, Remark 3.7, Theorem 3.8, its proof, and its projection lemma. Heineken--Morillas and Ahmadi et al. were inspected at their relevant canonical-dual results. No numerical approximation, timeout inference, or unsupported automated certificate is used.
