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
H=\ell^2(\mathbb N),\qquad
W_i=V_i=\operatorname{span}\{e_i\},\qquad
w_i=v_i=1.
\]
For every subset \(\sigma\subseteq\mathbb N\),
\[
\sum_{i\in\sigma}\|P_{W_i}f\|^2+
\sum_{i\in\sigma^c}\|P_{V_i}f\|^2
=
\sum_{i=1}^{\infty}|\langle f,e_i\rangle|^2
=
\|f\|^2.
\]
Thus the pair is woven with exact bounds \(1\) and \(1\).

Define
\[
K(x_1,x_2,\ldots)
=
\left(\sum_{i=1}^{\infty}2^{-i}x_i\right)e_1.
\]
Cauchy--Schwarz gives
\[
\|Kx\|
\le
\left(\sum_{i=1}^{\infty}4^{-i}\right)^{1/2}\|x\|
=
\frac1{\sqrt3}\|x\|.
\]
Hence \(K\) is bounded. Since \(K e_i=2^{-i}e_1\ne0\),
\[
K W_i=K V_i=\operatorname{span}\{e_1\}
\]
for all \(i\). These image subspaces are closed and \(R(K)=\operatorname{span}\{e_1\}\) is closed.

For \(f=e_1\),
\[
\sum_{i=1}^{\infty}\|P_{K W_i}f\|^2
=
\sum_{i=1}^{\infty}1
=
\infty.
\]
Thus the transformed family is not a fusion Bessel sequence and cannot be a \(K\)-fusion frame.

The source PDF was inspected at Proposition 1.5 and Proposition 2.5, including the complete proof. Proposition 1.5 requires the two families to be \(K\)-fusion Bessel sequences. Proposition 2.5 proves a lower estimate for the image weave and then invokes Proposition 1.5 for the upper estimate without proving that premise.

For the sufficient repair, assume the two image families have Bessel bounds \(C_W\) and \(C_V\). The lower computation in the source yields
\[
\frac{A}{\|K\|^2}\|K^*f\|^2
\le
E_\sigma(f),
\]
while Proposition 1.5 yields
\[
E_\sigma(f)\le(C_W+C_V)\|f\|^2.
\]
These bounds are uniform in \(\sigma\).

No numerical experiment or finite truncation is used.
