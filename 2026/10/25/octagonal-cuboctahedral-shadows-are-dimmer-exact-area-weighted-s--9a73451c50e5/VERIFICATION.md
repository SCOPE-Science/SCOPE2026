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

Verified the 12 vertices, six square faces and eight triangles, the dichotomy N=8 iff largest absolute directional coordinate exceeds the other two, and the Cauchy face-area formula A=4a+2b+2c (octagon) or 3(a+b+c) (hexagon). The 24 spherical cones have area arcsin(1/3); the sphere Laplacian/divergence identity gives chamber first moments Ix=pi/(6sqrt3), Iy=Iz=pi/8−pi/(6sqrt3), hence the weighted octagonal integral pi/2. Thus E[A;N8]=3 and E[A;N6]=sqrt3 by total surface area (12+4sqrt3)/4. Exact inequalities imply Cov(A,N)<0. Independently rebuilt projected planar convex hulls of 480 generic views with max area error 2.7e−15; separate angular quadrature reproduces cone area and first moments. These finite checks corroborate, but only the analytic proof covers all Haar directions.

## originality

PASS

The known unconditional mean-projection theorem and Platonic-solid shadow moments do not determine type-conditioned first moments for this Archimedean solid. The cuboctahedral 24-cone weighted split (3,sqrt3) and negative covariance are the distinct claim; novelty remains best-of-knowledge.

## value

PASS

The cuboctahedron is a canonical Archimedean solid; projected area and silhouette complexity are independently natural observable statistics. An exact negative association, reversing the naive complexity/area heuristic, and clean weighted decompositions (3,sqrt3) are precise benchmark facts for random visual geometry, not routine restatements of the total Cauchy mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
