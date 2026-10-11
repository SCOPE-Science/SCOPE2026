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
S=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix},
\qquad
T=U=
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix}.
\]
Then
\[
TST=
\begin{pmatrix}
6&6\\
6&9
\end{pmatrix}.
\]
Its characteristic polynomial is
\[
\lambda^2-15\lambda+18,
\]
so its eigenvalues are
\[
\frac{15\pm3\sqrt{17}}2.
\]
Both are positive.

Also,
\[
T^2=
\begin{pmatrix}
5&4\\
4&5
\end{pmatrix}.
\]
With
\[
\Lambda=
\begin{pmatrix}
1&0\\
0&\sqrt2
\end{pmatrix}
\]
and
\[
f=(1,i),
\]
the source-definition target mixed form is
\[
\langle \Lambda f,\Lambda T^2 f\rangle
=
15+4i
\]
under the source convention, hence is not real.

The relevant source proof was checked at the exact step
\[
\langle TSU f,f\rangle
=
\langle STU f,f\rangle.
\]
This equality is valid if
\[
TS=ST.
\]
The source later includes exactly this type of frame-operator commutation hypothesis in Theorem 3.10.

All calculations are exact symbolic matrix identities; no numerical approximation or finite search is used as mathematical evidence.
