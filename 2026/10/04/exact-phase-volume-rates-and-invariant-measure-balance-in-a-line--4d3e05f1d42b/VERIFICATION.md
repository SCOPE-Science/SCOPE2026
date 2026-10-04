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

The packaged symbolic checker verifies the exact divergence \(\nabla\!\cdot F=z\), the equilibrium line \(E_s=(0,0,s)\), the characteristic polynomial \(\lambda(\lambda^2-s\lambda+a)\), and the Lie-derivative identities
\[
\dot z=x^2-b y^2,
\qquad
\frac d{dt}(a x^2+y^2)=2y^2z.
\]
It also checks symbolically that the equilibrium tangent-map volume factor is \(e^{st}\).

These are algebraic and local-flow checks. They do not validate the numerical Lyapunov exponents, chaotic sea, bifurcation diagrams, or basin plots reported in the source article.
