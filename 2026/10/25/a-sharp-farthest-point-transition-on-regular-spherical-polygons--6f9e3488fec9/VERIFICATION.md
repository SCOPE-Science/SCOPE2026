---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS. For all n≥3 and 0<rho<pi/2, hemisphere containment excludes -v0 as an interior minimum of v0·x, reducing global farthest-point optimization to polygon edges. Even n: polar-angle bound v0·x≥cos(2rho) has equality only at opposite vertex. Odd n: every edge interpolation z has v0·z=t≥m and c≤||z||≤1, with equal t=m only on opposite edge. The sign of m forces respectively opposite two vertices (m>0), entire opposite edge (m=0), or sole geodesic midpoint (m<0); m=0 iff tan²rho=1/cos(pi/n). Endpoint cases 0<rho<pi/2 and n=3 valid. Independent boundary sampling at 50 n/rho pairs gave maximum prediction discrepancy 2.22e-16, used only as sanity check.

## originality

PASS

PASS best knowledge. Available Zachos source minimizes weighted sums of distances on spherical triangle, not a maximum of one fixed vertex over all spherical regular n-gons. Published Resultary farthest-distance profile is Euclidean and does not imply the geodesic opposite-edge threshold. Exact all-n equality locus has no identified dominant prior formula. Risk: unindexed spherical farthest-point/diameter formula or specialized thesis.

## value

PASS

PASS. The fixed-source farthest-point set on a natural spherical regular polygon undergoes a sharp geometry-driven dimension jump: two vertices, then entire geodesic edge, then a unique edge midpoint, contrasted with even-n rigidity. The exact radius and equality loci are structural geodesic-optimization data and not a renamed Euclidean result. Limitation: regular northern-hemisphere polygons only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
