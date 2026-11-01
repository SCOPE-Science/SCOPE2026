---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

Reconstructed the ordinary four-cut definition from complements of disconnected induced 4-subgraphs on the 15 two-subsets of [6]. Exact Alexander dual L forbids all disconnected 4-subsets, including larger faces; its face counts by size 0..7 are (1,15,105,455,750,492,70,0). A verified staged vertex-toggle matching on all 1,887 nonempty dual faces pairs 925 covers and leaves one critical 0-cell plus 36 critical 4-cells; the full 7,455-cover oriented Hasse digraph is acyclic by a topological sort of all 1,887 faces. Forman gives L≃ wedge^36 S4. Integral combinatorial Alexander duality for 15 vertices gives reduced H8(K,Z)=Z^36 and all other reduced integral homology zero. Independently enumerated K has 615 10-facets and the complete seven-skeleton, hence is six-connected; H7=0 and Hurewicz give seven-connectivity, and representatives of the H8 basis yield wedge^36 S8 via homological Whitehead. Pure ten-dimensional K has nonzero lower-degree homology and is not shellable.

## originality

PASS

Best-of-knowledge original exact nonequivariant homotopy classification for the ordinary 4-cut complex of KG(6,2). The strongest same-definition Kneser result in the primary 2024 paper is an ordinary 2-cut theorem in a triangle-free range; the 2025 sequel treats disjoint unions, squared paths and grids; published same-graph Čech and equal-numerical Heawood results concern different simplicial complexes. Resultary high-girth general theorem is inapplicable because this graph has triangles. No searched equivalent or logically stronger statement was found, with an explicit risk of an unindexed equivalent computation.

## value

PASS

KG(6,2) is the canonical first triangle-containing two-subset Kneser graph immediately after the Petersen graph KG(5,2); it is a natural boundary beyond the triangle-free two-cut result in the main literature. The ordinary four-cut construction is a standard graph complex invariant, and a complete integral homotopy type at this natural graph/cut parameter can be useful independently of an all-Kneser classification. The 36 eight-spheres arise two dimensions below its pure ten-dimensional facets, proving an informative nonshellability obstruction that cannot be read from the facet count or Euler characteristic alone. The certified homotopy classification uses a nontrivial acyclic matching and Alexander duality, not a textbook substitution or an arbitrary numerical slice. Its scope is explicitly one finite, nonequivariant graph and it does not assert broader families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
