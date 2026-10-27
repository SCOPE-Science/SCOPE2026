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

Claim checked: For every finite quiver \(Q=(Q_0,Q_1,s,t)\) and finite field \(k=\mathbb F_q\), let \(J\) be the arrow ideal and \(A=kQ/J^2\). Write \(m_{uv}=|\{\alpha\in Q_1:s(\alpha)=u,\ t(\alpha)=v\}|\), \(E=|Q_1|\), \(L=\sum_{v\in Q_0}m_{vv}\), and \(\Gamma_Q=\{\sigma\in\operatorname{Sym}(Q_0):m_{uv}=m_{\sigma(u)\sigma(v)}\text{ for all }u,v\}\). The map induced on \(A/J\) has image \(\Gamma_Q\), its kernel is isomorphic to \((J/(Z(A)\cap J),+)\rtimes\prod_{u,v\in Q_0}\operatorname{GL}_{m_{uv}}(k)\), and hence \(\left|\operatorname{Aut}_{k\text{-alg}}(A)\right|=q^{E-L}|\Gamma_Q|\prod_{u,v\in Q_0}|\operatorname{GL}_{m_{uv}}(\mathbb F_q)|\), with \(\operatorname{GL}_0(\mathbb F_q)\) trivial.

The symbolic argument establishes the result for arbitrary finite quivers and arbitrary finite fields under the stated split, field-linear assumptions. The attached verifier exhaustively checks all invertible linear maps over \(\mathbb F_2\) in six small cases; each computed order agrees with the formula. These finite checks are corroborative only. The independent audit and independent validation remain unperformed.
