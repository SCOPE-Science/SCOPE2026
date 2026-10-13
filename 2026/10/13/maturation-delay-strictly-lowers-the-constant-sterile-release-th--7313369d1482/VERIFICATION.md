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
The bundled checker reconstructs the source equilibrium cubic and the release graph
\[
B_a(N)
=
\frac{N(\mu_2+\xi_2N)(a-\mu_1-\xi_1N)}{a}.
\]

It verifies symbolically that
\[
\frac{\partial B_a(N)}{\partial a}
=
\frac{N(\mu_2+\xi_2N)(\mu_1+\xi_1N)}{a^2}>0.
\]

For the Figure 1 parameters it evaluates \(b_0(\tau)\) by solving the exact quadratic stationarity equation for the unique interior maximizer. It reproduces
\[
b_0(0)\approx21.9375160204,
\]
\[
b_0(0.2)\approx21.0432928772,
\]
\[
b_0(1.5)\approx16.0416587978,
\]
and
\[
b_0(4.9)\approx7.8190596714.
\]

It also reconstructs the two positive equilibria at \(\tau=0.2\) and \(b=21\), matching the source's rounded coordinates, and brackets the unique crossing
\[
b_0(\tau)=21
\]
near \(\tau=0.209893\).

The general monotonicity and endpoint asymptotic are analytic; numerical values only replay the source parameter set.
