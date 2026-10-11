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

Define
\[
W(z)
=
\log\!\left(
\frac{1-z^2}{1+z^2}
\right).
\]
The source branch is analytic in
\[
\mathbb D,
\]
and
\[
u_*=(2/\pi)\operatorname{Im}W.
\]
Since
\[
W'(z)=-4z/(1-z^4),
\]
the Cauchy--Riemann equations give
\[
(u_*)_y(z)
=
-\frac8\pi
\operatorname{Re}\!\left(
\frac{z}{1-z^4}
\right).
\]

Therefore
\[
J_{F_M}(z)
=
1-
\frac{8(M-1)}{\pi}
\operatorname{Re}\!\left(
\frac{z}{1-z^4}
\right).
\]

For every
\[
|z|\le r<1,
\]
\[
\operatorname{Re}\!\left(
\frac{z}{1-z^4}
\right)
\le
\frac{r}{1-r^4}.
\]
Equality holds uniquely at
\[
z=r>0.
\]
Thus
\[
\min_{|z|\le r}J_{F_M}(z)
=
1-
\frac{8(M-1)}{\pi}
\frac{r}{1-r^4}.
\]

The defining equation
\[
8(M-1)r_M=\pi(1-r_M^4)
\]
therefore implies
\[
J_{F_M}>0
\]
throughout
\[
\mathbb D_{r_M},
\]
with the first centered-disk zero at the boundary point
\[
z=r_M.
\]

For fixed real coordinate
\[
x,
\]
the imaginary coordinate of
\[
F_M(x+iy)
\]
has derivative
\[
J_{F_M}(x,y)>0
\]
on the entire connected vertical slice of
\[
\mathbb D_{r_M}.
\]
Together with
\[
\operatorname{Re}F_M=x,
\]
this proves injectivity on
\[
\mathbb D_{r_M}.
\]

Every larger centered disk contains the Jacobian-zero point
\[
r_M.
\]
Lewy's theorem therefore prevents univalence on any such disk.

The argument is exact and analytic; numerical sampling is not used to certify positivity, injectivity, or maximality.
