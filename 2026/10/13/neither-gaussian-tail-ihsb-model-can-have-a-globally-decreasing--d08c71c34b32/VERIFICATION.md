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
For both models the hazard is evaluated directly as
\[
h_\alpha(x)
=
\frac{x^{\alpha-1}R_0(x)}
{\int_x^\infty t^{\alpha-1}R_0(t)\,dt}.
\]

The analytic proof gives
\[
h_\alpha(x)\sim x/\beta^2
\]
at the right endpoint and
\[
h_\alpha(x)\sim
\alpha x^{\alpha-1}/\operatorname{E}(X_0^\alpha)
\]
at the left endpoint.

The bundled checker numerically evaluates the source integral formulas for both the half-normal and Maxwell baselines, verifies the large-\(x\) normalized hazard ratio, and reproduces representative interior minima for \(\alpha=0.1\) and \(\beta=1\).

Finite numerical calculations are not used as proof of the endpoint statement.
