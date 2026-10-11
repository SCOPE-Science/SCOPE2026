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
K=
\begin{pmatrix}
2&0\\
0&1/2
\end{pmatrix},
\qquad
K^\dagger=
\begin{pmatrix}
1/2&0\\
0&2
\end{pmatrix}.
\]
Choose
\[
F=(e_1,e_2,0,\ldots),
\qquad
G=(2e_1^*,0,0,\ldots).
\]

The mixed reconstruction matrices are
\[
T_FR_G=
T_GR_F=
\begin{pmatrix}
2&0\\
0&0
\end{pmatrix}.
\]
Therefore
\[
K-T_FR_G
=
K^*-T_GR_F
=
\begin{pmatrix}
0&0\\
0&1/2
\end{pmatrix},
\]
and both operator norms equal \(1/2<1\).

On the other hand,
\[
K^\dagger T_FR_G
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\]
so the operator asserted invertible in Lemma 19 is singular.

For the claimed \(K\)-frame conclusion,
\[
R_Ge_2=0,
\qquad
Ke_2=\frac12e_2.
\]
Thus no positive lower \(K\)-frame bound exists.

For the repair, an injective operator with generalized inverse satisfies
\[
K^\dagger K=I
\]
because
\[
K(K^\dagger K-I)=0.
\]
Hence
\[
I-K^\dagger T_FR_G
=
K^\dagger(K-T_FR_G).
\]
The condition
\[
\|K^\dagger\|\,\|K-T_FR_G\|<1
\]
implies invertibility by the Neumann lemma. The counterexample has
\[
\|K^\dagger\|\,\|K-T_FR_G\|
=
2\cdot\frac12
=
1,
\]
and singularity occurs at that boundary.

The source statement, its hypotheses, and the proof's Neumann step were checked in the open publisher full text. The verification uses exact matrix identities only.
