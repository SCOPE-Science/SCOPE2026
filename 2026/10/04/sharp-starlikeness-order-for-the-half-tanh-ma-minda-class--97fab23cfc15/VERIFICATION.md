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

For
\[
z=x+iy
\]
one has
\[
\operatorname{Re}\tanh z
=
\frac{\sinh(2x)}
{\cosh(2x)+\cos(2y)}.
\]
On the right half of the unit disk, fixing \(x\) and increasing \(|y|\) decreases the denominator because
\[
0\le |y|\le1<\frac{\pi}{2}.
\]
Hence the positive maximum occurs on the unit circle.

On the first-quadrant arc,
\[
F(t)
=
\frac{\sinh(2\cos t)}
{\cosh(2\cos t)+\cos(2\sin t)},
\]
and
\[
F'(t)
=
\frac{2G(t)}
{\left(
\cosh(2\cos t)+\cos(2\sin t)
\right)^2}.
\]
The included checker verifies one sign change of \(G\) and returns
\[
1.0072145940722<t_*<1.0072145940723.
\]

The resulting numerical enclosure is
\[
0.5742700656061
<
1-\frac12F(t_*)
<
0.5742700656064.
\]

Odd symmetry gives the matching negative minimum of
\[
\operatorname{Re}\tanh z.
\]
Subordination transfers the supporting half-plane to every class member.

Finally,
\[
f_*(z)
=
z\exp\left(
\frac12\int_0^z\frac{\tanh\zeta}{\zeta}\,d\zeta
\right)
\]
satisfies
\[
\frac{zf_*'(z)}{f_*(z)}
=
1+\frac12\tanh z,
\]
so the order is sharp.

The numerical checker locates the unique critical point; the proof of the class-wide statement is analytic and does not rely on a finite coefficient truncation.
