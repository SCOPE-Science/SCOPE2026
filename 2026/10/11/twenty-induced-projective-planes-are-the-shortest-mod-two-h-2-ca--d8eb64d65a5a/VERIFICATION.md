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

Independently rebuilt the 40 tetrahedra from the public Lutz facet table (exact same 40 labelled facets as in assigned verify.py), yielding f=(11,51,80,40). A separately written GF(2) bit-vector boundary reduction finds rank ∂2=40 and rank ∂3=39 on 80 triangles, hence H2 dimension one. For all vertex subsets of sizes 1..6, independently constructed complete local 2-cycle spaces and reduced them modulo global 3-boundaries; numbers of supporting subsets are 0,0,0,0,0,20. Every minimizing induced complex has six vertices, fifteen edges, ten triangles, no tetrahedron, links single cycles and χ=1, so is RP2. Exhaustive degree/triangle-compatible vertex bijections with final facet preservation gave 48 automorphisms and 12+8 carrier orbit sizes with the specified two representatives. All searches over 11 vertices or labelled permutations finite and exhaustive; this is mod-two homology, not integral H2.

## originality

PASS

The exact original Lutz public table contains this triangulation and all facets, but not the minimum induced H2 support, twenty induced RP2 carriers, or the action of its automorphisms on those carriers. Other indexed research addresses shortest mod-two H1 loops, not H2, and a well-known standalone six-vertex RP2 is not an occurrence census inside this RP3. No stronger claim implying these enumerated data was found in actual literature/Resultary comparisons; an unindexed historical facet census remains a risk.

## value

PASS

The vertex-minimal triangulation of a standard manifold has a canonical nonzero mod-two middle homology class. Knowing its sharp minimum vertex support and exactly which minimal induced RP2 subcomplexes realize it, including complete orbit decomposition, is a natural and usable invariant for triangulation topology, embedding constraints and symmetry comparisons rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
