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

Take
\[
K=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
\Lambda_1=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
\Phi_1=
\begin{pmatrix}
1&\delta\\
0&0
\end{pmatrix},
\]
with \(0<\delta<1\).

Then
\[
\|\Lambda_1f\|^2=\|K^*f\|^2,
\]
so the original one-block family has \(K\)-frame bounds \(A=B=1\).

Moreover
\[
\Lambda_1-\Phi_1=
\begin{pmatrix}
0&-\delta\\
0&0
\end{pmatrix},
\]
whose operator norm is exactly \(\delta\). Thus the perturbation hypothesis holds with
\[
a=b=0,\qquad c=\delta.
\]
Because \(K^\dagger=K\),
\[
\frac{c}{1-a}=\delta<1=\frac{\sqrt A}{\|K^\dagger\|}.
\]

For
\[
f_\delta=
\begin{pmatrix}
-\delta\\
1
\end{pmatrix},
\]
we have
\[
\Phi_1f_\delta=0
\]
but
\[
K^*f_\delta=
\begin{pmatrix}
-\delta\\
0
\end{pmatrix}.
\]
Hence the claimed lower inequality fails.

For the repair, closed range gives
\[
(K^\dagger)^*K^*=P_{R(K)}.
\]
Therefore every \(g\in R(K)\) satisfies
\[
\|g\|\le\|K^\dagger\|\,\|K^*g\|.
\]
If \(W_j\subseteq R(K)\) for all \(j\), replace any test vector \(f\) by \(g=P_{R(K)}f\). All analysis energies are unchanged and \(K^*g=K^*f\), so the proof of the lower bound becomes valid.

The open publisher HTML and the PDF theorem pages were inspected directly. No numerical approximation or finite search is used.
