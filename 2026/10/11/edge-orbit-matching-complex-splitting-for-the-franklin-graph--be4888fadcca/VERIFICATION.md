---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

The LCF [5,-5]^6 construction has 12 cubic vertices and exactly 18 edges. Independent enumeration from its edge definition yields the full matching-complex face vector (18,117,336,417,186,17) and both complete deletion/link orbit face-vector classes (6 and 12 edges). A fresh explicit acyclic discrete-Morse matching independently reconstructs 1091, 875, 215, 869 and 221 nonempty faces, respectively, with critical profiles {0:1,3:12}, {0:1,3:8}, {0:1,2:4}, {0:1,2:1,3:11}, {0:1,2:2}. All five oriented Hasse incidence digraphs topologically sort (3942,3105,609,3075,633 incidences). The exceptional B-edge deletion integral signed Morse boundary was independently recomputed as (-1,-1,-1,-1,1,-1,0,-1,0,-1,1), a primitive unit row, eliminating its sole 2-cell against one 3-cell. Under the representative-orbit reduction (48 automorphisms, two orbits, verified in inspected verifier, and independently 6/12 profiles), M(F) is a wedge of 12 S^3. For each edge, link is a wedge of S^2 and deletion a wedge of S^3; pi_2(target)=0 gives the null inclusion and a genuine deletion-link cofiber splitting, not a field-rank inference.

## originality

PASS

Best-of-knowledge originality: the final claim is the full *ordinary* Franklin matching-complex integral homotopy and both 6+12 edge-orbit deletion/link sphere profiles, including exceptional integral degree. The broad claw-free and outerplanar literature is not an implication-level substitute for this complete finite orbit calculation. No retrieved covering exact table was identified. Resultary query failed, leaving an explicit database literature risk, not a negative result.

## value

PASS

The complete edge-orbit deletion/link profile is a motivated local-to-global topological invariant of the canonical Franklin cubic symmetric graph, not just a lone small Betti number. Its two local profiles differ even though both cofiber splittings yield 12 three-spheres; one profile crucially has nontrivial integral cell cancellation invisible to field-rank tables. The exact self-contained finite invariant could be reused to test broader matching-complex calculations without claiming a family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
