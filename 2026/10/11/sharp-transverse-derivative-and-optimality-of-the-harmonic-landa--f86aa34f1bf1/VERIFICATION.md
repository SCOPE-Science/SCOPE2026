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

For a bounded real harmonic function with
\[
u(0)=0,
\qquad
\nabla u(0)=0,
\]
the constant and first Fourier modes vanish.

The transverse derivative kernel at
\[
(r,0)
\]
is
\[
K_r(t)
=
\sum_{n\ge1}
n r^{n-1}\sin(nt)
=
\frac{(1-r^2)\sin t}{(1-2r\cos t+r^2)^2}.
\]
After odd symmetrization, the first-sine coefficient constraint is
\[
\int_0^\pi
\psi(t)\sin t\,dt=0.
\]
Subtracting the level at
\[
\cos t=0
\]
and using
\[
|\psi|\le1
\]
gives the exact extremal integral
\[
\frac{8r}{\pi(1-r^4)}.
\]

The boundary trace
\[
-\operatorname{sgn}(\sin2t)
\]
attains the extremal sign pattern. Its Poisson integral is the source function
\[
u_*(z)
=
\frac2\pi
\operatorname{Arg}
\left(
\frac{1-z^2}{1+z^2}
\right),
\]
for which
\[
(u_*)_y(r,0)
=
-\frac{8r}{\pi(1-r^4)}.
\]

For
\[
F_{M,u}(x+iy)
=
x+i(y+(M-1)u(x,y)),
\]
\[
J_{F_{M,u}}
=
1+(M-1)u_y.
\]
Therefore every positive-real-axis fold satisfies
\[
r\ge r_M,
\]
where
\[
8(M-1)r_M
=
\pi(1-r_M^4),
\]
and equality is attained by \(u_*\).

The threshold equation obtained from
\[
r_M=r_0(M)
\]
factors as
\[
(\rho-1)
\left(
\pi\rho^3+\pi\rho^2+(\pi+4)\rho+\pi-4
\right)
=
0.
\]
The cubic factor is strictly increasing on \((0,1)\), so its root there is unique.

The packaged checker replays the kernel identity, exact extremal integral, source derivative, threshold factorization, and numerical evaluation of the uniquely characterized root.
