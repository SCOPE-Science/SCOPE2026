---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The 12-vertex icosahedron with 30 edges and 20 triangular faces gives 60 oriented-edge truncation vertices and 90 edges. Every distance-two Rips shortcut is homotopic to a two-step graph walk. Its 12 pentagonal face boundaries lie in 4-simplices; each of its 20 hexagons has an explicit four-triangle filling, so the Rips complex is simply connected by planar facial generation. Exact exhaustive simplex counts are (60,270,340,120,12), Euler characteristic 22. The inspected check.py has a genuine maintained free-coface dictionary and a 120-step pairwise codimension-one elementary collapse, removing all simplices of dimension greater than 2 and leaving face counts (60,270,232). Consequently H2 is free of rank 21 (subgroup of free C2), and Hurewicz plus homological Whitehead give the integral wedge. Independently reconstructed all 60 vertices, 90 edges, 20 icosahedral faces, every Rips face and Euler 22; the 120-collapse proof is justified by inspected exact verifier, not claimed independently rerun.

## originality

PASS

Best-of-knowledge PASS: the precise 60-vertex truncated-icosahedron radius-two homotopy wedge is not supplied by the closely relevant Platonic-solids classification, nor by graph-power collapse theorems whose hypotheses fail at girth five. Other polyhedral Rips complexes in the published database are different graphs or metrics. A specialized unindexed computation could still predate this.

## value

PASS

A natural highly symmetric Archimedean 60-vertex graph has a precise previously unclassified scale-two integral homotopy type, beyond Betti-number data. The explicit planar face filling plus simplicial collapse provides reusable structural method and a benchmark for graph-metric Rips filtrations, so this is not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
