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

The derivation was checked against arXiv:2609.25747v1, Proposition 3 and equations (50)--(52). With \(R=\sqrt{u_M/u_m}\) and \(a=-y_{\infty}^{\mathrm{cycle}}/b\), the printed fixed-point equation reduces exactly to the equation used here, and the printed maximum-height formula reduces exactly to \(Z=Ra-\log(1+Ra)\).

For correctness, the partial derivatives of the implicit equation were factored exactly. Their signs on the source-proved interval \(a\in(1-R^{-1},1)\) yield \(a'(R)>0\), and monotonicity of \(x-\log(1+x)\) yields \(Z'(R)>0\). The weak-contrast coefficients were independently expanded through one order beyond the leading terms. For the strong-contrast limit, the transformed equation for \(\epsilon=1-a\) was used before expansion, preventing a circular assumption about exponential smallness.

Consistency checks of the exact scalar root gave \(a(1.01)\approx0.0148513381\), \(a(1.1)\approx0.136239927\), \(a(2)\approx0.716375267\), \(a(5)\approx0.983833343\), and \(a(10)\approx0.999815940\). These numerical values are not used to establish any infinite or asymptotic statement.

The result is restricted to the singular toy-model cycle and inherits the source's finite-\(\varepsilon\) limitation. No claim is made about uniform finite-\(\varepsilon\) constants or uniqueness of multi-stage optimal strategies.
