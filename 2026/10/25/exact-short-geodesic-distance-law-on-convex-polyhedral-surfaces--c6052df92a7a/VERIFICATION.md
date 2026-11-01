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

Each vertex neighborhood is an Euclidean cone with total angle alpha_v in (0,2pi); away from vertices edges unfold flatly. For pair radii t,s, the angular difference from the planar baseline is 2[min(beta,alpha/2)-beta]. Its double area integral is homogeneous r^4; exact radial/angular integration gives F(alpha)=-alpha/8[cot(alpha/2)+(pi-alpha/2)csc^2(alpha/2)]. Disjoint vertex charts and a positive small-radius cutoff localize all nonflat contributions, yielding pi r^2/A + r^4 sum_v F(alpha_v)/A^2. The tetrahedron specialization is pi r^2/sqrt(3)-pi^2 r^4/12. Independent numerical integration confirmed the exact F(alpha) at six cone angles within 7e-16, including alpha=pi.

## originality

PASS

Wenk–Cook (2009) derive shortest-path computation and geometry on polyhedral surfaces, not the distribution of distances between two independent area-uniform points. The inspected published convex-polygon result computes Euclidean distances of pairs within a planar polygon and angle-dependent quartics but has a boundary-induced cubic term; it is a different metric space and measure from a closed intrinsically flat polyhedral surface. Mathai et al. (1999) compute extrinsic Euclidean distances for a solid cube rather than this intrinsic surface cone law (abstract-level comparison only). No stronger primary statement was observed to supply the exact sum-of-cone coefficients.

## value

PASS

Exact termination of the short-radius probability at quartic order on all convex polyhedral surfaces, and dependence on the individual cone angles rather than only total curvature, gives a natural measurable geometric statistic. The formula distinguishes regular tetrahedron and cube despite equal Gauss–Bonnet total defect; this is an independently useful complete local law, not a trivial smooth-manifold expansion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
