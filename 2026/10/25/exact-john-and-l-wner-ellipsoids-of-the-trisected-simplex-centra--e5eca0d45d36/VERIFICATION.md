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

For each m>=3 in H_m={x:sum x_i=1} with the inherited Euclidean metric, the half-spaces x_i<=2x_j have centered normals Π(e_i-2e_j) of squared norm 5-1/m, all genuine facets, so the centered John radius squared is 1/[m(5m-1)]. Kazakov’s listed vertices v_L have k low coordinates 1/(2m-k) and remaining 2/(2m-k); direct exact squared distance is k(m-k)/[m(2m-k)^2]. The derivative m(2m-3x)/(2m-x)^3 plus exact adjacent-cardinality comparisons proves the unique maximizing k: 2q when m=3q, otherwise 2q+1. S_m irreducibility on the sum-zero hyperplane makes the unique John/Löwner ellipsoids centered balls. Explicit zero-first-moment isotropic frame identities for ALL facet normals and the unique contact vertex orbit certify global ellipsoid optimality, not merely maximal centered balls. Independently recomputed exact ratios for m=3..25 and full rational facet Gram frames for m=3..8; finite checks corroborate the symbolic all-m proof.

## originality

PASS

The same polytope and the exhaustive two-level vertex description are published by Kazakov (arXiv:2606.02087v1); his Appendix B already calculates a three-dimensional facet distance, and that part is NOT new. His inspected construction/vertex/appendix does not contain the general John and Löwner ellipsoids, unique three-residue maximizing vertex shells, or both isotropic contact certificates. Classical ellipsoid characterization does not evaluate this particular family; other symmetric-polytope ellipsoids have inequivalent defining inequalities. Best-of-knowledge O PASS, with the explicit risk of implicit or unindexed equivalent treatment.

## value

PASS

This is a complete all-dimensional exact natural metric-invariant classification for an independently motivated central simplex polytope, giving both extremal ellipsoids, all contact sets, and exact certificates. It is useful for sharp containment/shape comparison and does not simply repeat Kazakov’s vertex count or volume.

The dated certificate retains the supplied scientific assessment, sources and limitations.
