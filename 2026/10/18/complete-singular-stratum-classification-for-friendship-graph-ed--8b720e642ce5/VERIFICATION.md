---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The facet list is exact: each block is a nonnegative multiple of the triangle with vertices (1,0),(0,1),(1,1), with admissible multiplier in [max(x_a,x_b),x_a+x_b]; the displayed inequalities give a simultaneous choice with multipliers summing to one. Facet equality vertices have affine dimension 2m-1. Active choice facets form a Boolean subcube unless a blade contains both spokes. Two free bits give a square circuit; a free empty blade gives the flip circuit with its two zero normals; no free bits with the total facet active gives the total-choice circuit. In the remaining cases the active coordinate normals extend by a unit pivot for a single total/choice ray, or by the two free-blade coordinates for the two choice rays when that blade contains its base. Each displayed circuit is inclusion-minimal with saturated span: use the two choice differences and one choice ray for the square, the two free coordinate rays and a selected coordinate outside that blade for the flip, and the complementary coordinates and one selected coordinate for total-choice. Their respective ranks yield codimensions 3,3,m+1 under face-cone duality and the independent bit choices give the counts. The saturated ray relations give the degree-zero monomial rings of weights (1,1,-1,-1) and (1,1,-1,...,-1), hence the claimed Segre cones in every characteristic, times smooth torus directions. The Segre degrees are 2 and m; the height-one ray functional exists for the first two patterns but would force m=2 for the third. The simplicial cones are smooth, and every vertex lies in a displayed singular face. Inspected the finite checker and its recorded m=2,3,4 face counts without execution; the all-parameter decision rests on the symbolic argument, not finite calculations. No conclusion about nonreduced or intersection germs.

## originality

PASS

The relevant prior base-edge charts concern the same variety over C and already give part of the local geometry. They do not cover the spoke-only total-choice orbits, or give the full global classification. The checked global polytope results supply general machinery, not the specific all-m singular basket, its transverse types, or its complete non-Q-factorial support.

## value

PASS

The graph is a natural repeated-triangle family with a growing facet set; global nonsmoothness or a fixed-point chart does not say where singularities occur. The classification gives exact incidence-defined components, shows non-equidimensionality, and separates the ordinary-node families from the deeper non-Q-Gorenstein Segre strata. That is useful local and global information for this family, in particular outside the already studied base-edge opens.

The dated certificate retains the supplied scientific assessment, sources and limitations.
