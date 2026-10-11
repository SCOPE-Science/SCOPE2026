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
The arbitrary-\(n\) derivation is in `RESULT.md`.

Critical checks:
- the signed-filter definition on a chain reduces to suffix vectors \(u_k\) and \(v_k\);
- \(u_k=(u_{k-1}+v_{k-1})/2\) and \(0=(u_n+v_n)/2\), leaving exactly \(n+1\) simplex vertices;
- the displayed \(a_k\) and \(b\) are the complete facet normals with support constant \(1\);
- \(\|a_k\|=N_{n-k}\) and \(\|b\|=N_{n-1}\);
- \(b+\sum_k2^{k-1}a_k=0\);
- the incenter equations give the displayed \(r_n\) and coordinate formula;
- the perpendicular-bisector recurrence gives \(q_j=1/2-2^{-j}\);
- all vertices have squared distance \(n/4+4/3-2^{-n}-4^{-n}/3\) from \(q\);
- \(q\) satisfies \(0\le q_1\le\cdots\le q_n\le1\), placing it in the ordinary order polytope and therefore in the enriched order polytope;
- center-in-contact-convex-hull gives minimum-enclosing optimality and uniqueness.

`verify.py` performs exact symbolic checks for \(1\le n\le12\), including every vertex-facet incidence, the normal dependence, both inradius expressions, every incenter tangency equation, every circumsphere equation, and the center-membership inequalities. Finite computation is corroborative only and does not assess originality.
