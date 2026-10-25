---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The degree-five Clebsch folded cube is the Cayley graph on F_2^4 with jumps 1,2,4,8,15 (not the ten-regular alternate Clebsch graph). A face of the dominance complex is exactly a subset containing no closed neighborhood N[v] entirely; enumeration of all 65,536 masks yields 53,730 nonempty faces, with f-vector through dimension 11 matching source. Independent deterministic toggle matching in vertex order 0..15 yields 26,799 pairs and exactly 132 critical faces: one 0-face and 131 9-faces. Independently oriented all 401,088 nonempty Hasse cover incidences, with paired edges reversed; complete Kahn topological sort visits every face. Forman's theorem gives a CW complex with a point and 131 nine-cells and no intermediate cells, hence wedge of 131 S^9, free integral homology and trivial fundamental group. Exhaustive check is finite for this specific graph, not a family-wide formula.

## originality

PASS

The dominance complex is Alexander dual to a complement open-neighborhood complex; Matsushita–Wakatsuki general duality and graph-family calculations are relevant but do not state a Clebsch wedge of 131 nine-spheres. Results for the same Clebsch graph's ordinary independence complex (wedge^9 S3) and open-neighborhood/Lovász complex (wedge^31 S2) concern different simplicial functors and cannot be substituted. Resultary searches for 131 and dominance/Clebsch found no exact previous classification; O PASS best of knowledge.

## value

PASS

This gives a complete integral homotopy invariant of a canonical strongly regular, vertex-transitive folded cube for a natural domination-theoretic simplicial complex. The large 131 multiplicity and concentration at dimension nine, despite dimension eleven, is a nonroutine exact finite benchmark for combinatorial topology and graph-complex duality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
