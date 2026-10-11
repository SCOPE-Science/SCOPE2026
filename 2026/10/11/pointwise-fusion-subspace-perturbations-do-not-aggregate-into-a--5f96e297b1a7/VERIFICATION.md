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
H=\mathbb R^2,\qquad
I=\{1,2,3,4\},\qquad
C=C'=I_H,\qquad
v_i=\frac12.
\]
For
\[
W_i=H
\]
one has
\[
\sum_i v_i^2\|P_{W_i}f\|^2
=
4\cdot\frac14\|f\|^2
=
\|f\|^2.
\]
Thus \(A=B=1\).

Let
\[
Z_i=\operatorname{span}\{e_2\}.
\]
Then
\[
P_{W_i}-P_{Z_i}
=
P_{\operatorname{span}\{e_1\}},
\]
so
\[
\left\|
v_i(P_{W_i}-P_{Z_i})^{1/2}f
\right\|
=
\frac12\|P_{\operatorname{span}\{e_1\}}f\|
\le
\frac12\|f\|.
\]
Hence the theorem's hypothesis holds with
\[
\varepsilon=\frac12<\sqrt A.
\]

The perturbed energy is
\[
\sum_i v_i^2\|P_{Z_i}f\|^2
=
\|P_{\operatorname{span}\{e_2\}}f\|^2,
\]
which equals \(0\) at \(f=e_1\). Therefore the claimed lower bound
\[
A-\varepsilon^2=\frac34
\]
is impossible.

For the repair, if
\[
D_i=C^*P_{W_i}C'-C^*P_{Z_i}C'\ge0,
\]
then
\[
E_W(f)-E_Z(f)
=
\sum_i v_i^2\langle D_i f,f\rangle
=
\sum_i v_i^2\|D_i^{1/2}f\|^2.
\]
A global bound by \(\varepsilon^2\|f\|^2\) therefore gives
\[
(A-\varepsilon^2)\|f\|^2
\le
E_Z(f)
\le
B\|f\|^2.
\]

For \(N\) finite indices, the pointwise estimate sums to at most
\[
N\varepsilon^2\|f\|^2.
\]
The repeated-subspace family with weights \(1/\sqrt N\) has \(A=1\), \(\varepsilon=1/\sqrt N\), and zero perturbed lower bound, proving sharpness of the factor \(N\).

The primary theorem and proof were inspected directly in the publisher PDF and page image. The related aggregate perturbation theorem was inspected in the open controlled-\(K\)-fusion preprint. No numerical approximation or finite search is used.
