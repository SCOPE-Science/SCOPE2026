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
F_{\varepsilon,a}
=
(z_2-\varepsilon z_1^2)^2-a^2.
\]
For
\[
\Phi_t(z_1,z_2)
=
\left(
(1+t)z_1,\,
z_2+\varepsilon((1+t)^2-1)z_1^2
\right),
\]
direct substitution gives
\[
F_{\varepsilon,a}\circ\Phi_t
=
F_{\varepsilon,a}.
\]

The source graph criterion uses
\[
N_\varepsilon(\xi)
=
|\xi_1|^2+
\operatorname{Re}
\left(
2\varepsilon\xi_1^2\overline{\xi_2}
\right).
\]
On a graph component,
\[
\xi_2=\varepsilon\xi_1^2+\sigma a,
\qquad
\sigma\in\{-1,1\},
\]
and on the sphere,
\[
1
=
|\xi_1|^2+
|\varepsilon|^2|\xi_1|^4+
a^2+
2\sigma a\operatorname{Re}(\varepsilon\xi_1^2).
\]
Eliminating the cross term gives
\[
N_\varepsilon(\xi)
=
1-a^2+
|\varepsilon|^2|\xi_1|^4
>
0.
\]
Thus the source theorem applies for every
\[
\varepsilon\in\mathbb C.
\]

For the global sphere threshold, write
\[
x=|\xi_1|^2,
\qquad
|\xi_2|=\sqrt{1-x}.
\]
Minimizing over phases yields
\[
\min N_\varepsilon
=
x
\left(
1-2|\varepsilon|\sqrt{1-x}
\right).
\]
This is nonnegative for all
\[
0\le x\le1
\]
if and only if
\[
|\varepsilon|\le\frac12.
\]
For larger \(|\varepsilon|\), both signs occur.

Finally,
\[
\left.
\frac{d}{dt}
\rho(\Phi_t(\xi))
\right|_{t=0}
=
2N_\varepsilon(\xi),
\]
so opposite signs give boundary points of
\[
\Phi_t(B)
\]
strictly inside and strictly outside \(B\) for all sufficiently small positive \(t\). Hence the domains are nonnested beyond the threshold.

No finite experiment or numerical approximation is used.
