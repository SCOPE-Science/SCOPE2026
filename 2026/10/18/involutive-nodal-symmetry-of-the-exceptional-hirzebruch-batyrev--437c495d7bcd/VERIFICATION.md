---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

An independent exact integer enumeration on all 22 listed 4D lattice vertices restricts a GL(4,Z) stabilizer by known vertex differences to 52 candidate (Ae1,Ae2) pairs and 12 (Ae3,Ae4) pairs, 624 cases total; determinant and complete vertex-set checks yield only I and displayed involution T. Independently enumerating primitive supporting hyperplanes from 4-vertex combinations yields 26 primal and 22 polar facets, with 72/68 distinct two-faces, size histograms (50 triangles,21 quadrilaterals,1 hexagon)/(38 triangles,26 quadrilaterals,2 pentagons,2 hexagons), and 20/26 parallelogram unit-square faces. For the 26 polar square-diagonal columns, exact rational elimination gives rank 18 and exactly two coloops, exchanged under T transpose. The signed action has domain ± eigendimensions 14 and 12, image ± ranks 9 and 9, and therefore kernel ± dimensions 5 and 3. All exhaustive calculations were run as a separate independent implementation; symmetry is of lattice polytope/fan, not a generic anticanonical hypersurface.

## originality

PASS

Best-of-knowledge original component is complete integral lattice stabilizer C2 and its explicit face orbit/equivariant node-dependency character for Wuebben’s unique exceptional mirror pair. Wuebben 2026 Theorem 6.1 already publishes the 22/26 vertices, two-face inventories, nodes, Hodge numbers and nonsmoothability; Remark 6.3 already gives 26×26 node matrix rank 18 and two coloop faces. None of those individually supplies the complete lattice automorphism group nor +5/−3 character. General lattice polytope algorithms do not state this particular certified profile, though an unindexed database implicit computation is a residual priority risk.

## value

PASS

The exceptional mirror pair is singled out by a singularity/smoothability dichotomy, making its exact lattice symmetry and action on node relations natural finite invariants. The 5+3 kernel character and exchanged coloops refine known eight-dimensional dependency data and can constrain equivariant deformation questions, even though they do not themselves prove a smoothing theorem. Exhaustive computation of a motivated fixed finite object can be scientifically meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
