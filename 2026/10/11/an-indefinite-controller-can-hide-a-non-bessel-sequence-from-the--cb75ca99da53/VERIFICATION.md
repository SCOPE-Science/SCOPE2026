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

Set
\[
v=\frac1{\sqrt2}
\begin{pmatrix}
1\\
1
\end{pmatrix},
\qquad
U=I,
\qquad
C=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]
For every \(j,k\),
\[
f_j=f_k=v
\]
and
\[
\langle C f_j,U f_k\rangle
=
\langle Cv,v\rangle
=
0.
\]
Hence the controlled Gram matrix is the zero operator on \(\ell^2\).

At the same time,
\[
|\langle v,f_k\rangle|^2=1
\]
for every \(k\), so
\[
\sum_{k=1}^{\infty}|\langle v,f_k\rangle|^2=\infty.
\]
The sequence is not Bessel.

For the repair, if
\[
A=U^*C\in GL^+(H),
\]
then
\[
\langle C f_j,U f_k\rangle
=
\langle A^{1/2}f_j,A^{1/2}f_k\rangle.
\]
Thus the controlled Gram matrix is an ordinary Gram matrix. A bounded ordinary Gram matrix gives a bounded synthesis map on finitely supported sequences and therefore a Bessel sequence. Since \(A^{-1/2}\) is bounded, Besselness of \(A^{1/2}f_k\) is equivalent to Besselness of \(f_k\).

The complete source proof was inspected in the first public PDF, including the page where its third case discards the \(M^\perp\) component. No numerical approximation, finite truncation, or experimental inference is used.
