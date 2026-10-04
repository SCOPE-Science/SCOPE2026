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
The central comparison is analytic.

For positive constants \(A\), \(B\), \(\Pi\), and \(\varphi\), define
\[
y_+
=
\frac{y_0+A\Pi}
{1+A\varphi}
\]
and
\[
\lambda
=
\frac{B\varphi}
{1+A\varphi}.
\]
The candidate positive-time CF integral solution is
\[
y(t)
=
\frac{\Pi}{\varphi}
+
\left(
y_+-\frac{\Pi}{\varphi}
\right)e^{-\lambda t}.
\]

The bundled checker verifies directly that this satisfies
\[
y(t)-y_0
=
A(\Pi-\varphi y(t))
+
B\int_0^t(\Pi-\varphi y(s))\,ds.
\]
It also verifies
\[
y_+=y_0
\]
if and only if
\[
y_0=\frac{\Pi}{\varphi}
\]
when \(A>0\).

As an illustration only, the checker compares this exponential transient with the order-\(1/2\) classical Caputo solution
\[
\frac{\Pi}{\varphi}
+
\left(
y_0-\frac{\Pi}{\varphi}
\right)
e^{\varphi^2t}\operatorname{erfc}(\varphi\sqrt t).
\]
The two values differ away from the equilibrium case.

The numerical illustration is not used to prove the source-specific operator mismatch; that follows from the printed integral equations and the cited method's operator definition.
