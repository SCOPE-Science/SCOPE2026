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
r=\frac{s}{2},
\qquad
u_s=\psi_s^2.
\]
For
\[
E_{\varepsilon,b}
=
(-r,r-\varepsilon)
\cup
(r-\varepsilon+b,r+b),
\]
the discrepancy at center zero is
\[
D_0(E_{\varepsilon,b})
=
\int_{r-\varepsilon}^{r}
\int_0^b
-u_s'(x+t)\,dt\,dx.
\]

If
\[
b\to0,
\qquad
\varepsilon\le b,
\]
then every point
\[
x+t
\]
in this rectangle tends uniformly to \(r\), so
\[
D_0(E_{\varepsilon,b})
=
-u_s'(r)\varepsilon b(1+o(1)).
\]

For the translated mass
\[
\Phi_{\varepsilon,b}(a)
=
\int_{E_{\varepsilon,b}}u_s(x-a)\,dx,
\]
the interval limit has unique maximum at zero and
\[
\Phi_{0,0}''(0)
=
2u_s'(r)
<
0.
\]
Moreover,
\[
\Phi_{\varepsilon,b}'(0)
=
\int_{r-\varepsilon}^{r}
\bigl(u_s'(x)-u_s'(x+b)\bigr)\,dx
=
O(\varepsilon b).
\]
Uniform boundedness of \(u_s''\) and strict local curvature give
\[
a_{\varepsilon,b}=O(\varepsilon b)
\]
for the optimal center, and therefore
\[
\Phi_{\varepsilon,b}(a_{\varepsilon,b})
-
\Phi_{\varepsilon,b}(0)
=
O(\varepsilon^2b^2).
\]
Thus
\[
\mathcal D(E_{\varepsilon,b})
=
-u_s'(r)\varepsilon b(1+o(1)).
\]

The inspected stability theorem proves
\[
0
\le
\mathcal D(E)-\eta(E)
\le
A_s\mathcal D(E)^2.
\]
Since
\[
\varepsilon b\to0,
\]
this error is lower order, yielding
\[
\eta(E_{\varepsilon,b})
\sim
-u_s'(r)\varepsilon b.
\]

The proof uses no numerical experiment or finite-degree extrapolation.
