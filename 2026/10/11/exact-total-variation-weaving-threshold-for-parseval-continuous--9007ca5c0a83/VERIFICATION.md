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

For a unit vector \(f\), write \(a=a_f\), \(b=b_f\) with
\[
\int_Xa\,d\mu=\int_Xb\,d\mu=1.
\]
Then
\[
\int_X\min(a,b)\,d\mu=\frac12\int_X(a+b-|a-b|)\,d\mu=1-\frac12\int_X|a-b|\,d\mu,
\]
\[
\int_X\max(a,b)\,d\mu=1+\frac12\int_X|a-b|\,d\mu.
\]
Choose \(\sigma_f=\{a_f\le b_f\}\) to attain the former as a weaving energy, and choose \(\{a_f\ge b_f\}\) for the latter. Since \(\inf_\sigma\inf_f=\inf_f\inf_\sigma\) and \(\sup_\sigma\sup_f=\sup_f\sup_\sigma\), the optimal universal bounds are exactly \(1-\tau\) and \(1+\tau\), without a common optimizing partition.

Write \(D_\sigma=S_{1,\sigma}-S_{2,\sigma}\), which is self-adjoint. Then \(\|D_\sigma\|=\sup_{\|f\|=1}|\int_\sigma(a_f-b_f)|\); as this scalar signed density has zero total mass, \(\sup_\sigma|\int_\sigma(a_f-b_f)|=\tfrac12\int_X|a_f-b_f|\). Exchange the suprema to obtain \(\tau=\sup_\sigma\|D_\sigma\|\). All woven frame operators are \(I+D_\sigma\), and taking complements changes the sign, confirming both optimal constants.

For the exact two-point model use
\[
A_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad A_2=\begin{pmatrix}0&0\\0&1\end{pmatrix},
\]
\[
B_1=\begin{pmatrix}1-t&0\\0&t\end{pmatrix},\quad B_2=\begin{pmatrix}t&0\\0&1-t\end{pmatrix},\quad 0\le t\le1.
\]
Both pairs sum to \(I\), so their square roots are valid Parseval analysis maps. The signed energy differences at the two atoms are equal and opposite, with absolute magnitude \(t\bigl||f_1|^2-|f_2|^2\bigr|\). Hence \(\tau=t\). The two mixed weaves have diagonal eigenvalues \((1+t,1-t)\) and \((1-t,1+t)\); both optimal bounds are realized at every \(t\). At \(t=1\), a mixed weave is \(2P_1\), with kernel \(\operatorname{span}\{e_2\}\), though each source sum remains \(I\). Equivalently, to realize this boundary example with one common fibre map, set \(\Lambda(1)=\Lambda(2)=I_H\), \(F(1)=\operatorname{span}\{e_1\}\), \(F(2)=\operatorname{span}\{e_2\}\), \(G(1)=\operatorname{span}\{e_2\}\), and \(G(2)=\operatorname{span}\{e_1\}\), with unit weights.

The 2021 primary preprint was inspected at its frame and weaving definitions and complete Theorem 2.15 proof, including its rendered theorem page. This exhibits the distinction between an integrated positive difference and positivity of local differences; the latter is a stronger condition and is not met in the boundary example. Foundational weaving-frame and generalized-frame source sections were also compared for implication-level coverage.
