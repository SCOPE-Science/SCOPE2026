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

Let
\[
\Lambda=|h'|+|g'|,
\qquad
\lambda=|h'|-|g'|.
\]
For nonnegative Jacobian,
\[
0\le\lambda\le\Lambda,
\qquad
J=\Lambda\lambda,
\]
and
\[
|h'|^2+|g'|^2
=
\frac{\Lambda^2+\lambda^2}{2}.
\]

When \(\Lambda>0\), put
\[
x=\lambda/\Lambda,
\qquad
t=K_0/\Lambda^2.
\]
The weak quasiregular condition is exactly
\[
t\ge\max\{0,1-Kx\}.
\]
Thus universal validity of
\[
\Lambda^2
\le
A(|h'|^2+|g'|^2)+BK_0
\]
is equivalent to
\[
1\le\frac A2(1+x^2)+Bt
\]
for this scalar feasible set.

For \(x\ge1/K\), the allowed value \(t=0\) forces
\[
A\ge\frac{2K^2}{K^2+1}.
\]
For \(x<1/K\), the least admissible defect gives
\[
B\ge
\frac{1-\frac A2(1+x^2)}{1-Kx}.
\]
The derivative numerator is
\[
AKx^2-2Ax+K(2-A).
\]
For
\[
\frac{2K^2}{K^2+1}\le A\le2,
\]
the maximizing root is
\[
x_A
=
\frac{A-\sqrt{A((K^2+1)A-2K^2)}}{KA},
\]
and the critical-point equation yields
\[
\max B
=
\frac{Ax_A}{K}
=
\frac{A-\sqrt{A((K^2+1)A-2K^2)}}{K^2}.
\]

The sharpness construction uses constant derivatives
\[
h'=\frac{L(1+x_A)}2,
\qquad
g'=\frac{L(1-x_A)}2,
\]
with
\[
K_0=L^2(1-Kx_A).
\]
It saturates both the defining distortion inequality and the frontier estimate. Hence the sharpness is exact and finite-dimensional, not experimental.
