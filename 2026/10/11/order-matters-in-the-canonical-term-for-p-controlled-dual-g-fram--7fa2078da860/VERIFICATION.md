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

The defining identity was checked in operator form:
\[
\Gamma\text{ is a }P\text{-controlled dual}
\iff T_{P\Lambda P}T_\Gamma^*=I.
\]
The controlled synthesis and frame operators are
\[
T_{P\Lambda P}=PT_\Lambda,
\qquad
S_{P\Lambda P}=P S_\Lambda P.
\]
Thus the canonical bounded right inverse is \(T_\Lambda^*P S_{P\Lambda P}^{-1}\), and adding an arbitrary bounded \(T\) with \(T_{P\Lambda P}T=0\) gives exactly all right inverses.

For the explicit example,
\[
S_\Lambda=\begin{pmatrix}1&0\\0&2\end{pmatrix},
\quad
P=\begin{pmatrix}2&1\\1&2\end{pmatrix},
\quad
S_{P\Lambda P}=\begin{pmatrix}6&6\\6&9\end{pmatrix}.
\]
Exact inversion and multiplication give
\[
S_{P\Lambda P}^{-1}P=\begin{pmatrix}2/3&-1/6\\-1/3&1/3\end{pmatrix}
\]
and therefore
\[
P S_\Lambda S_{P\Lambda P}^{-1}P
=\begin{pmatrix}2/3&1/3\\-2/3&7/6\end{pmatrix}\ne I.
\]
For the corrected order,
\[
P S_{P\Lambda P}^{-1}=\begin{pmatrix}2/3&-1/3\\-1/6&1/3\end{pmatrix},
\quad
P S_\Lambda P S_{P\Lambda P}^{-1}=I.
\]

The sharp boundary for the published order follows symbolically:
\[
P S_\Lambda S_{P\Lambda P}^{-1}P=I
\iff P S_\Lambda P^{-1}S_\Lambda^{-1}=I
\iff P S_\Lambda=S_\Lambda P.
\]
No numerical approximation is needed. The 2019 comparison source was checked at the primary PDF pages containing \(\Gamma_i=\Lambda_i C S_C^{-1}\).
