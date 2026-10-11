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
u=P[f],
\qquad
F=u+iv,
\qquad
\omega=\Phi^{-1}\circ F,
\qquad
\Phi(z)=\frac4\pi\arctan z.
\]
The inspected primary proof gives
\[
u=U\circ\omega,
\qquad
U=\operatorname{Re}\Phi,
\]
with
\[
\omega(0)=0
\]
and
\[
|\omega(z)|\le|z|.
\]

Define
\[
g(z)=
\begin{cases}
\omega(z)/z,&z\ne0,\\
\omega'(0),&z=0,
\end{cases}
\]
and
\[
q=q_r(f)=\max_{|z|\le r}|g(z)|.
\]
Then
\[
0\le q\le1.
\]

When
\[
q>0,
\]
the map
\[
\psi(z)=\frac{\omega(rz)}{qr}
\]
satisfies
\[
|\psi(z)|\le|z|
\]
and fixes zero. Hence Littlewood subordination applied to
\[
|U(qrz)|^p
\]
gives
\[
\|P_r f\|_p^p
\le
M_p(qr).
\]

For
\[
p>1,
\]
\[
\Delta|U|^p
=
p(p-1)|U|^{p-2}|\nabla U|^2
\]
is strictly positive on a nonempty open subset of every annulus because
\[
\Phi'(z)=\frac{4}{\pi(1+z^2)}
\]
does not vanish in the disk. Therefore the circular mean
\[
M_p(\rho)
\]
is strictly increasing.

If
\[
q<1,
\]
this yields a strict loss from the sharp value
\[
M_p(r)^{1/p}.
\]
If
\[
q=1,
\]
the analytic function \(g\), bounded by one, attains modulus one at an interior point and is a unimodular constant. Thus
\[
\omega(z)=e^{i\theta_0}z,
\]
and the radial boundary trace is exactly
\[
\operatorname{sgn}\cos(\theta+\theta_0).
\]

No numerical computation or finite sampling is used.
