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

With \(H=V_1=V_2=\mathbb C\) and \(v_1=v_2=1\), the two local singleton frames are
\[
\varphi^{(1)}=\{2^{-1/2}\},\qquad
\varphi^{(2)}=\{\sqrt{3/2}\}.
\]
Their local operators satisfy
\[
S_1=\tfrac12 I,\qquad S_2=\tfrac32 I.
\]
The common local lower/upper bounds \(1/2\) and \(3/2\) are valid for both blocks. The fusion and global energies are
\[
\sum_i v_i^2\|P_{V_i}z\|^2=2|z|^2,
\qquad
\sum_i\sum_j|\langle z,v_i\varphi^{(i)}_j\rangle|^2=(\tfrac12+\tfrac32)|z|^2=2|z|^2.
\]
Thus \(S_V=S_{v\varphi}=2I\). The analysis operator and its closed range are
\[
C_Vz=(z,z),\qquad R=\operatorname{span}\{(1,1)\}.
\]
The local defect and compression are
\[
M=\begin{pmatrix}\tfrac12&0\\0&-\tfrac12\end{pmatrix},
\qquad
P_R=\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
Direct multiplication yields
\[
P_RMP_R=0,\qquad MC_Vz=(z/2,-z/2)\ne0\text{ for }z\ne0.
\]
Therefore the zero-compression conclusion holds while the published zero-restriction conclusion fails.

For the general criterion, the source proves
\[
S_V-S_{v\varphi}=C_V^*MC_V.
\]
Since \(C_V\) is onto \(R\), this difference is zero exactly when
\[
\langle Mr,s\rangle=0\quad(r,s\in R),
\]
which is exactly \(P_RM|_R=0\). This proof does not infer vanishing from self-adjointness alone.

For \(V_i=H=\mathbb C^d\), the equality reduces exactly to
\[
\sum_i v_i^2(S_i-I_d)=0.
\]
The positive definite operators \(S_i=I_d+T_i\) all arise from \(\{S_i^{1/2}e_k\}_{k=1}^d\), and the last deviation is uniquely forced by the first \(m-1\). The ambient real dimension is therefore \((m-1)d^2\); strict positive definiteness gives a nonempty relatively open convex set.

The primary open journal PDF was inspected at the complete target corollary and proof, with both relevant pages visually checked, and the corresponding preprint text was compared. No numerical approximation or finite enumeration is used in the proof.
