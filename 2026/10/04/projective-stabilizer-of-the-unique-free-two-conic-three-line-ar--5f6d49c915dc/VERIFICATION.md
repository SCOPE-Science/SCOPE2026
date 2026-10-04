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
The included `artifacts/verify.py` uses exact rational arithmetic to verify the matrices \(R\) and \(S\), the relations \(R^3=S^2=1\) and \(SRS=R^{-1}\), preservation of both conics, and permutation of the three line components. It checks the three inner-conic tangency points, the three outer-conic triple points with distinct tangent directions, the two conic intersections at infinity via the relation \(Y^2=-3x^2\), and the equality of the total pairwise Bézout count with the contributions of five tacnodes and three ordinary triple points.

The verifier is a finite exact check of the displayed coordinates. The global upper bound on the automorphism group is a proof step rather than an exhaustive matrix search: every automorphism fixes the inner conic and therefore acts faithfully on its three intrinsic tangency points. No claim is made about automorphisms of the complement that do not extend projectively.
