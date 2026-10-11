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

Take \(H=\mathbb C^2\) with the standard \(2\)-inner product and anchor \(e_2\). On the induced quotient,
\[
\|x,e_2\|=|x_1|.
\]
Set \(K=I\), \(t\in(0,1)\), and
\[
r=\frac{1-t}{1+t}.
\]
Use \(f_{p1}=e_1\), \(f_{q1}=r e_1\), with all later entries zero.

If \(1\in I\), the perturbation condition reduces to
\[
1-r\le t+t r,
\]
and equality holds because
\[
1-r=t(1+r)=\frac{2t}{1+t}.
\]
If \(1\notin I\), both sides vanish.

The printed lower bound is \(1\), while the q-only weave has exact lower bound
\[
r^2<1.
\]
The source proof gives
\[
(1+\mu)E_q(I)^{1/2}\ge(1-\lambda)E_p(I)^{1/2},
\]
so the corrected factor is
\[
\left(\frac{1-\lambda}{1+\mu}\right)^2.
\]
On the witness family it equals \(r^2\), proving sharpness.

The publisher PDF was inspected at the theorem statement and proof and by page image. No numerical approximation is used.
