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

The displayed formulas for \(C_+\) and \(C_-\) were checked against Theorem 3.4 of arXiv:2609.14148. The proof was replayed from those formulas on the complete parameter domain \(a,b>1\), \(c>0\), \(R>2\).

For fixed \(R\), monotonicity forces \(b=R-1\) and \(c=(R-1)/(1+a)\). The reduced objective was differentiated on both sides of its unique crossing. At \(R=3\) the branches meet at \((a,b,c)=(2,2,2/3)\). Representative substitutions at \(R=2.1,2.5,3,4,3+\sqrt3,10\) reproduce the closed formulas, but these checks are not used to establish the universal statement.

The product profile was differentiated symbolically. Its only admissible critical point comes from \(d^3-6d-4=(d+2)(d-(1+\sqrt3))(d-(1-\sqrt3))\), with \(d=R-2\), giving \(R=3+\sqrt3\) and product \(9+6\sqrt3\).

The scientific limit is essential: the theorem concerns the explicit proof guarantees, not exact norms of the constructed isomorphisms and not a universal lower frontier over all possible constructions.
