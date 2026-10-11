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

The source theorem assumes finite-dimensional \(H\), closed-range \(K\), and the orthogonal projection \(P\) onto \(R(K^\dagger)\), with \(KP\) of rank \(m\). It chooses a unitary \(U_F\) from a representation \(f_j=KPU_Fe_j\) and defines the proposed Grassmannian point as \(U_F^*KPU_FH\).

For the exact witness,
\[
K=\frac1{\sqrt2}\begin{pmatrix}1&0\\1&0\end{pmatrix}
\]
is a rank-one partial isometry. Direct adjoint multiplication gives
\[
K^*K=P_{e_1},
\qquad
KK^*=P_{\operatorname{span}\{(e_1+e_2)/\sqrt2\}},
\]
so \(K^\dagger=K^*\) and \(P=P_{e_1}\).

With
\[
U=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
Q=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
V=QU,
\]
one has \(KQ=K\), hence
\[
KPU=KPV=\begin{pmatrix}\frac12&\frac12\\\frac12&\frac12\end{pmatrix}.
\]
Thus the two auxiliary unitaries generate exactly the same ordered frame.

Let \(a=(e_1+e_2)/\sqrt2\). The common frame is
\[
F=(a/\sqrt2,a/\sqrt2),
\]
and for every \(x\in\mathbb C^2\),
\[
\sum_{j=1}^2|\langle x,f_j\rangle|^2
=
|\langle x,a\rangle|^2
=
\|K^*x\|^2.
\]
So it is a Parseval \(K\)-frame.

The proposed outputs are different:
\[
U^*R(K)=\operatorname{span}\{e_1\},
\qquad
V^*R(K)=\operatorname{span}\{e_2\}.
\]
Therefore the map in the theorem proof is not well-defined.

The choice-independent statement recorded in the result is
\[
R(T_F^*)=U_F^*R(K^*).
\]
It follows because \(T_F=KPU_F\), \(R(K^*)=R(K^\dagger)\), and therefore \(PK^*=K^*\). No further bijectivity claim is inferred from this identity.
