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

For one index with
\[
W_1=H=\mathbb C,\qquad
\omega_1=2,\qquad
K=I,
\]
the fusion synthesis operator is
\[
T_Wx=2x.
\]
Thus the reduced solution of
\[
T_WX=I
\]
is
\[
X_w=\frac12I.
\]

Take
\[
\theta_1=\frac14I.
\]
The source's resolution identity is satisfied exactly:
\[
\omega_1^2\theta_1
=
4\cdot\frac14I
=
I.
\]
Its square-summability condition is also satisfied:
\[
\omega_1^2\|\theta_1f\|^2
=
4\cdot\frac1{16}\|f\|^2
=
\frac14\|f\|^2.
\]

The published minimum-norm inequality would require
\[
\|X_wf\|^2
=
\frac14\|f\|^2
\le
\frac1{16}\|f\|^2
=
\|\theta_1f\|^2,
\]
which is false for every nonzero \(f\).

For the repair, define
\[
\widehat\theta f=\{\omega_i\theta_i f\}_i.
\]
Then
\[
T_W\widehat\theta f=Kf.
\]
The Douglas reduced solution lies in
\[
N(T_W)^\perp,
\]
so it is the minimum-norm solution pointwise:
\[
\|X_wf\|^2
\le
\sum_i\omega_i^2\|\theta_i f\|^2.
\]
Because
\[
T_W^*f=\{\omega_i\pi_{W_i}f\}_i
\]
also lies in \(N(T_W)^\perp\), Pythagoras yields
\[
\sum_i\|(X_wf)_i-\omega_i\pi_{W_i}f\|^2
\le
\sum_i\omega_i^2\|\theta_i f-\pi_{W_i}f\|^2.
\]

The complete public preprint statement and proof of Theorem 4.3 and Corollary 4.4 were inspected. The earliest verified public version is arXiv:1705.00209v1 dated 29 April 2017.
