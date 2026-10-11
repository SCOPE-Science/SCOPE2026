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

For
\[
I=J=\{1,2\},
\qquad
H_i=K_j=\mathbb R,
\]
a displayed coefficient family in Note 3.2 has matrix form
\[
M=
\begin{pmatrix}
f_1g_1&f_1g_2\\
f_2g_1&f_2g_2
\end{pmatrix}.
\]
Direct calculation gives
\[
\det M=0.
\]
The matrices
\[
A=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}
\]
are both of the prescribed form, but
\[
\det(A+B)=1.
\]
Thus the displayed set is not closed under addition.

For the repaired spaces
\[
E=\bigoplus_i^{\ell^2}H_i,
\qquad
F=\bigoplus_j^{\ell^2}K_j,
\qquad
G=\bigoplus_{i,j}^{\ell^2}(H_i\otimes K_j),
\]
the canonical map on simple tensors satisfies
\[
\|U((f_i)_i\otimes(g_j)_j)\|_G^2
=
\left(\sum_i\|f_i\|^2\right)
\left(\sum_j\|g_j\|^2\right).
\]
Finite-support elementary tensors are dense in \(G\), so \(U\) extends to a unitary.

On simple coefficient tensors, direct expansion of the synthesis sum gives
\[
T_{\Lambda\otimes\Gamma}U
=
T_\Lambda\otimes T_\Gamma.
\]
Density and boundedness extend this identity to the completed spaces; taking adjoints gives the corrected analysis identity.

The open primary PDF was inspected at Note 3.2, Note 3.5, and Theorem 3.6, including page images of Note 3.2 and the synthesis calculation in Theorem 3.6. No numerical approximation or finite search is used in the proof.
