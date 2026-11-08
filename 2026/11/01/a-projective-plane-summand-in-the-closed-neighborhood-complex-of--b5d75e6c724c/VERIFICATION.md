---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For ordinary KG(8,3), all 56 vertices are 3-subsets, with ten disjoint neighbors plus each center in an 11-vertex closed neighborhood. Independently built all 56 facets and their downward closure: 111,482 nonempty faces and dimensions0..10 f-vector (56,1540,8400,18270,25872,25872,18480,9240,3080,616,56). Independently regenerated 54,910 actual elementary simplicial free-face/coface removals, resulting in exactly 56 vertices, 628 edges and 978 triangles. The integral 2-complex reduction pairs 569 edges with triangles, 55 tree edges with vertices, leaving one vertex, four edges and 409 2-cells; the source verifies the full acyclic Hasse orientation and the dependency DAG of attaching-word substitutions. Independently reconstructed all 409 attaching words, performed three single-generator degree-one CW cancellations, and obtained one oriented circle and 406 2-cell relators with degree histogram -2:60,0:299,+2:47. After choosing one degree-two relator to form RP2, all 405 remaining even-degree attaching loops vanish in pi1(RP2)=Z2 and split off 405 S2. Independent raw F2/F3/F5 cellular ranks 572/573/573 agree with mod2 Betti (1,406) and odd-prime (0,405). Since pure 10-dimensional with H1 torsion, shellability is excluded. This proves the exact finite homotopy type and not merely an integral homology guess.

## originality

PASS

A specific exact closed-neighborhood homotopy classification of the naturally defined Kneser graph KG(8,3). Full-text primary Matsushita closed-neighborhood work establishes broad suspension/duality/graph-fundamental-group results but not this explicit 56-vertex RP2 wedge classification; Matsushita–Wakatsuki addresses mainly open-neighborhood and dominance duals. The specialized triangle-free edge-disjoint 4-cycle theorem is inapplicable: the target graph has overlapping 4-cycles sharing edge (012,345). Resultary same-object searches returned no equivalent classification. Best-of-knowledge PASS with unindexed-computation risk.

## value

PASS

A 56-vertex Kneser graph and its closed-neighborhood complex are standard canonical combinatorial-topology objects. The exact emergence of RP2 2-torsion together with 405 independent 2-spheres gives a full integral homotopy classification for a natural, highly symmetric complex and a sharp non-shellability obstruction. Exact attaching words lift simple field-homology data to an independently useful homotopy result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
