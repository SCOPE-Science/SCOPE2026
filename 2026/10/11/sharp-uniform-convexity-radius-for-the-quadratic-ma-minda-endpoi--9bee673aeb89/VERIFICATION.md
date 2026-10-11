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

For the endpoint target
\[
\phi(z)=1+z+\frac{z^2}{2},
\]
write
\[
w=s e^{i\theta},
\qquad
x=\cos\theta.
\]
The parabolic uniform-convexity defect on \(|w|=s\) is
\[
\begin{aligned}
F(s,x)=\;&s^4x^4-s^4x^2+2s^3x^3-2s^3x\\
&+3s^2x^2-2s^2+2sx+1.
\end{aligned}
\]

The exact endpoint checks are
\[
F(s,-1)=(1-s)^2,
\qquad
F(s,1)=(1+s)^2.
\]

The packaged checker computes
\[
\operatorname{Res}_x
\left(
F,
\frac{1}{2s}F_x
\right)
=
-s^{16}(s^6-4s^4+23s^2-9).
\]
The nontrivial factor has exactly one root in \((0,1)\), enclosed by
\[
0.646983632244827
<
\rho
<
0.646983632244828.
\]

The linear subresultant yields
\[
x_\rho
=
-\frac{\rho^4-11\rho^2+3}
{\rho(\rho^4-4\rho^2-3)},
\]
and exact reduction modulo
\[
y^3-4y^2+23y-9
\]
with \(y=\rho^2\) verifies
\[
-1<x_\rho<0.
\]
Substitution gives
\[
F(\rho,x_\rho)=0,
\qquad
F_x(\rho,x_\rho)=0.
\]

The extremal derivative is
\[
f_0'(z)=\exp\!\left(z+\frac{z^2}{4}\right),
\]
so
\[
1+\frac{zf_0''(z)}{f_0'(z)}
=1+z+\frac{z^2}{2}.
\]
This makes the contact certificate an actual equality case in the analytic class, not merely a target-domain computation.
