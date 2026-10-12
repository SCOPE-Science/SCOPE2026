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
The universal result is analytic. The standalone checker replays exact algebra for a rational two-mode example.

For
\[
a=0,
\qquad
d=\frac35,
\]
the Gramian coefficients are
\[
p=1,
\qquad
q=\frac{25}{16},
\qquad
r=1.
\]
The predicted optimal squared actuator components are
\[
\cos^2\theta_*=\frac{25}{41},
\qquad
\sin^2\theta_*=\frac{16}{41}.
\]
Choosing the positive representative
\[
v_*=\frac1{\sqrt{41}}(5,4)^{\mathsf T}
\]
gives
\[
W_*=
\frac1{41}
\begin{pmatrix}
25&20\\
20&25
\end{pmatrix}.
\]
The checker verifies exactly that
\[
W_*
\begin{pmatrix}
1\\1
\end{pmatrix}
=
\frac{45}{41}
\begin{pmatrix}
1\\1
\end{pmatrix},
\qquad
W_*
\begin{pmatrix}
1\\-1
\end{pmatrix}
=
\frac5{41}
\begin{pmatrix}
1\\-1
\end{pmatrix},
\]
so the condition number is exactly \(9\).

It also checks that determinant maximization would use squared weights \(1/2,1/2\), which are different from the condition-number optimum in this example.

Finite replay is corroborative only. The all-parameter minimization, uniqueness in squared weights, and hyperbolic formula are proved symbolically in `RESULT.md`.
