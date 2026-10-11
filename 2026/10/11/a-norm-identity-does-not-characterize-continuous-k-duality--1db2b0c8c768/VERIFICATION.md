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
1&0\\
0&0
\end{pmatrix}
\]
on \(\mathbb C^2\), and take the two-point Parseval continuous frame
\[
f(1)=g(1)=e_1,
\qquad
f(2)=g(2)=e_2.
\]

For
\[
h=(a,b),
\]
one has
\[
Kh=(a,0)
\]
and therefore
\[
\sum_{j=1}^2
\langle h,g(j)\rangle
\langle f(j),Kh\rangle
=
a\overline a
=
|a|^2
=
\|Kh\|^2.
\]
Since \(K=K^*\), the second scalar identity is identical.

The reconstruction operator is
\[
T_fT_g^*=I.
\]
Hence
\[
T_f(\langle e_2,g\rangle)=e_2
\]
but
\[
Ke_2=0.
\]
The pair is not a \(K\)-dual pair.

For the exact defect formula, write
\[
M=T_fT_g^*.
\]
The scalar identity is
\[
\langle (M-K)h,Kh\rangle=0
\]
for all \(h\). Complex polarization yields
\[
(M-K)^*K=0,
\]
equivalently
\[
K^*(M-K)=0.
\]
Thus
\[
R(M-K)\subseteq N(K^*)
=
\overline{R(K)}^\perp.
\]
In the explicit example,
\[
M-K=I-K
\]
is exactly the orthogonal projection onto that invisible complementary subspace.

The complete target theorem and proof were inspected in the first public preprint and journal version. No numerical approximation or finite experimental extrapolation is used.
