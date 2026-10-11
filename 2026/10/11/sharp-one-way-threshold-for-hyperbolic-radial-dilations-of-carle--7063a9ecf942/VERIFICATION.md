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

Write the hyperbolic metric as
\[
d\ell^2=dR^2+\sinh^2R\,d\theta^2.
\]
For
\[
D_a(R,\theta)=(aR,\theta),
\]
the inverse has differential stretches
\[
\frac1a
\quad\text{and}\quad
\frac{\sinh(R/a)}{\sinh R}.
\]
When
\[
a\ge1,
\]
convexity of \(\sinh\) gives
\[
\sinh R\ge a\sinh(R/a),
\]
so both inverse stretches are at most \(1/a\). Thus
\[
d_{\mathbb D}(D_a z,D_a w)
\ge
a\,d_{\mathbb D}(z,w)
\]
and hence
\[
\rho(D_a z,D_a w)\ge\rho(z,w).
\]
Carleson's product-separation lower bound is therefore preserved.

For
\[
0<a<1,
\]
take
\[
r_n=\tanh(R_n/2)
\]
with geometrically decreasing boundary defects and choose
\[
\sin(\theta_n/2)=c/\sinh R_n.
\]
Then the same-radius identity
\[
\sinh\!\left(\frac{d_{\mathbb D}}2\right)
=
\sinh R\,\sin(\theta/2)
\]
makes every source pair have the same positive separation. The inspected two-point packet lemma then proves the union is interpolating.

After dilation,
\[
\sinh\!\left(
\frac{d_{\mathbb D}(D_a z_n,D_a w_n)}2
\right)
=
c\frac{\sinh(aR_n)}{\sinh R_n}
\longrightarrow0.
\]
Thus the image fails pairwise separation.

Finally,
\[
D_a^{-1}=D_{1/a}
\]
and
\[
D_a\circ D_b=D_{ab},
\]
which give the bidirectional statement and the semigroup formulation.

No numerical approximation or finite experiment is used.
