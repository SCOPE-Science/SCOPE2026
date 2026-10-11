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

For the counterexample, take
\[
H=\mathbb R,\qquad
W_1=H,\qquad
v_1=1,\qquad
\Lambda_1=2I,\qquad
\Theta_1=\sqrt5\,I.
\]
Then
\[
S_\Lambda=4I,\qquad
S_\Theta=5I.
\]
Thus
\[
A=B=4
\]
are exact original bounds, and
\[
\|(S_\Lambda-S_\Theta)f\|=\|f\|
\]
shows that the perturbation hypothesis holds with
\[
R=1<4.
\]

The source's upper formula evaluates to
\[
\min\left\{
4+1\sqrt{\frac44},
1+\sqrt4
\right\}
=
\min\{5,3\}
=
3.
\]
But
\[
\langle S_\Theta f,f\rangle=5\|f\|^2,
\]
so \(3\) cannot be an upper frame bound.

For the corrected theorem, the source hypothesis implies
\[
\|(S_\Theta-S_\Lambda)f\|\le R\|f\|
\]
for every \(f\), hence
\[
\|S_\Theta-S_\Lambda\|\le R.
\]
Since the difference is self-adjoint,
\[
-RI\le S_\Theta-S_\Lambda\le RI.
\]
Therefore
\[
(A-R)I\le S_\Theta\le(B+R)I.
\]

Sharpness is exact in one dimension. With
\[
S_\Lambda=cI,
\]
the choices
\[
S_\Theta=(c-R)I
\quad\text{and}\quad
S_\Theta=(c+R)I
\]
satisfy the perturbation hypothesis with equality and attain the corrected lower and upper constants.

The preprint Corollary 6 and final journal Corollary 2 were both inspected directly, including rendered PDF pages. The related earlier \(g\)-frame perturbation proposition was also inspected. No numerical approximation is used.
