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
The bundled checker evaluates the direct stress–strength integral
\[
R
=
\beta_1 e^2
\int_1^\infty t^{\beta_1-1}
 e^{-t^{\beta_1}-t^{\beta_2}}\,dt
\]
at high precision.

On representative pairs with \(\beta_2<\beta_1\), it verifies agreement with the source's upper-incomplete-gamma series.

At \(\beta_1=\beta_2=1\), it verifies the direct value \(R=1/2\) and shows that the source-series term magnitudes approach \(e^2\) rather than zero.

For \((\beta_1,\beta_2)=(0.5,1.5)\), it verifies that the printed-series terms rapidly increase in magnitude, while the complementary swapped series agrees with the direct integral.

These numerical checks supplement the analytic convergence proof.
