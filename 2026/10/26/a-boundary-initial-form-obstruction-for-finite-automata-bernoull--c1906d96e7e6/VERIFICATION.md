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

The algebraic proof was checked line by line against the displayed definitions. For the family, both summands of \(Q_d\) are bounded above by \(1\) on the closed simplex, and \(Q_d-P_d=p_3^{d-2}(p_1-p_2)^2+p_1^{d-1}(p_1+p_3)\) on the open simplex. This yields \(0<f_d<1\) and \(\min(f_d,1-f_d)\ge\frac12(p_1p_2p_3)^d\). The numerator factors only as \(p_1^{d-1}p_2\), and neither factor divides the denominator. After setting \(p_3=1\), the lowest nonzero homogeneous denominator term is \((x-y)^2\) exactly when \(d\ge4\). The nonnegative-coefficient contradiction is then exact.

The proof depends on the cited multivariate criterion for existence of a general Bernoulli factory and the cited Bernstein-ratio characterization for finite-automata factories. The former was checked via the accessible 2026 note because the original thesis PDF timed out. No computational experiment is presented as proof. The condition is sufficient only; no necessity claim or complete classification is made. Independent audit and independent validation have not been performed.
