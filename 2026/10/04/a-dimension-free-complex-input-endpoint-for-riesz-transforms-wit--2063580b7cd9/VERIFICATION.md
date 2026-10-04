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

The source theorem was checked in its full primary text and states
\[
\|R_v f\|_{L^{1,\infty}(\mu_v;\mathbb R^n)}
\le2\|f\|_{L^1(\mu_v)}
\]
for real-valued \(f\), uniformly in \(n\) and \(v\).

For the geometric transfer, let
\[
z=a+ib\in\mathbb C^n
\]
with \(|z|=1\). The Gram matrix of \(a\) and \(b\) has eigenvalues
\[
\lambda,\ 1-\lambda,
\qquad
1/2\le\lambda\le1.
\]
After an angular shift,
\[
|\operatorname{Re}(e^{-i\theta}z)|^2
=
\lambda\cos^2\theta+(1-\lambda)\sin^2\theta.
\]
For
\[
0<c\le2^{-1/2},
\]
the bad-angle threshold satisfies
\[
t_\lambda^2
=
\frac{c^2-(1-\lambda)}{2\lambda-1}
\le c^2,
\]
because
\[
(1-\lambda)(1-2c^2)\ge0.
\]
Therefore at least
\[
4\arccos c
\]
radians of phase satisfy
\[
|\operatorname{Re}(e^{-i\theta}z)|>c|z|.
\]

Applying the real endpoint to
\[
f_\theta=\operatorname{Re}(e^{-i\theta}f)
\]
and using
\[
\int_0^{2\pi}
|\operatorname{Re}(e^{-i\theta}w)|\,d\theta
=
4|w|
\]
gives
\[
\|R_v^{\mathbb C}f\|_{1,\infty}
\le
\frac{2}{c\arccos c}\|f\|_1.
\]

With
\[
c=\cos\theta,
\]
the denominator is maximized when
\[
\theta\tan\theta=1.
\]
The unique solution in
\[
(\pi/4,\pi/2)
\]
is
\[
\theta_*=0.860333589019379\ldots,
\]
hence
\[
c_*=0.652184623909186\ldots
\]
and
\[
C_{\mathbb C}=3.564450280406266\ldots .
\]

No numerical experiment is used as proof; the decimals only evaluate the exact optimizer equation.
