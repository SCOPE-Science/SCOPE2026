---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Normalize projective coordinate triples over F₃ by first nonzero coefficient 1; obtain 13 points and 13 lines, each line containing 4 points. The 26-vertex bipartite *nonincidence* graph has nine neighbors per vertex. Its open Lovász neighborhood complex splits into disjoint point and line components, and duality identifies each with all nonempty subsets of 13 nine-point line complements. I independently constructed every one of 3,861 faces and confirmed dimension-ordered f-vector (13,78,286,702,1170,1014,468,117,13). Independent F₂ reduced boundary ranks (1,12,66,220,482,649,364,104,13), with first entry augmented ∂0, yield β4=39, β5=1. More importantly, I independently reconstructed the package's pivot toggle matching: 1,910 nonempty-face pairs and exactly 1 critical vertex, 39 critical 4-cells and 1 critical 5-cell; the full 20,085-edge oriented Hasse diagram topologically sorts (no directed cycle). An independent signed integral Morse reduction computes all 39 components of the unique critical 5-cell boundary to be zero. The 4-skeleton is a wedge of 39 S4, for which π4≅H4 by Hurewicz; zero attaching degrees imply the 5-cell is null-attached. Thus each component ≃(∨39 S4)∨S5, without mistaking mod-two homology for an integral homotopy proof. Code paths check_plane_neighborhood.py and independent_plane_check.py were inspected at frozen Git blob SHAs.

## originality

PASS

Best-of-knowledge PASS for the exact *nonincidence* PG(2,3) graph's integral two-component homotopy type; point-line incidence-graph neighborhood complexes and nonblocking complexes of other projective orders are not interchangeable. The Matsushita general fundamental-group theorem does not imply a rank-39 S4 wedge with a 5-cell. Published Steiner *incidence* graph circle-wedge result is on the opposite adjacency and not covering. The actual finite-geometry alias 'sets avoiding a projective line' was included in searching. Residual risk of literature under blocking-set Alexander dual or finite-geometry terms is acknowledged.

## value

PASS

The 13-point order-three projective plane is a natural symmetric finite geometry. Its open-neighborhood/nonblocking complex has genuinely mixed integral higher homotopy dimensions, and proving its S5 attaching map vanishes (not merely computing Betti ranks) is an independently useful exact classification and reproducible benchmark. No general plane-order theorem is required for the exact intrinsic case to have value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
