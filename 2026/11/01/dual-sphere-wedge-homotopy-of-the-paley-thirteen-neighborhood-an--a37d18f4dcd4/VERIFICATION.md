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

Enumerating quadratic residues Q={1,3,4,9,10,12} yields the unique graph P13. All 8192 subsets are classified by the actual predicates sigma⊆N(v) for some v (neighborhood) and N[v] not subset sigma for all v (dominance); face totals 598 and 7592 and claimed f-vectors follow. Independent reimplementation of deterministic 0..12 vertex-toggle matching gave 286 and 3783 disjoint pairs and critical cells exactly (one 0-cell,25 2-cells) and (one 0-cell,25 8-cells). Independent explicit oriented Hasse adjacency digraphs were completely topologically sorted on all 598 and 7592 faces, establishing acyclicity rather than just Morse counts. Forman’s theorem then yields a CW model with one vertex and only 25 cells of one dimension >=2, i.e. the claimed integral sphere wedges. Multiplication by 2 gives P13 ≅ complement graph; Matsushita–Wakatsuki Alexander duality explains pairing, not individual wedge ranks. The complete finite calculation does not claim all Paley orders.

## originality

PASS

An exact pair of integral homotopy computations for the canonical thirteen-vertex Paley graph is not supplied by general dominance-neighborhood Alexander duality, six-regular versus bounded-degree circulant results, or indexed Paley order 17/25 computations.

## value

PASS

A motivated exact integral homotopy classification for a canonical strongly regular self-complementary graph central to neighborhood-complex coloring topology and its Alexander-dual domination invariant. Complete finite matchings establish much more than field Betti numbers, without pretending to solve an arbitrary Paley family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
