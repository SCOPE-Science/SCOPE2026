---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The defining graph is exactly generalized Petersen GP(10,2): edges u_i u_{i+1}, u_i v_i, v_i v_{i+2} (indices mod10). Independently generated all independent vertex subsets recursively: exactly 5,828 with empty face, nonempty size counts 20,160,660,1510,1912,1240,320,5. Independently constructed vertex-order greedy matching on 5,827 nonempty faces with 2,911 matched covers and 5 critical cells: one singleton {0} and four specified 6-vertex faces. Constructed all 27,620 oriented Hasse edges and topologically sorted all 5,827 vertices: acyclic. A perfect finite Forman matching with one 0-cell and four 5-cells gives wedge of four S^5, because all 5-cell attachments land in the sole 0-skeleton. Euler characteristic −3 supports the result but does not establish homotopy type.

## originality

PASS

Berghoff 2020 studies independence-complex homology and explicitly works out Petersen and cubical examples; materially inspected paper does not compute dodecahedral GP(10,2). Goyal–Shukla–Singh 2019 provide wedge decompositions for different graph families, not this generalized Petersen instance. Published related dodecahedral MATCHING, neighborhood, Rips and Čech complexes are different complexes and therefore do not cover ordinary independent vertex sets.

## value

PASS

An explicit homotopy invariant of the canonical dodecahedron graph is a natural previously undetermined exact case. The finite acyclic matching proves a complete homotopy classification, strictly beyond an Euler characteristic or homology table; it is useful to compare independence complexes of Platonic and generalized Petersen graphs without requiring a family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
