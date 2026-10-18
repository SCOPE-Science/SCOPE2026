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

Used exact directed multihomomorphism definition: triples of nonempty pairwise-disjoint subsets (A,B,C) of Z/9 with all arcs from A to B, B to C, C to A present for cyclic steps 1..4. Independently enumerated all 4^9 assignments as bitmasks: 720 valid cells, f=(90,270,270,90), 1,917 Hasse covers. A separately implemented coordinate-vertex staged matching pairs 359 covers and leaves only ({0},{1},{5}) dimension0 and ({6},{1},{2,5}) dimension1. Independently built and topologically sorted the directed Hasse graph with precisely matched edges reversed; all 720 vertices sorted without cycle. Forman discrete Morse thus yields a CW complex with one 0- and one 1-cell, necessarily S^1. Cellular mod2 Betti (1,1,0,0) follows from the source verifier but alone would not prove homotopy type.

## originality

PASS

Dochtermann–Singh introduce the directed Hom functor and identify topology for nontransitive tournament targets as an open direction; their transitive-target theorem and seven-vertex Möbius example do not determine regular cyclic tournament R9. Published Resultary results regarding the path homology of cyclic tournaments and directed flag complexes treat different functors, not multihomomorphism complexes from oriented C3; self-hit did not establish earlier coverage.

## value

PASS

Canonical smallest source oriented cycle and symmetric 9-vertex regular target form a natural benchmark for directed Hom theory. The complete homotopy type (not just homology) is a motivated finite answer to the literature’s nontransitive-target program; lack of an infinite family theorem is explicitly acknowledged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
