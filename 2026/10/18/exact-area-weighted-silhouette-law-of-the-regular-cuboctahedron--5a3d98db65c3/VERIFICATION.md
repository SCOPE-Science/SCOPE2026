---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Direct facet-normal signs for square and triangular faces show six silhouette edges when a<b+c and eight when a>b+c. Cauchy projected-area formula gives 3(a+b+c) and 4a+2b+2c in those respective chambers. Spherical triangle Girard area yields p=12 atan(3-2sqrt2)/pi. Independent high-precision evaluation yielded p=0.649040687816, conditional areas 4.62220636751<4.93518977112, covariance -0.142587021853. The analytical surface-divergence boundary flux integral of B over one spherical triangle is pi/2, yielding exact weighted mass 3 and complementary sqrt3; the finite Monte Carlo checker cannot replace that proof.

## originality

PASS

McGuire computes expected silhouette size via dihedral-angle sums; this may already imply p for the 6/8 dichotomy, so p alone is not original. Cauchy area mean 3+sqrt3 is classical. Neither marginal alone yields the exact partition of area by silhouette size, the conditional means, or covariance.

## value

PASS

The exact joint area/edge-count relationship is a natural complete first-moment invariant of the canonical Archimedean cuboctahedron, distinguishing combinatorial complexity from projected area.

The dated certificate retains the supplied scientific assessment, sources and limitations.
