---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS. The specified icosahedral graph is a 12-vertex 30-edge planar 20-face triangulated sphere. Independent edge-by-edge enumeration of ordinary matchings yielded 5,887 nonempty faces with f-vector (30,315,1400,2535,1482,125). The full 23,130 face incidences and prescribed 2,866 discrete-Morse pairs form a directed acyclic graph (complete Kahn topological sort); critical cells are one vertex, 109 three-cells, 45 four-cells. Independent signed gradient-path recursion reconstructed the 109x45 Morse boundary: rank mod 3=44 and rank mod 2,5=45; specified exact 45x45 minor determinant +3. Since all maximal minors divisible by 3 and one equals 3, SNF=1^44,3; the 3-skeleton is bouquet of 109 S^3 and pi_3 is classified by integer degree vectors, so splitting yields 64 S^3 wedge M(Z/3,3). The torsion violates any wedge-of-spheres or contractible conclusion. Both integral exact certificate and complete incidence DAG are essential; modular Betti numbers alone would not prove the homotopy type.

## originality

PASS

Best-of-knowledge PASS after exact-object and logical-implication comparison. Theorem 2 of Bayer–Jelić Milutinović–Vega concerns outerplanar graphs; icosahedron 30 edges on 12 vertices is not outerplanar (outerplanar bound <=21). Their planar Conjecture 11 is an unproved assertion, not prior coverage, and the certified 3-torsion refutes it. Classical matching complexes of K_n or K_{m,n} have 3-torsion but do not imply icosahedral matching complex calculation. An indexed-search miss alone is not treated as novelty proof.

## value

PASS

PASS. An explicit integral 3-torsion obstruction in the ordinary matching complex of a planar polyhedral graph disproves the specifically stated universal planar matching-complex sphere-wedge conjecture. The complete finite homotopy type gives a reproducible, graph-natural counterexample and more structure than a mere negative computational check, so the motivated finite computation has substantial mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
