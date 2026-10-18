---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

For C4□Cn with n≥7 the shortest graph distance is d_n+d_4. A clique not contained in adjacent columns must contain two same-row vertices in columns j−1 and j+1 of distance exactly two; every additional vertex is one of three center-column rows r−1,r,r+1. The endpoint pair B_(j,r) is unique for each outside face because no second distance-two pair fits. For each B, the four lower faces B∪T (T⊆{(j,r−1),(j,r+1)}) paired with addition of (j,r), processed in decreasing |T|, are genuinely free and remove all 32n non-slab faces in 16n simplicial collapse steps. Each remaining consecutive-column slab has eight vertices and four mutually disjoint forbidden cross edges, hence the boundary of a 4-cross-polytope, a triangulated S³. Adjacent slabs intersect in full four-vertex tetrahedra, all other and triple intersections empty. Cyclic gluing along these contractible intersections adds n S³ summands and a single S¹. Inclusion-exclusion for slabs gives faces (4n,18n,28n,15n), plus outside binomial counts gives full (4n,22n,40n,27n,4n). The separate independent Python enumeration verified every free pair and face count for n=7,8,9 and the source verifier handles n=7..24; finite checks only corroborate the all-n combinatorial proof.

## originality

PASS

The closest torus-grid source treats primarily square C_n□C_n instances and describes the same local cross-polytope mechanism; the lattice source concerns nonperiodic infinite integer grids. The present finite asymmetric thin C4□Cn family has a cyclic S¹ factor and exactly n three-spheres after a uniform exact finite collapse, neither implied by square-grid or infinite-lattice formulas. Both relevant primary articles were read in accessible full text. Resultary could not complete the current search; equivalent independent rectangular grid work remains a bounded risk.

## value

PASS

This is a full homotopy classification of a natural, infinite family of finite toroidal graph Rips complexes, with integral homology, exact face counts and an explicit certified elementary-collapse scheme. The width-four asymmetry and n≥7 boundary are geometrically motivated; the n sphere multiplicity and essential cycle are independently useful in metric topology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
