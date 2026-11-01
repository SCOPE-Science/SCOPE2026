---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For the 16 spanning-tree incidence vectors in the intrinsic 5-dimensional lattice, Edmonds rank inequalities over all 62 nonempty proper edge subsets give the complete facets. An independently written checker used graph-connectivity rank, exact affine ranks and a separate SciPy Qhull support enumeration: both yielded the same 16 facet masks. Intersecting them exhaustively produced 219 nonempty faces with dimensions (16,54,78,54,16,1). For every face, exact gcds of maximal minors of its primitive normal-ray matrix distinguish smooth from nonsimplicial cones; exactly 94 are singular (16 vertices, 48 edges, 30 2-faces) and no simplicial nonunimodular cone occurs. The 30 maximal singular 2-faces are 24 primitive triangles and six primitive parallelograms, with full S4 orbit sizes 12,12,6; each normal cone has four rays, all triples saturated, and primitive relation (+1,+1,-1,-1), which identifies the rank-3 generic transverse singularity with ad-bc=0. Every singular face is contained in a maximal singular 2-face; hence the reduced singular locus has precisely 30 components. The nonsimplicial-orbit set coincides with the singular set, proving reduced equality with the non-Q-factorial locus. The finite analysis is exhaustive only because the rank inequalities cover this fixed matroid and all their facet intersections were enumerated; it is not an extrapolation to larger graphs.

## originality

PASS

Best-of-knowledge originality: the complete 30-component local singularity stratification, 24/6 component surface split, 94 singular orbits and generic conifold cones were not covered by the inspected primary statements. The K4 Bergman example/normal-fan dictionary (Feichtner–Sturmfels), torus-orbit projective normality (Howard), Gorenstein criteria (Hibi et al., Lasoń–Michałek) and face enumeration (Ferroni–Schröter) are prior methods or different invariants. Resultary was actually queried for equivalent geometric and exact numeric aliases. An unindexed exact polytope/fan computation remains a bounded priority risk. This is not proof of global novelty or an invented independent certification.

## value

PASS

The fivefold X_P is a canonical toric compactification of the Grassmannian torus orbit for the first richly structured complete-graph graphic matroid K4. Identifying its exact singular locus as 24 planes and six Segre surfaces, with uniform ordinary-node transverse geometry and a precise non-Q-factoriality obstruction, is a natural complete local-geometric classification. The motivated object/invariant pairing and the local analytic type are not given by a generic toric criterion or the already known f-vector alone. This fixed finite example can be independently useful for birational geometry, toric resolutions and comparison with larger graphic-matroid orbit closures without claiming a generalization or major theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
