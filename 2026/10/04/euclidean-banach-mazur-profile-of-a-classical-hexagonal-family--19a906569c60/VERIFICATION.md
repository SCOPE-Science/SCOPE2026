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
# Verification

The distance computation was replayed symbolically from the unit ball.

1. The unit ball is the intersection of the three symmetric strips with normals \(f_0=(0,1)\), \(f_+=(1,1-\gamma)\), and \(f_-=(1,-(1-\gamma))\), and its vertices are exactly \(\pm(1,0)\), \(\pm(\gamma,1)\), and \(\pm(\gamma,-1)\).
2. For \(E_P=\{u:u^{\mathsf T}Pu\le1\}\), inner containment is exactly \(f^{\mathsf T}P^{-1}f\le1\), equivalently \(P\succeq ff^{\mathsf T}\). Outer containment at squared dilation \(R\) is exactly \(v^{\mathsf T}Pv\le R\) at all vertices.
3. Averaging all coordinate-reflection conjugates of a feasible \(P\) preserves every constraint and produces a diagonal feasible matrix at the same \(R\). Thus the reduction to \(P=\operatorname{diag}(p,q)\) is exact.
4. The diagonal constraints give \(q\ge1\) and \(p\ge q/(q-(1-\gamma)^2)\). At an optimum equality holds. The two outer bounds are \(p(q)\) and \(F(q)=\gamma^2p(q)+q\).
5. The function \(p(q)\) decreases, while \(F(q)\) increases for \(q\ge1\). They cross at \(q=2(1-\gamma)\). This point is feasible exactly when \(\gamma\le1/2\), yielding squared distance \(2/(1+\gamma)\); otherwise the optimum is \(q=1\), yielding squared distance \(2/(2-\gamma)\).
6. Both branches equal \(4/3\) at \(\gamma=1/2\), and monotonicity on either side gives the unique minimum \(2/\sqrt3\).

No finite experiment, numerical optimization, or unproved contact-pattern assumption is used. The only unresolved issue is a literature-access residual, not a proof dependency.
