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
I(\mu,\rho)
=
\int_0^{(1+\rho)\pi}
t^{\mu-1}\sin(t-\rho\pi)\,dt
\]
and
\[
p=1-\nu(1-\varepsilon).
\]
The inspected source proves
\[
p=O(\varepsilon^2)
\]
and gives
\[
J_0=I_\mu(1,1)
=
\gamma+\log(2\pi)-\operatorname{Ci}(2\pi)>0.
\]

Direct evaluation gives
\[
I(1,1-\varepsilon)
=
1-\cos(\pi\varepsilon)
=
\frac{\pi^2}{2}\varepsilon^2
+
O(\varepsilon^4).
\]

For the derivative,
\[
I_{\mu\rho}(1,1)
=
\pi
\int_0^{2\pi}
\log t\,\cos t\,dt.
\]
The boundary term in integration by parts vanishes at both endpoints, so
\[
I_{\mu\rho}(1,1)
=
-\pi
\int_0^{2\pi}
\frac{\sin t}{t}\,dt
=
-\pi\operatorname{Si}(2\pi).
\]
Therefore
\[
I_\mu(1,1-\varepsilon)
=
J_0+
\pi\operatorname{Si}(2\pi)\varepsilon
+
O(\varepsilon^2).
\]

Taylor expansion in the first variable gives
\[
0
=
I(1,1-\varepsilon)
-
pI_\mu(1,1-\varepsilon)
+
O(p^2).
\]
Because
\[
p^2=O(\varepsilon^4),
\]
division yields
\[
p
=
\frac{\pi^2}{2J_0}\varepsilon^2
-
\frac{\pi^3\operatorname{Si}(2\pi)}
{2J_0^2}\varepsilon^3
+
O(\varepsilon^4).
\]

High-precision root evaluations were used only as a sanity check. They give the quadratic ratio tending to
\[
2.024406839216634\ldots
\]
and the cubic residual ratio tending to
\[
-3.699971396358804\ldots.
\]
The quantified asymptotic proof is analytic and does not depend on finite sampling.
