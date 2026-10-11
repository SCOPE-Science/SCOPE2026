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
U=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
U^*=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
\]
Then
\[
R(U)=R(K)=\operatorname{span}\{e_1\}.
\]

With one component
\[
W_1=H,\qquad \Lambda_1=K,\qquad v_1=1,
\]
the original coefficient energy is
\[
\|\Lambda_1f\|^2=\|K^*f\|^2.
\]
Thus the original family is Parseval relative to \(K\).

For \(f=(f_1,f_2)\),
\[
U^*f=(0,f_1),
\]
so
\[
\|U^*f\|=|f_1|=\|K^*f\|.
\]
The source's lower comparison therefore holds with \(\delta=1\).

But
\[
KU^*=0.
\]
Hence every transformed coefficient vanishes. At \(e_1\),
\[
\|K^*e_1\|^2=1
\]
while the transformed coefficient energy is zero.

Since \(K\) is an orthogonal projection,
\[
K^\dagger=K
\]
and
\[
(K^\dagger)^*K^*=K.
\]
Thus
\[
(K^\dagger)^*K^*U^*e_1=0
\]
although
\[
U^*e_1=e_2.
\]
This directly verifies failure of the source proof identity.

For a general transformed family, direct expansion of the coefficient energy gives
\[
S_\Gamma=US_\Lambda U^*.
\]
Therefore the exact lower-frame condition is
\[
US_\Lambda U^*\ge cKK^*
\]
for some \(c>0\), with the equivalent Douglas range condition
\[
R(K)\subseteq R(US_\Lambda^{1/2}).
\]

The published theorem, the related earlier preprint, and the later adjoint-range version were materially inspected. No numerical approximation or finite experimental inference is used.
