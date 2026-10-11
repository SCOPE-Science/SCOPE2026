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
P=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix},
\qquad
Q=
\begin{pmatrix}
1&19/20\\
19/20&1
\end{pmatrix}.
\]
The eigenvalues of \(P\) are \(2,1\). Since \(Q\) has diagonal entries \(1\) and off-diagonal entries \(19/20\), its eigenvalues are
\[
\frac{39}{20},\qquad \frac1{20}.
\]
Thus both controls are positive invertible.

For the one-point identity continuous \(g\)-frame,
\[
q(f)=\langle Pf,Qf\rangle.
\]
Writing \(f=(x,y)^{\mathsf T}\),
\[
q(f)=2x^2+\frac{57}{20}xy+y^2.
\]
At
\[
f_0=(1,-3/2)^{\mathsf T},
\]
\[
q(f_0)
=
2-\frac{171}{40}+\frac94
=
-\frac1{40}.
\]
Therefore no positive lower controlled-frame bound exists.

As an independent algebraic check,
\[
\frac{PQ+QP}{2}
=
\begin{pmatrix}
2&57/40\\
57/40&1
\end{pmatrix}
\]
has determinant
\[
-\frac{49}{1600}.
\]
Hence the quadratic form is indefinite.

For a general ordinary continuous \(g\)-frame with frame operator \(S_\Lambda\),
\[
\int_\Omega
\langle\Lambda_\omega Pf,\Lambda_\omega Qf\rangle\,d\mu(\omega)
=
\langle Q S_\Lambda P f,f\rangle.
\]
The controlled inequalities are therefore equivalent to
\[
A I_H\le Q S_\Lambda P\le B I_H
\]
for some \(0<A\le B<\infty\), which is equivalent to
\[
Q S_\Lambda P\in GL^+(H).
\]

The arXiv PDF was inspected both as extracted text and as a page image at the complete statement and proof of Theorem 2.1. The final journal text was inspected at the same theorem, Corollary 2.2, the controlled frame operator, and the primary MSC metadata. All computations above are exact.
